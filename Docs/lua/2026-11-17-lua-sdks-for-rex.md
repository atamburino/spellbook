---
title: "Generate any service's API as a Lua SDK for rex"
source_url: https://x.com/dillon_mulroy/status/2122781686077210795
linked_urls:
  - https://pbs.twimg.com/media/HXWifAzXcAA88CZ.jpg
author: "Dillon Mulroy (@dillon_mulroy)"
saved: 2026-11-17
tags: [lua, rex, sdk-generation, cloudflare, planetscale]
requested_via: "X reply by @AndyTamburino (https://x.com/AndyTamburino/status/2122859057048392172), passed on by Chief and dr eggbot"
---

# Generate any service's API as a Lua SDK for rex

## Post

> what if you could have or generate every services api you love and use as a lua sdk ready for use in rex

(Dillon Mulroy, @dillon_mulroy, Nov 17, 2026, with one code screenshot attached)

## Why saved

"save this for me and hand this off to our doc bot"

## Reference

The post is an idea pitch: take the APIs of services you already use and generate typed Lua SDKs for them, so they drop straight into rex scripts. The attached screenshot shows what that would look like. A `distilled` library is loaded with a rex host, then generated `cloudflare.workers` and `planetscale` clients are built against that host, and each is wrapped in a `rex.action` that lists items, using `distilled.check(...)` plus a paginated `*_items(...):collect(100)` call.

Code from the screenshot, transcribed:

```lua
local distilled = require("distilled")
local host = require("distilled.host.rex")()
local account = os.getenv("CLOUDFLARE_ACCOUNT_ID")
local org = os.getenv("PLANETSCALE_ORGANIZATION")

local workers = require("cloudflare.workers").new({ host = host })
local ps = require("planetscale").new({ host = host })

rex.action({
  name = "cf_workers",
  title = "Cloudflare: list Workers",
  run = function()
    local out = {}
    for i, s in ipairs(distilled.check(workers:list_scripts_items({ account_id = account }):collect(100))) do
      out[i] = s.id
    end
    return out
  end,
})

rex.action({
  name = "ps_databases",
  title = "PlanetScale: list databases",
  run = function()
    local out = {}
    for i, db in ipairs(distilled.check(ps:list_databases_items({ organization = org }):collect(100))) do
      out[i] = db.name
    end
    return out
  end,
})
```

Worth keeping: the pattern of one shared host object injected into every generated client, credentials read from environment variables, and list endpoints exposed as paginated iterators you `collect(n)` and unwrap with `check`.

The post has no outside link, only the image. What rex and `distilled` are isn't explained in the post: not fetched, no linked page.
