#!/usr/bin/env python3
"""Mino Lee / Content Academy — wired board.

One pannable canvas. Two mechanisms share a single subdomain and a single Meta
pixel: a free live class (Thu 6pm ET) and a direct book-a-call page. The thing
that makes this funnel worth swiping sits between them — a five-question survey
on the THANK-YOU page that splits every registrant on money and urgency before
the class has even happened, then sends the buyers to a call and everybody else
into a $20-$247/mo SaaS.

Layout rule: one column per funnel STEP, parallel variants stack vertically
inside that column so an arrow never crosses a card it is not pointing at.

Run:  python3 build_board.py   ->  board.html
"""
import base64, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DIMS = json.load(open(os.path.join(HERE, "dims.json")))
SHOTS_SRC = os.path.join(HERE, "media", "full")

CARD_W = 330
CHROME = 166
X = {1: 60, 2: 470, 3: 880, 4: 1290, 5: 1700, 6: 2110, 7: 2520}

# id -> (asset, col, y, lane, title, url, note)
SHOTS = {
    # ---- LANE 1: the free live class
    "reg": ("01_Webinar_registration", 2, 150, "class", "Class registration",
            "https://start.contentacademy.io/class?el=ad",
            "Countdown to a REAL fixed datetime (Thu 6pm ET) — not an evergreen "
            "fake timer. Modal opt-in: first, last, email, PHONE (all required)."),
    "ty": ("02_Thank-you_page", 3, 150, "class", "Thank-you — 67% bar",
           "https://start.contentacademy.io/class/thank-you",
           "No confirmation. No calendar link. One CTA: “your spot is almost "
           "saved…” Endowed progress bar opens at 67%, not 0%."),
    "survey": ("03_Application", 4, 150, "class", "5-question survey",
               "https://start.contentacademy.io/class/survey",
               "Disguised as unlocking a free AI tool. It is the qualification "
               "gate. Testimonial interstitial fires right before the money question."),
    "call": ("04_Thank-you_page_qualified_-_call", 5, 150, "qual",
             "QUALIFIED → book a call",
             "https://start.contentacademy.io/class/call",
             "Auto-redirect after 1.4s. 9 video testimonials, 60-creators proof, "
             "iClosed booking widget. No price anywhere."),
    "ai": ("05_Upsell_OTO_unqualified_-_SaaS", 5, 700, "dq",
           "UNQUALIFIED → ContentHooks SaaS",
           "https://start.contentacademy.io/ai",
           "The “free gift” is a paid product. $20 / $97 / $247 per month. "
           "Everyone who fails the money gate gets monetised anyway."),
    "cal": ("09_Calendar_iClosed", 6, 150, "qual", "iClosed calendar",
            "https://app.iclosed.io/e/contentacademy/content-academy-demo-call",
            "“Content Academy Demo Call”. Email + name only. Stripe and Hotjar "
            "both load on the booking widget."),

    # ---- LANE 2: the direct call funnel + the back end
    "root": ("06_Opt-in_page_call_funnel", 2, 1620, "direct",
             "Direct call page (no class)",
             "https://start.contentacademy.io/",
             "Byte-identical to the qualified thank-you page. Same asset, two "
             "entry points — one for cold traffic, one for survey-qualified."),
    "hooks": ("07_Hook_library_bonus_tool", 3, 1620, "direct", "Free hook library",
              "https://start.contentacademy.io/ai/hook-library",
              "Ungated SEO/utility page. Copy-to-clipboard hooks. Top of the "
              "ContentHooks funnel and a standalone traffic asset."),
    "main": ("08_Main_sales_site", 4, 1620, "direct", "contentacademy.io",
             "https://contentacademy.io/",
             "The brand site. Framer build, 31:08 YouTube VSL, Whop community "
             "link (30,820 joined · 4.9 from 153 reviews)."),
}

# id -> (col, y, h, lane, kicker, title, rows[], foot)
DATA = {
    "ads": (1, 300, 420, "class", "TRAFFIC — HOW WILL GOT SERVED", "Meta / TikTok paid",
            [("Landing param", "?el=ad"), ("Meta pixel", "829859546688723"),
             ("Same pixel", "BOTH funnels"), ("TikTok pixel", "D6AKEHJC77U3L7SP8JQG"),
             ("Attribution", "HYROS acct 214594")],
            "One pixel across both funnels, by their own source comment. "
            "CompleteRegistration fires on /class/thank-you, not on the opt-in."),
    "vsl": (1, 1700, 400, "direct", "THE 9:51 VSL", "0 → 10K followers (4 steps)",
            [("Runtime", "9m 51s"), ("Player", "Wistia g3is6j1p25"),
             ("Source pulled", "1080p, ungated"), ("Words", "2,108"),
             ("CTA", "“book a demo call below”")],
            "Free 4K/1080p MP4 straight off Wistia. No token, no gate. "
            "Their entire pitch, downloadable with one curl."),
    "offer": (6, 1700, 460, "qual", "THE OFFER", "Content Academy",
              [("Program price", "NEVER STATED"), ("ContentHooks", "$20 / $97 / $247 mo"),
               ("Whop members", "30,820 joined"), ("Whop rating", "4.9 · 153 reviews"),
               ("Proof claim", "60 students past 10K"),
               ("Founder claim", "$101,698.55 Whop gross, Jan 2025")],
              "The high-ticket number appears nowhere on any page, in the VSL, "
              "or on Whop. It is revealed on the call only."),
    "proof": (5, 1700, 440, "direct", "PROOF ARCHITECTURE", "What they lead with",
              [("Follower counts", "520K · 1.3M · 900K"),
               ("Aggregate", "2.6 BILLION views"),
               ("Revenue screenshot", "Whop gross, dated"),
               ("Named students", "9 on the call page"),
               ("Income proofs", "$14K / $17K / $40K")],
              "Screenshots with dates and platform names, not typed claims. "
              "The Whop revenue shot is the single strongest asset on the page."),
}


# ---------------------------------------------------------------- routing logic
# Hangs BELOW the clean funnel line. Each entry is a condition and what fires.
# state: "yes" | "no" | "dq" | "unver"
BRANCH = [
    ("b_gate", X[4] + 15, 1150, "dq", "The gate is MONEY × URGENCY, and it is in the JS",
     "Decompiled straight out of <code>survey/page-bf93c16709583769.js</code>. "
     "You reach the call if <b>(priority = “all-in ASAP” OR “top 3”) AND income "
     "≥ $5K/mo</b>, or if <b>income $1K&ndash;$5K AND priority = all-in</b>. "
     "Everything else redirects to <code>/ai</code>. <b>$0&ndash;$1K/month never "
     "qualifies, no matter how motivated.</b> The follower-count question and the "
     "“what describes you” question are <b>not used in the routing at all</b> — "
     "they are segmentation for the closer, and for the ad account.",
     "VERIFIED · logic read from the public JS bundle AND confirmed live: "
     "answering 0&ndash;1K followers / all-in / student / $0&ndash;1K redirected to /ai"),
    ("b_proof", X[3] + 15, 1150, "yes", "Proof is injected mid-survey, before the money question",
     "Between question 2 and question 3 the survey stops and shows three income "
     "screenshots: <b>Alfonso $14,000 in 1 month at 172 followers</b>, "
     "<b>Richard Lin $17,000 in 1 month</b>, <b>Thomas Tran $40,000+ in one "
     "month</b>. Then it asks how much you earn. They anchor first and measure "
     "second.",
     "VERIFIED · testimonial array in the same JS bundle, "
     "events <code>survey_testimonials_viewed</code> / <code>_continued</code>"),
    ("b_progress", X[2] + 15, 1150, "yes", "The progress bar never starts at zero",
     "Step values are hard-coded <code>[67, 74, 82, 88, 92, 96, 100]</code>. "
     "You land on the thank-you page already “67% done”, and the last four "
     "questions move you only 12 points. Endowed progress, applied to a survey "
     "the prospect never agreed to take.",
     "VERIFIED · array <code>g=[67,74,82,88,92,96,100]</code>"),
    ("b_dq", X[5] + 15, 2270, "dq", "Failing the gate is a product, not a dead end",
     "The DQ path does not go to a nurture sequence. It goes to a checkout. "
     "<b>ContentHooks at $20, $97 or $247 per month</b>, positioned as the free "
     "bonus they were promised for registering. The broke half of the list "
     "becomes MRR.",
     "VERIFIED · <code>/ai</code> pricing block, three tiers, “Cancel anytime”"),
    ("b_noreplay", X[2] + 15, 2270, "no", "No replay, stated on the page",
     "FAQ: <i>“There will be NO replays, so try your best to make it — we'll be "
     "giving away bonus free tools/assets for everyone who watches live.”</i> "
     "The scarcity is the show-rate mechanism, and it is backed by a real fixed "
     "date rather than an evergreen timer.",
     "VERIFIED · FAQ copy + countdown resolves to a real fixed datetime"),
    ("b_class", X[3] + 15, 2270, "unver", "The class itself was never seen",
     "Registration requires a <b>phone number</b>, and no research number exists "
     "— so the opt-in was never submitted. The live room, the deck, the pitch, "
     "the price and the whole email/SMS sequence are unobserved. Everything "
     "above is pre-registration evidence only.",
     "MISSING · hard rule: never type a fabricated phone number"),
]


def branch_card(b):
    bid, x, y, state, cond, body, ev = b
    cls = "br " + ("unver" if ev.startswith(("UNVERIFIED", "MISSING")) else state)
    return (f'<div class="{cls}" style="left:{x}px;top:{y}px">'
            f'<span class="cond">{cond}</span><p>{body}</p>'
            f'<span class="ev">{ev}</span></div>')


A = []
CLASS, DIRECT, QUAL, DQ = "#818cf8", "#34d399", "#22d3ee", "#fb923c"
LANE_COL = {"class": CLASS, "direct": DIRECT, "qual": QUAL, "dq": DQ}


def b64(rel):
    p = os.path.join(SHOTS_SRC, "mino_" + os.path.basename(rel).replace(".jpg", "") + ".jpg")
    with open(p, "rb") as fh:
        return "data:image/jpeg;base64," + base64.b64encode(fh.read()).decode()


def node_box(nid):
    if nid in SHOTS:
        asset, col, y = SHOTS[nid][0], SHOTS[nid][1], SHOTS[nid][2]
        return X[col], y, CARD_W, DIMS["assets/%s.jpg" % asset][1] + CHROME
    col, y, h = DATA[nid][0], DATA[nid][1], DATA[nid][2]
    return X[col], y, CARD_W, h


def right(n):
    x, y, w, h = node_box(n); return (x + w, y + h / 2)


def left(n):
    x, y, w, h = node_box(n); return (x, y + h / 2)


def bottom(n):
    x, y, w, h = node_box(n); return (x + w / 2, y + h)


def top(n):
    x, y, w, h = node_box(n); return (x + w / 2, y)


def h_arrow(a, b, col=CLASS, label=None):
    (x1, y1), (x2, y2) = right(a), left(b)
    mx = (x1 + x2) / 2
    A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
              % (x1 + 6, y1, mx, y1, mx, y2, x2 - 13, y2),
              col, False, label, ((x1 + x2) / 2, min(y1, y2) - 16)))


def v_arrow(a, b, col=DIRECT, label=None):
    (x1, y1), (x2, y2) = bottom(a), top(b)
    my = (y1 + y2) / 2
    A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
              % (x1, y1 + 6, x1, my, x2, my, x2, y2 - 13),
              col, False, label, ((x1 + x2) / 2, (y1 + y2) / 2 - 12)))


# ------- LANE 1: the free class. The survey is the whole mechanism.
h_arrow("ads", "reg", CLASS, "paid traffic · ?el=ad")
h_arrow("reg", "ty", CLASS, "phone REQUIRED")
h_arrow("ty", "survey", CLASS, "“unlock the free AI”")
h_arrow("survey", "call", QUAL, "money × urgency PASS")
h_arrow("call", "cal", QUAL)
v_arrow("survey", "ai", DQ, "FAIL → sold a $20–247/mo SaaS")

# ------- LANE 2: the direct call funnel, same brand, no class in between.
h_arrow("vsl", "root", DIRECT, "9:51 VSL sits on this page")
h_arrow("root", "hooks", DIRECT)
h_arrow("hooks", "main", DIRECT)
h_arrow("main", "proof", DIRECT)
h_arrow("proof", "offer", DIRECT, "call → price revealed")

# The one real join between the lanes: qualified survey traffic lands on the
# byte-identical page cold traffic gets.
_cx, _cy = bottom("call")
_rx, _ry = top("root")
A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
          % (_cx, _cy + 6, _cx, 1400, _rx, 1400, _rx, _ry - 13),
          QUAL, False, "same page, byte for byte", (_rx + 190, 1380)))


def drop(nid, bx, by, col):
    """A soft dotted line from a funnel card down to its routing-logic card."""
    x, y, w, h = node_box(nid)
    sx, sy = x + w / 2, y + h
    A.append(("M%.1f %.1f C%.1f %.1f %.1f %.1f %.1f %.1f"
              % (sx, sy + 4, sx, (sy + by) / 2, bx + 150, (sy + by) / 2, bx + 150, by - 8),
              col, True, None, (0, 0)))


drop("survey", X[4] + 15, 1150, DQ)
drop("survey", X[3] + 15, 1150, CLASS)
drop("ty", X[2] + 15, 1150, CLASS)
drop("ai", X[5] + 15, 2270, DQ)
drop("root", X[2] + 15, 2270, CLASS)
drop("main", X[3] + 15, 2270, "#94a3b8")

BANDS = [
    (125, "1 · FREE LIVE CLASS — REGISTER, THEN GET SORTED BY MONEY BEFORE THE CLASS HAPPENS", CLASS),
    (1595, "2 · DIRECT CALL FUNNEL + BACK END — SAME SUBDOMAIN, SAME PIXEL, NO CLASS IN BETWEEN", DIRECT),
    (2245, "3 · ROUTING LOGIC — READ OUT OF THE JAVASCRIPT, NOT GUESSED", DQ),
]

LANE_TAG = {"class": "FREE CLASS", "direct": "CALL FUNNEL",
            "qual": "QUALIFIED", "dq": "DISQUALIFIED"}


def shot_card(nid):
    asset, col, y, lane, title, url, note = SHOTS[nid]
    a = "assets/%s.jpg" % asset
    w, h = DIMS[a]
    x, yy, cw, ch = node_box(nid)
    return (f'<a class="n {lane}" href="{url}" target="_blank" rel="noopener" '
            f'style="left:{x}px;top:{yy}px;width:{cw}px">'
            f'<div class="nh"><span class="tag">{LANE_TAG[lane]}</span>'
            f'<span class="go">open ↗</span></div>'
            f'<div class="nt">{title}</div><div class="nu">{url}</div>'
            f'<div class="ni" style="height:{h}px"><img src="{b64(a)}" alt=""></div>'
            f'<div class="nn">{note}</div></a>')


def data_card(nid):
    col, y, h, lane, kick, title, rows, foot = DATA[nid]
    x, yy, cw, ch = node_box(nid)
    rs = "".join(f'<div class="dr"><span>{k}</span><b>{v}</b></div>' for k, v in rows)
    return (f'<div class="n {lane}" style="left:{x}px;top:{yy}px;width:{cw}px;'
            f'height:{h}px">'
            f'<div class="nh"><span class="tag">{kick}</span></div>'
            f'<div class="nt">{title}</div><div class="drs">{rs}</div>'
            f'<div class="nn">{foot}</div></div>')


W, H = 2620, 2660
paths = "".join(
    (f'<path d="{d}" stroke="{c}" stroke-width="1.6" fill="none" stroke-dasharray="5 5" '
     f'opacity=".65"/>' if dashed else
     f'<path d="{d}" stroke="{c}" stroke-width="2.5" fill="none" marker-end="url(#a{c[1:]})"/>')
    + (f'<text class="alabel" x="{lx:.0f}" y="{ly:.0f}">{lab}</text>' if lab else "")
    for d, c, dashed, lab, (lx, ly) in A)
markers = "".join(
    f'<marker id="a{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
    f'markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>'
    for c in (CLASS, DIRECT, QUAL, DQ, "#94a3b8"))
bands = "".join(
    f'<div class="band" style="top:{y - 52}px"><span style="color:{c}">{t}</span></div>'
    for y, t, c in BANDS)
nodes = ("".join(shot_card(n) for n in SHOTS)
         + "".join(data_card(n) for n in DATA)
         + "".join(branch_card(b) for b in BRANCH))

tpl = open(os.path.join(HERE, "board_template.html")).read()
out = (tpl.replace("{{W}}", str(W)).replace("{{H}}", str(H))
          .replace("{{NODES}}", nodes).replace("{{BANDS}}", bands)
          .replace("{{MARKERS}}", markers).replace("{{PATHS}}", paths)
       )
open(os.path.join(HERE, "board.html"), "w").write(out)
print(f"board.html  {len(out)/1024:.0f} KB  ({len(SHOTS)} screenshots, "
      f"{len(DATA)} data cards, {len(BRANCH)} branch cards, {len(A)} wires)")
