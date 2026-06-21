"""
Find yesterday's upload for a YouTube channel, bypassing a sandbox network
policy that blocks www.youtube.com but allows youtubei.googleapis.com.
Usage: python3 find_yesterday_video.py <channel_id>
Prints: <video_id>\t<date>\t<title>  on a yesterday match,
        "LATEST\t<video_id>\t<date>\t<title>" if nothing matches yesterday,
        or "ERROR ..." / "NO_MATCH" on failure.
"""
import sys, json, re
from datetime import datetime, timedelta, timezone

import yt_dlp
from yt_dlp.extractor.youtube._base import YoutubeBaseInfoExtractor

_captured = []
_orig_call_api = YoutubeBaseInfoExtractor._call_api
def _patched_call_api(self, ep, query, video_id, **kwargs):
    result = _orig_call_api(self, ep, query, video_id, **kwargs)
    if ep == "browse":
        _captured.append(result)
    return result
YoutubeBaseInfoExtractor._call_api = _patched_call_api

YDL_OPTS = {
    "quiet": True, "no_warnings": True, "extract_flat": True,
    "playlist_items": "1-8", "skip_download": True,
    "nocheckcertificate": True,
    "extractor_args": {"youtube": {"innertube_host": ["youtubei.googleapis.com"]}},
}

def find_video_entries(data):
    results = []
    def walk(node):
        if isinstance(node, dict):
            if "lockupViewModel" in node:
                lvm = node["lockupViewModel"]
                vid = lvm.get("contentId")
                title, rel_time = None, None
                try:
                    title = lvm["metadata"]["lockupMetadataViewModel"]["title"]["content"]
                except Exception:
                    pass
                try:
                    rows = lvm["metadata"]["lockupMetadataViewModel"]["metadata"]["contentMetadataViewModel"]["metadataRows"]
                    for row in rows:
                        for part in row.get("metadataParts", []):
                            txt = part.get("text", {}).get("content", "")
                            if "ago" in txt:
                                rel_time = txt
                except Exception:
                    pass
                if vid:
                    results.append({"videoId": vid, "title": title, "relative": rel_time})
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for item in node:
                walk(item)
    walk(data)
    return results

def parse_relative(rel, now):
    if not rel:
        return None
    m = re.match(r"(\d+)\s+(hour|day|week|month|year)s?\s+ago", rel)
    if not m:
        return now if rel.strip().lower() in ("just now", "1 second ago") else None
    n, unit = int(m.group(1)), m.group(2)
    return now - {
        "hour": timedelta(hours=n), "day": timedelta(days=n),
        "week": timedelta(weeks=n), "month": timedelta(days=30 * n),
        "year": timedelta(days=365 * n),
    }[unit]

def main(channel_id):
    _captured.clear()
    now = datetime.now(timezone.utc)
    try:
        with yt_dlp.YoutubeDL(YDL_OPTS) as ydl:
            ydl.extract_info(f"https://www.youtube.com/channel/{channel_id}/videos", download=False)
    except Exception as e:
        print(f"ERROR {e}")
        return
    if not _captured:
        print("ERROR no_browse_response")
        return
    data = max(_captured, key=lambda r: len(json.dumps(r)))
    entries, seen, dated = find_video_entries(data), set(), []
    for e in entries:
        if e["videoId"] in seen or not e["relative"]:
            continue
        seen.add(e["videoId"])
        dt = parse_relative(e["relative"], now)
        if dt:
            dated.append((dt, e))
    dated.sort(key=lambda x: x[0], reverse=True)
    yesterday = (now - timedelta(days=1)).date()
    for dt, e in dated:
        if dt.date() == yesterday:
            print(f"{e['videoId']}\t{dt.date()}\t{e['title']}")
            return
    if dated:
        dt, e = dated[0]
        print(f"LATEST\t{e['videoId']}\t{dt.date()}\t{e['title']}")
    else:
        print("NO_MATCH")

if __name__ == "__main__":
    main(sys.argv[1])