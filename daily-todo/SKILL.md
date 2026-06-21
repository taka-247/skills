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
1. Use `web_fetch` on each channel's `/videos` page to get the latest uploads and check publish dates
2. If that doesn't clearly show yesterday's video, fall back to `web_search` with a query like:
   `site:youtube.com/watch "[channel name]" after:[yesterday's date]`
**YouTube channels:**
- https://www.youtube.com/@misayuka.podcast/videos
- https://www.youtube.com/@BusinessInsider/videos
- https://www.youtube.com/@LearnEnglishWithTVSeries/videos
**Notes:**
- If multiple channels published yesterday, pick one video randomly
- If no channel published yesterday, say so clearly — do not guess or fabricate a link
 