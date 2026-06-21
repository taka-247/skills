---
name: daily-todo
description: >
  Use this skill to return the user's daily todo list. Trigger whenever the user asks
  for their daily todo list, morning routine, or what they should do today. The static
  list is defined in this file — read it directly. For items marked #1 and #2, always
  use web_search to find fresh content each time; never answer those from memory.
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
1. Use `web_fetch` on each channel's RSS feed (XML, not the `/videos` page — YouTube's
   anti-bot wall blocks direct fetches of the rendered `/videos` page, but the RSS
   endpoint is plain XML and is not blocked) to get the latest uploads and check
   publish dates:
   `https://www.youtube.com/feeds/videos.xml?channel_id=[CHANNEL_ID]`
2. If a feed fetch fails or doesn't clearly show yesterday's video, fall back to
   `web_search` with a query like:
   `site:youtube.com/watch "[channel name]" after:[yesterday's date]`
3. If the fall back didn't work out, just list up one latest video of each channel, i.e. put three video url there. Plus, no need to include the reason why 1 and 2 failed

**YouTube channels (handle → channel ID for the RSS feed):**
- @misayuka.podcast → `UC-8PjUhkPibqh1ogdKaWk2w` → https://www.youtube.com/feeds/videos.xml?channel_id=UC-8PjUhkPibqh1ogdKaWk2w
- @BusinessInsider → `UCcyq283he07B7_KUX07mmtA` → https://www.youtube.com/feeds/videos.xml?channel_id=UCcyq283he07B7_KUX07mmtA
- @LearnEnglishWithTVSeries → `UCKgpamMlm872zkGDcBJHYDg` → https://www.youtube.com/feeds/videos.xml?channel_id=UCKgpamMlm872zkGDcBJHYDg
**Notes:**
- If multiple channels published yesterday, pick one video randomly
- If no channel published yesterday, say so clearly — do not guess or fabricate a link
 