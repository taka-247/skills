---
name: it-daily-digest
description: >
  Use this skill to generate a daily digest of the 5 most important IT news
  items from yesterday. Trigger this skill whenever the user asks for recent
  IT news, a daily tech roundup, what happened in tech yesterday, or anything
  like "what's new today", "daily tech update", "show me yesterday's IT news",
  "any AI tool updates", or "what should I know today as a developer". Always
  use this skill — do not answer from memory, as IT news changes daily.
---
 
# IT Daily Digest Skill
 
Generate a curated digest of the **5 most important** IT developments from
**yesterday**, filtered specifically for a web application developer.
 
---
 
## Target Stack
 
**Frontend:** React, TypeScript  
**Backend:** Node.js, MongoDB
 
---
 
## Priorities (ranked highest to lowest)
 
1. **🤖 AI tools & LLM updates** — New models, coding assistants, AI-powered
   dev tools, or API changes that can accelerate React/TypeScript/Node.js
   development (e.g. new Claude/GPT/Gemini capabilities, Cursor updates,
   GitHub Copilot changes, AI code generation tools)
2. **🛠️ Dev tools & ecosystem news** — New libraries, frameworks, or tooling
   that meaningfully improve the React / TypeScript / Node.js / MongoDB
   workflow
---
 
## Relevance test (apply before including any item)
 
Ask: **"Does this directly change how I write or ship React/TypeScript/Node.js/MongoDB web apps today?"**
If the answer is no, exclude it. If you are unsure, exclude it.
 
## Exclusions (never include these)
 
- Security patches, CVEs, vulnerability advisories, and runtime/dependency
  updates (e.g. "Node.js patches CVE-XXXX", "MongoDB security release",
  "npm package vulnerability")
- Routine patch/minor releases with no meaningful user-facing change
- Compiler/toolchain infrastructure changes that don't affect how you write
  application code (e.g. TypeScript compiler rewrites, build speed improvements,
  tsconfig changes, Go-based compiler ports) — these are internal engineering
  changes, not features a web app developer uses day-to-day
- Language version releases unless they introduce new syntax or APIs you would
  actually use in a React/Node.js app right now
- Cloud infrastructure news (AWS, Azure, GCP, Heroku, Vercel platform
  changes, etc.) unless it directly changes how you write React/Node.js code
- Mobile development news (Flutter, Swift, Kotlin, React Native)
- Database news unrelated to MongoDB
- Opinion pieces or trend articles with no concrete announcement
- Anything unrelated to building web application features
---
 
## Workflow
 
### Step 1 — Search for Yesterday's News
 
Take time to search broadly — aim for **8–10 searches** across multiple
angles and sources. Always use the actual date of yesterday in queries.
 
**Mandatory source coverage — fetch these directly every run:**
- https://techcrunch.com/
- https://www.wired.com/
- https://thenextweb.com/
- https://www.reuters.com/technology/
- https://edition.cnn.com/business/tech
- https://technologymagazine.com/
- https://thenextweb.com/
- https://www.vox.com/technology
Use `web_fetch` on at least 3–4 of these homepages to pull the latest
headlines directly, then supplement with targeted web searches:
 
- `AI coding tool LLM release [yesterday's date]`
- `React TypeScript JavaScript developer tool [yesterday's date]`
- `GitHub Copilot Cursor Claude GPT Gemini update [yesterday's date]`
- `web development framework library release [yesterday's date]`
- `open source AI model coding [yesterday's date]`
- `site:techcrunch.com developer AI tool [yesterday's date]`
- `site:thenextweb.com web development [yesterday's date]`
Fetch full article pages (`web_fetch`) for any promising headlines that
need more detail. If a search returns nothing from yesterday, broaden to
the last 48 hours and note the date.
 
### Step 2 — Filter & Rank
 
From all gathered results, select the **5 most relevant items** using this
scoring order:
 
| Priority | Type | Keep if… |
|---|---|---|
| 1 | AI tool / LLM update | Directly speeds up React/TS/Node dev |
| 2 | Dev tool / library | Meaningful new capability or DX improvement |
 
If fewer than 5 genuinely relevant items exist from yesterday, include the
most recent items from the past 48 hours and note the date.
 
### Step 3 — Format the Digest
 
Present the 5 items in this exact format:
 
---
 
## 🗓️ IT Daily Digest — [Yesterday's date, e.g., Jun 18, 2026]
 
*Curated for: React · TypeScript · Node.js · MongoDB*
 
---
 
### 1. [Title]
**Category:** [AI Tool / Dev Tool / Library / Breaking Change]  
**Relevant to:** [React / TypeScript / Node.js / MongoDB — whichever apply]
 
**What happened:** 2–3 sentences in plain language.
 
**Why it matters for you:** 1–2 sentences on the concrete benefit —
be specific about how it affects your React/TypeScript/Node.js/MongoDB work.
 
**Learn more:** [URL]
 
---
 
*(Repeat for items 2–5)*
 
---
 
## 💡 Today's Key Takeaway
*One sentence: the single most interesting or actionable thing from today.*
 
---
 
### Format rules
- Use emoji icons: 🤖 AI/LLM, 🛠️ dev tool, 📦 library
- Lead with AI items — they always go first
- Keep language direct and developer-focused, no marketing fluff
- Always include a source URL
---
 
## Quality Checklist (self-check before responding)
 
- [ ] At least 3–4 of the mandatory sources were fetched directly via web_fetch
- [ ] At least 8 total searches/fetches were run
- [ ] All items are from yesterday (or last 48h if noted)
- [ ] AI/LLM items appear before other categories
- [ ] No security patches, CVEs, or vulnerability news included
- [ ] Each item passes the relevance test: "Does this directly change how I write or ship React/TypeScript/Node.js/MongoDB web apps today?"
- [ ] No compiler/toolchain infrastructure news (e.g. TS compiler rewrites, build speed, tsconfig changes) unless it adds new syntax or APIs usable in app code
- [ ] No cloud infrastructure items (AWS/Azure/GCP/Heroku platform news)
- [ ] No routine minor patch releases with no user-facing impact
- [ ] No mobile or non-web topics
- [ ] Each item has a concrete "why it matters for you" tied to the target stack
- [ ] Source URLs are included
 