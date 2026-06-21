---
name: daily-todo
description: "Use this skill to return the user's daily todo list. Trigger whenever the user asks for their daily todo list, morning routine, or what they should do today. The static list is defined in this file — read it directly. For items marked #1 and #2, always use web_search to find fresh content each time; never answer those from memory."
---

# TODO List

The following bullet list should be returned when the user asks for their daily todo list:

- stretch my body and read through IT Daily Digest
- drink 2 cups of water
- rotate shoulders and neck 100 times each
- eyes exercise
- work out * 50 times each
  - sit-ups
  - push-ups
  - back-extensions
  - grip
  - toe-up
- beauty
  - soften cheeks
  - take out K
- english
  - one interesting article for reading
    - #1
  - one video for listening
    - #2
- tech
  - learn new thing
- 30 mins piano lesson

## What Claude Does For The User

### #1 — Article for Reading

Use `web_search` to find one interesting article and give **only the URL** to the user — no title, no description.

The article should ideally relate to one of the following:
- Good life hacks in Japan
- Amazing products making life much better
- New discoveries or things that could potentially change our life
- Interesting Japanese culture, tradition, trend, event, or food spotlighted soon or recently
- Something very interesting that is worth reading through
- Things related to Japan are preferred but not required
- Articles must be written in English

### #2 — Video for Listening

Find one video published **yesterday** from one of the following YouTube channels and give **only the URL** to the user — no title, no description.

**Strategy (try in order):**

1. **Primary: yt-dlp via the YouTube InnerTube API host.** In sandboxed environments, `www.youtube.com` (and therefore its RSS feed endpoint, despite being plain XML) is often blocked at the network-egress level — not by YouTube's anti-bot wall, but by the sandbox's own allowlist. The host `youtubei.googleapis.com` (YouTube's internal "InnerTube" API, which serves the data behind the channel "Videos" tab) is commonly allowed even when `www.youtube.com` is not, and yt-dlp can be pointed at it directly. Per-video pages still trigger YouTube's bot-check, so do **not** fetch `watch?v=...` directly for metadata — instead pull the channel's video list (which embeds a relative-time string like `"1 day ago"`) and convert that to an absolute date locally.

   ```bash
   pip install -q yt-dlp  # if not already installed
   python3 find_yesterday_video.py <CHANNEL_ID>
   ```

   The script lives at `daily-todo/find_yesterday_video.py` in this repo.
   Run once per channel ID below.

   The video URL is `https://www.youtube.com/watch?v=<video_id>` from the
   printed `video_id`. If the output starts with `LATEST`, that channel had
   no upload dated exactly yesterday — use its most recent video instead.

2. If the script errors for a channel (e.g. `ERROR ...` or `NO_MATCH`), fall
   back to `web_search` with a query like:
   `site:youtube.com/watch "[channel name]" after:[yesterday's date]`

3. If that fallback also doesn't work out, just list up one latest video of
   each channel, i.e. put three video URLs there. Plus, no need to include
   the reason why 1 and 2 failed.

**YouTube channels (handle → channel ID):**
- @misayuka.podcast → `UC-8PjUhkPibqh1ogdKaWk2w`
- @BusinessInsider → `UCcyq283he07B7_KUX07mmtA`
- @LearnEnglishWithTVSeries → `UCKgpamMlm872zkGDcBJHYDg`

**Notes:**
- If multiple channels published yesterday, pick one video randomly
- If no channel published yesterday, say so clearly — do not guess or fabricate a link