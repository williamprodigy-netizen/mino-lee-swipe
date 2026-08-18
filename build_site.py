#!/usr/bin/env python3
"""Build the Mino Lee / Content Academy swipe site.

Run: python3 build_site.py
"""
import sys, os, glob
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/MINO_LEE_Swipe")
tx_vsl = sorted(glob.glob(os.path.join(PKG, "Transcript/transcript_vsl.md")))
tx_test = sorted(glob.glob(os.path.join(PKG, "Transcript/transcript_kayvon.md")))

CONFIG = {
    "SITE": "Content Academy — Mino Lee",
    "CREATOR": "Mino Lee Content Academy",
    "ADS_KEY": None,
    "FUNNEL_IDS": ["F122"],
    "CAPTURED": "6 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/MINO_LEE_Swipe",
    "BLURB": "A free live class where <b>registration is not the conversion event</b>. The "
             "thank-you page is. A five-question survey disguised as &ldquo;unlock your free "
             "AI tool&rdquo; sorts every registrant on income and urgency <i>before the class "
             "has happened</i>, auto-redirects the buyers to a booking page, and sells everyone "
             "else a <b>$20&ndash;$247/month SaaS</b>. The routing rule was read out of their "
             "JavaScript, not guessed. Vertical is personal-brand growth (0 &rarr; 10K "
             "followers), not UGC-for-brands.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("pages.html", "Funnel pages"),
        ("transcripts.html", "Transcripts"),
        ("videos.html", "Video library"),
        ("copybank.html", "Copy bank"),
    ],

    "STATS": [
        ("Program price", "never stated"),
        ("SaaS ladder", "$20 / $97 / $247 mo"),
        ("Survey questions", "5"),
        ("Questions that route", "2"),
        ("VSL", "9m 51s"),
        ("Funnel steps captured", "9"),
        ("Class itself", "not seen"),
        ("Captured", "6 Aug 2026"),
    ],

    "OFFER": [
        ("Product", "Content Academy &mdash; paid community for short-form creators"),
        ("Face / operator", "Mino Lee (@mino1ee, @minolee.mp4) &mdash; solo founder, "
                                "no agency behind him that the capture can find"),
        ("Big idea", "&ldquo;How to Build a Full-Time Creator Career in just 1 hour/day&rdquo;"),
        ("Class promise", "&ldquo;Your First 10,000 True Fans In 90 Days&rdquo;"),
        ("ICP", "beginners and 9-to-5ers with <b>0&ndash;10K followers</b> &mdash; but the "
                "survey only lets through people already earning <b>$1K+/month</b>"),
        ("Mechanism", "A 4-stage roadmap: post your first video &rarr; make it a habit "
                      "&rarr; micro-optimisation (hook, script, edit, tonality) &rarr; monetise"),
        ("Core reframe", "&ldquo;Content is a <b>skill</b> you train&rdquo; &mdash; not a "
                         "lottery, not an algorithm hack. He tells you to expect zero growth "
                         "on your first 30 videos."),
        ("Entry", "Free class. First name, last name, email and <b>phone &mdash; all required</b>"),
        ("Front-end", "<b>ContentHooks</b> SaaS at $20 / $97 / $247 per month, sold to the "
                      "people who fail the qualification survey"),
        ("Price", "<b>never stated anywhere</b> &mdash; not on a page, not in the VSL, not on "
                  "their Whop. Revealed on the call only."),
        ("Guarantee", '<span class="tag warn">not observed</span> &mdash; no guarantee appears '
                      'on any pre-call asset'),
        ("Backend", "iClosed &ldquo;Content Academy Demo Call&rdquo; &rarr; Whop community "
                    "(30,820 joined, 4.9 from 153 reviews)"),
        ("Class cadence", "Fixed weekly slot, Thursday 6:00 PM ET. Countdown resolves to a "
                          "<b>real</b> datetime, not an evergreen rolling timer."),
    ],

    "FINDINGS": [
        ("The thank-you page is the conversion event, not the opt-in",
         "There is no confirmation message, no calendar link, no &ldquo;check your email&rdquo; "
         "reassurance. The page says <i>&ldquo;URGENT! Friend, your spot is almost saved&hellip;&rdquo;</i> "
         "with a progress bar at <b>67%</b> and exactly one button. They manufacture an "
         "incomplete-task feeling on a task that was already complete, and spend it on getting "
         "the survey filled. Meta's <code>CompleteRegistration</code> fires here, not on the form."),
        ("The qualification rule is money x urgency, and it is sitting in public JavaScript",
         "From <code>survey/page-bf93c16709583769.js</code>: you get the call if "
         "<b>(priority = &ldquo;all-in ASAP&rdquo; OR &ldquo;top 3&rdquo;) AND income &ge; $5K/mo</b>, "
         "or if <b>income $1K&ndash;$5K AND priority = all-in</b>. Everything else redirects to "
         "<code>/ai</code>. <b>Someone earning $0&ndash;$1K/month never reaches a call, no matter "
         "how motivated they say they are.</b> Confirmed live: answering 0&ndash;1K followers / "
         "all-in / student / $0&ndash;1K bounced straight to the SaaS page."),
        ("Three of the five survey questions do not affect routing at all",
         "Follower count, &ldquo;what are you looking for help with&rdquo; and &ldquo;what best "
         "describes you&rdquo; are collected and fired to PostHog, but the branch expression only "
         "reads <code>priority</code> and <code>income</code>. The other three are closer prep and "
         "audience-building data. Worth noticing: they ask the <b>flattering</b> questions first "
         "and the money question last, after proof."),
        ("Proof is injected mid-survey, immediately before the income question",
         "Between question two and question three the survey stops and shows three income "
         "screenshots &mdash; <b>Alfonso $14,000 in one month at 172 followers</b>, "
         "<b>Richard Lin $17,000 in one month</b>, <b>Thomas Tran $40,000+ in one month</b>. "
         "Then it asks what you currently earn. They anchor the number before they measure it."),
        ("The consolation prize is a checkout",
         "The registration page promises &ldquo;free access to our Viral Hooks Writer &mdash; "
         "<b>$97 FREE</b>&rdquo; as a show-up bonus. Fail the survey and you land on "
         "<code>/ai</code>, which is a three-tier subscription page: <b>$20, $97 and $247 per "
         "month</b>. The people who cannot afford the program become recurring revenue instead of "
         "a nurture sequence."),
        ("Two funnels, one subdomain, one pixel - and they say so in their own code",
         "The source comment reads: <i>&ldquo;Pixel 829859546688723 &mdash; same pixel "
         "contentmba-web uses, one pixel across both funnels.&rdquo;</i> "
         "<code>start.contentacademy.io/class</code> is the class funnel; "
         "<code>start.contentacademy.io/</code> is a direct book-a-call page. The qualified "
         "thank-you page (<code>/class/call</code>) is <b>byte-identical</b> to the root page &mdash; "
         "one asset, two entry points."),
        ("The countdown is real, and so is the no-replay policy",
         "The FAQ states: <i>&ldquo;There will be NO replays, so try your best to make it &mdash; "
         "we'll be giving away bonus free tools/assets for everyone who watches live.&rdquo;</i> "
         "The timer resolves to a genuine fixed datetime (Thu 6:00 PM ET) rather than a rolling "
         "evergreen clock. Most competitors in this swipe file fake this. He does not."),
        ("Their proof is screenshots with dates on them, not typed claims",
         "The registration page carries a <b>Whop revenue screenshot</b> labelled "
         "<i>&ldquo;WHOP &middot; JAN 1&ndash;31, 2025 &middot; GROSS $101,698.55&rdquo;</i>, four "
         "account cards with follower counts (525K / 280K / 180K / 900K), and an aggregate "
         "&ldquo;2.6 BILLION VIEWS&rdquo; counter. Platform-named, date-stamped, exact to the cent. "
         "That is a harder proof format than a testimonial quote."),
        ("The VSL is a free download and it contains the whole pitch",
         "9m 51s, Wistia <code>g3is6j1p25</code>, exposed at 4K and 1080p with no token. Pulled "
         "with one <code>curl</code>. It names the mechanism, the four stages, five named students, "
         "the coach roster, and closes on &ldquo;book a demo call below&rdquo; &mdash; without ever "
         "naming a price."),
        ("The offer is a community with named coaches, not a course",
         "The VSL sells three coaches by name and by number: <b>Gabe</b> (monetisation, 0 &rarr; "
         "$100K/mo agency in a year), <b>Prosper</b> (3,000 &rarr; 370,000 followers in a year), "
         "<b>Sam</b> (1,000 &rarr; 100,000 followers in 30 days, trains UGC creators). The "
         "differentiator he leans on is live weekly calls with people who have done it, not "
         "recorded modules."),
        ("Numbers do not reconcile across their own assets",
         '<span class="tag warn">CAUTION</span> The registration page says <b>&ldquo;over 60 '
         'students&rdquo;</b> reached 10K. The VSL says he has <b>&ldquo;coached over 1,500 '
         'creators&rdquo;</b>. The ContentHooks page says <b>&ldquo;trusted by 10,000+ members&rdquo;</b> '
         'and Whop says <b>30,820 joined</b>. The follower figures also drift &mdash; the class page '
         'lists 525K/280K/180K/900K, the ContentHooks page lists 520K/280K/150K/900K for the same '
         'four accounts. Do not repeat any single one of these as a fact about their business.'),
        ("No ad-library coverage",
         '<span class="tag warn">GAP</span> Meta Ad Library returns 403 to this environment and '
         'gethookd has no brand record, so creative volume, spend and survival rate are unmeasured. '
         'The only paid-traffic evidence is the <code>?el=ad</code> parameter on the URL Will was '
         'served, plus three confirmed trackers.'),
        ("The class itself was never seen, and could not be",
         '<span class="tag bad">HARD LIMIT</span> The opt-in modal requires a <b>phone number</b>. '
         'No research phone number exists, and fabricating one routes a real sales call to a real '
         'stranger. So the opt-in was never submitted. The live room, the deck, the pitch, the '
         'price, the email sequence and the SMS sequence are all unobserved. Everything on this '
         'site is <b>pre-registration evidence only</b>.'),
    ],

    "FUNNEL": [
        ("Class registration", "start.contentacademy.io/class?el=ad",
         "Countdown to a real fixed datetime. Modal opt-in: first, last, email, "
         "<b>phone (required)</b>. Placeholder names are &ldquo;Alex&rdquo; / &ldquo;Hormozi&rdquo;."),
        ("Thank-you", "start.contentacademy.io/class/thank-you",
         "No confirmation, no calendar link. 67% progress bar, &ldquo;URGENT!&rdquo;, one CTA. "
         "<code>CompleteRegistration</code> fires here."),
        ("Survey (the real application)", "start.contentacademy.io/class/survey",
         "5 questions. Only <b>priority</b> and <b>income</b> route. Testimonial interstitial "
         "between Q2 and Q3."),
        ("QUALIFIED &rarr; call page", "start.contentacademy.io/class/call",
         '<span class="tag good">auto-redirect, 1.4s</span> 9 video testimonials, iClosed widget, '
         'no price'),
        ("UNQUALIFIED &rarr; SaaS", "start.contentacademy.io/ai",
         '<span class="tag bad">the &ldquo;free gift&rdquo; is a checkout</span> $20 / $97 / $247 '
         'per month, three tiers'),
        ("Direct call page (cold)", "start.contentacademy.io/",
         "Byte-identical to <code>/class/call</code>. Carries the 9m51s Wistia VSL."),
        ("Free hook library", "start.contentacademy.io/ai/hook-library",
         "Ungated utility page, copy-to-clipboard hooks. Top of the ContentHooks funnel."),
        ("Brand site", "contentacademy.io",
         "Framer build. 31:08 YouTube VSL, Whop link, 40+ reviews at 4.98."),
        ("Booking", "app.iclosed.io/e/contentacademy/content-academy-demo-call",
         '<span class="tag warn">not submitted</span> &mdash; &ldquo;Content Academy Demo Call&rdquo;, '
         'email + name. Stripe and Hotjar load on the widget.'),
    ],

    "TRANSCRIPT_GROUPS": [
        ("VSL — how to go from 0 to 10K followers (4 steps), 9m 51s", tx_vsl),
        ("Kayvon Jafarzadeh testimonial, 1m 27s", tx_test),
    ],

    "SLIDE_PAGES": [],
    "DECKS": [],

    "VIDEOS": [
        ("mino_vsl_0to10k_1080p.mp4", 591, "86 MB",
         "The 9m51s VSL that sits on the call page. Wistia <code>g3is6j1p25</code>, named "
         "&ldquo;how to go from 0 to 10k followers (4 steps)&rdquo;. Exposed at 4K and 1080p "
         "with no token."),
        ("kayvon_testimonial_1080p.mp4", 87, "37 MB",
         "Kayvon Jafarzadeh's testimonial. Wistia <code>7eabr7y8fa</code>. Vertical 1080&times;1920 "
         "&mdash; it is a repurposed IG Reel, not a shot testimonial."),
        ("YouTube 7EHqhKXjzzs (not downloaded)", 1868, "&mdash;",
         "&ldquo;how i grew 200K followers in 1 year (working 90 minutes a day)&rdquo;, 31:08, "
         "uploaded 24 Dec 2024. Embedded on contentacademy.io as the brand-site VSL."),
    ],

    "EMAIL_NOTE": "Nothing has arrived, and nothing will. The opt-in requires a phone number, so "
                  "the research identity never registered &mdash; see the hard limit on the "
                  "overview page. The email and SMS sequences are completely unobserved.",

    "ANALYSIS": """
<div class="note"><b>The one-line read.</b> They do not run a webinar funnel with a survey bolted
on. They run a <b>survey funnel with a webinar as the bait</b>. The class is what gets the opt-in;
the thank-you page is what does the selling; and the two questions that decide everything are
income and urgency. If the class never ran, the machine would still work.</div>

<h2 class="sec">The routing rule, in full</h2>
<p>Read directly out of <code>/_next/static/chunks/app/class/survey/page-bf93c16709583769.js</code>.
Variables renamed for readability, logic unchanged:</p>
<div class="tablewrap"><table>
<tr><th>Term</th><th>Definition</th></tr>
<tr><td><code>HIGH_INCOME</code></td><td>income = $5,000&ndash;$10,000/mo <b>or</b> $10,000+/mo</td></tr>
<tr><td><code>MID_INCOME</code></td><td>income = $1,000&ndash;$5,000/mo</td></tr>
<tr><td><code>ALL_IN</code></td><td>priority = &ldquo;I'm ready to go all-in ASAP&rdquo;</td></tr>
<tr><td><code>TOP_3</code></td><td>priority = &ldquo;Top 3 on my priority list&rdquo;</td></tr>
<tr><td><b>QUALIFIED</b></td><td><b>(ALL_IN or TOP_3) and HIGH_INCOME</b> &nbsp;&mdash;or&mdash;&nbsp;
<b>MID_INCOME and ALL_IN</b></td></tr>
<tr><td>Destination</td><td>QUALIFIED &rarr; <code>/class/call</code> &nbsp;&middot;&nbsp;
everyone else &rarr; <code>/ai</code></td></tr>
</table></div>
<p>Two consequences worth sitting with. First, <b>$0&ndash;$1,000/month is a hard disqualifier</b> &mdash;
the exact person their ad creative targets (&ldquo;busy 9to5ers &amp; students&rdquo;, &ldquo;complete
beginner&rdquo;, &ldquo;0 followers&rdquo;) cannot reach a call. Second, urgency alone never rescues you:
saying you are all-in with no income still routes to the SaaS. Money gates the call, urgency only
widens it.</p>

<h2 class="sec">The survey, question by question</h2>
<div class="tablewrap"><table>
<tr><th>#</th><th>Question</th><th>Options</th><th>Routes?</th></tr>
<tr><td>1</td><td>How many followers do you have across all platforms?</td>
<td>0&ndash;1K &middot; 1K&ndash;10K &middot; 10K&ndash;100K &middot; 100K&ndash;1M</td>
<td><span class="tag">no</span></td></tr>
<tr><td>&mdash;</td><td colspan="2"><i>Interstitial: three income screenshots ($14K, $17K, $40K)</i></td>
<td><span class="tag warn">anchor</span></td></tr>
<tr><td>2</td><td>What are you looking for help with MOST right now? <i>(multi)</i></td>
<td>Posting my first video &middot; Growing an existing brand &middot; Monetizing with UGC &middot;
Generating leads for my business</td><td><span class="tag">no</span></td></tr>
<tr><td>3</td><td>How much of a priority is growing your personal brand right now?</td>
<td>All-in ASAP &middot; Top 3 &middot; Want it, not a priority yet &middot; Just exploring</td>
<td><span class="tag good">YES</span></td></tr>
<tr><td>4</td><td>What best describes you? <i>(multi)</i></td>
<td>Student &middot; Employed 9&ndash;5 &middot; Self-employed / freelancer &middot; Business owner</td>
<td><span class="tag">no</span></td></tr>
<tr><td>5</td><td>How much income are you currently making per month?</td>
<td>$0&ndash;1K &middot; $1K&ndash;5K &middot; $5K&ndash;10K &middot; $10K+</td>
<td><span class="tag good">YES</span></td></tr>
</table></div>
<p>Progress bar values are hard-coded <code>[67, 74, 82, 88, 92, 96, 100]</code>. You arrive already
&ldquo;67% done&rdquo;, and the four questions after the first move you a combined 12 points. Endowed
progress, applied to a survey nobody agreed to take.</p>

<h2 class="sec">How the VSL is built</h2>
<div class="tablewrap"><table>
<tr><th>Time</th><th>Beat</th><th>What he is doing</th></tr>
<tr><td>00:00</td><td>Promise + credential</td><td>Names the four stages, then the origin number:
&ldquo;January 1st of 2024 I was stuck at 50K followers making just $500 a month&rdquo; &rarr; 410K
followers, $760,000 in 20 months</td></tr>
<tr><td>00:20</td><td>Niche-proofing</td><td>Rattles off 16 niches it has worked in &mdash; real estate,
guitar, rock climbing, Amazon FBA, golfing, Christianity. Pre-empts &ldquo;it won't work for
mine&rdquo; before it forms</td></tr>
<tr><td>00:52</td><td>Volume proof + soft CTA</td><td>&ldquo;1,500 creators coached&rdquo;, then Henry
&mdash; 17 years old, 32 days, 27 posts, 10K followers. First call to book, 90 seconds in</td></tr>
<tr><td>01:39</td><td>Step 1 &mdash; expectation reset</td><td><b>&ldquo;You should expect zero
growth.&rdquo;</b> He kills the hack-seeker on purpose, then reframes to consistency and
accountability</td></tr>
<tr><td>02:27</td><td>The why</td><td>&ldquo;Learning content is the best skill you can learn in
2025&rdquo; &mdash; positions it as a career skill, not a side hustle</td></tr>
<tr><td>03:20</td><td>Step 2 &mdash; habit</td><td>Names the social cost out loud: &ldquo;your peers
are going to think you're cringe&rdquo;. Jojo: 67 days straight &rarr; first 100K-view video</td></tr>
<tr><td>04:09</td><td>Step 3 &mdash; micro-optimisation</td><td>The actual mechanism: hook, scripting,
editing, tonality, visuals, 1% a day. Jojo 1K &rarr; 10K in 47 days on ~200 posts</td></tr>
<tr><td>05:47</td><td>Step 4 &mdash; monetise without a product</td><td>Andrew: zero UGC experience
&rarr; $4,000 in two weeks &rarr; $12K month, via brand partnerships in their Discord</td></tr>
<tr><td>06:33</td><td>Escalation</td><td>The same skill produces <b>job offers</b> &mdash; CMO roles at
$100K&ndash;$250K/yr. Contrasts against marketing graduates &ldquo;getting cooked by the job
market&rdquo;</td></tr>
<tr><td>07:20</td><td>The fork</td><td>&ldquo;Two options once you click off this video&rdquo; &mdash;
alone with &ldquo;lonely nights pushing against judgment&rdquo;, or the community</td></tr>
<tr><td>08:05</td><td>Offer</td><td>Three named coaches with numbers, live weekly calls,
&ldquo;secret tools and sauce used by the top 1% of creators&rdquo;. <b>No price.</b></td></tr>
<tr><td>09:30</td><td>Close</td><td>&ldquo;Are you going to partake in day one, or put it off for one
day?&rdquo;</td></tr>
</table></div>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Qualify on the thank-you page, not the call</h3><p>Ours qualifies at the
application and again on the phone. Theirs qualifies <b>immediately after the opt-in</b>, for free,
with zero setter time, using two questions. The output is a clean split before a human touches
anyone. Worth testing on the UGCW confirmation page as a soft segment, not a hard gate.</p></div>
<div class="card"><h3>Give the disqualified a product, not a nurture sequence</h3><p>Their DQ path
terminates in a $20/mo checkout. Ours terminates in AI-LNS. Both are fine, but they are monetising
the half of the list we only ever nurture. A cheap recurring product for the &ldquo;can't afford
it yet&rdquo; segment is the single most transferable idea here.</p></div>
<div class="card"><h3>Anchor with proof immediately before the money question</h3><p>Three income
screenshots, then &ldquo;how much do you make?&rdquo; The sequencing is the whole trick &mdash; it
reframes what a normal answer looks like at the exact moment they answer.</p></div>
<div class="card"><h3>Start the progress bar at 67%</h3><p>Endowed progress is old, but applying it
to a <i>post</i>-conversion survey is not. It converts a finished task into an unfinished one, and
buys a five-question form off a page that would otherwise be a dead end.</p></div>
<div class="card"><h3>Proof as dated screenshots, not quotes</h3><p>&ldquo;WHOP &middot; JAN 1&ndash;31,
2025 &middot; GROSS $101,698.55&rdquo; is a harder claim than any testimonial, because it names the
platform, the window and the cent. Check what our reg page leads with against that bar.</p></div>
<div class="card"><h3>Kill the hack-seeker in the first two minutes</h3><p>&ldquo;You should expect
zero growth&rdquo; on your first 30 videos is a deliberate filter inside a sales asset. It costs him
the tyre-kickers and buys credibility with the person who has already failed once.</p></div>
</div>

<h2 class="sec">Where they are weak</h2>
<div class="grid g2">
<div class="card"><h3>The qualification logic is public</h3><p>It ships unobfuscated in a client-side
bundle. Anyone can read the gate &mdash; and anyone who wants the call can simply claim $10K/month
and &ldquo;all-in&rdquo;. A self-reported income question with a client-side branch is an honesty
system protecting the closer's calendar.</p></div>
<div class="card"><h3>The ad promise and the gate contradict each other</h3><p>They buy
&ldquo;complete beginner&rdquo;, &ldquo;0 followers&rdquo;, &ldquo;busy 9to5ers &amp; students&rdquo;
&mdash; then hard-disqualify anyone under $1K/month. They are paying to acquire the exact person
their own funnel refuses to talk to. Whether the SaaS covers that CAC is the question their P&amp;L
turns on, and nothing here answers it.</p></div>
<div class="card"><h3>Their own numbers do not agree</h3><p>60 students vs 1,500 coached vs 10,000+
members vs 30,820 joined; 525K/280K/180K/900K on one page and 520K/280K/150K/900K on another for the
same accounts. Sloppy, and it is the kind of thing a skeptical prospect notices.</p></div>
<div class="card"><h3>The VSL is a free download</h3><p>Their entire pitch, ungated at 4K on Wistia,
with no token. It cost one <code>curl</code> to take.</p></div>
<div class="card"><h3>No guarantee anywhere</h3><p>No risk reversal appears on any pre-call asset,
against a price that is never named. Both may well be handled on the call &mdash; but there is
nothing on the page doing that work.</p></div>
</div>

<h2 class="sec">What is missing, and why</h2>
<p>The opt-in modal requires a <b>phone number</b> and no research number exists, so the form was
never submitted. That means the live class, the deck, the pitch, the price, the guarantee, the email
sequence and the SMS sequence are all <b>unobserved</b>. Everything on this site is pre-registration
evidence. Meta Ad Library returns 403 to this environment and gethookd carries no brand record, so
there is no creative volume, spend or survival data &mdash; do not infer any. The iClosed calendar
was captured but never booked.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
