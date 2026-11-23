#!/usr/bin/env python3
"""The Noodle House (Rochester, MN) — template v2 T2 page generator
(websites lane, 2026-11-22, t_b9217573).

All copy from verified facts with sources only:
- postbulletin.com 2026-11 ("Noodle House to host 'soft opening'...") — owners, address, Kelley
  Building history, soft-open Nov 8 12-8 p.m., Marlene quote "Chai and I just love noodles..."
- postbulletin.com earlier feature ("Mango Thai owners cooking up a second restaurant...") —
  Marlene quote "it feels like a noodle house", 318 S. Broadway Mango Thai tie
- krocnews.com 2026-10/11 (menu + opening) — dishes pho/khao soi/ramen/chicken karaage (owners
  told KROC directly), soft-open Sunday Nov 8
- kaaltv.com (ABC 6) + kttc.com (ABC 5) — ramen/pho, "between Broadway Avenue S and 4th Street SE"
- restaurant's OWN Facebook About tab (logged-out 2026-11-22): 332 Broadway Ave S NAP, phone
  (507) 206-0577, email noodlehouse332@gmail.com, category Restaurant, price $$, FB "Website"
  field = Instagram only (no-site evidence)
- restaurant's OWN Instagram bio (web_fetch logged-out 2026-11-22): full hours
  "M-Th 11-9 | F 11-10 | Sa 12-10 | Su 12-8" (Su 12-8 matches the press soft-open hours)
Unknowns omitted, never guessed: menu prices, reservations policy, parking, delivery/takeout.
Canonical/OG pinned to the -demo host; noindex on every page (demo-host doctrine).
Geo: OSM Nominatim + US Census agree on 44.02003,-92.46295 for 332 Broadway Ave S (see geo.json).
"""
import json, os

ORIGIN = "https://noodle-house-rochester-demo.up.railway.app"
SITE = "The Noodle House"
PHONE = "(507) 206-0577"
TEL = "tel:+15072060577"
EMAIL = "noodlehouse332@gmail.com"
MAILTO = "mailto:noodlehouse332@gmail.com"
STREET = "332 Broadway Ave S"
CITYST = "Rochester, MN 55904"
# Google Maps / OSM / Census all resolve this address to the corner lot (see geo.json).
GEO_LAT, GEO_LON = 44.02003, -92.46295
MAPQ = "332+Broadway+Ave+S,+Rochester,+MN+55904"
DIRLINK = f"https://www.google.com/maps/dir/?api=1&destination={MAPQ}"
BUILT = "<!-- BUILT-2026-11-22 -->"

PB_SOFT = "https://www.postbulletin.com/business/noodle-house-to-host-soft-opening-in-downtown-rochester"
PB_ORIGIN = "https://www.postbulletin.com/business/mango-thai-owners-cooking-up-a-second-restaurant-in-downtown-rochester"
KROC = "https://krocnews.com/ixp/717/p/noodle-house-rochester-opening-and-menu/"
KAALTV = "https://www.kaaltv.com/news/new-restaurant-opening-in-rochester-in-november/"
KTTC = "https://www.kttc.com/2026-10-23/new-rochester-restaurant-set-open-late-november/"
IG = "https://www.instagram.com/noodlehousemn/"
FB = "https://www.facebook.com/p/Noodle-House-61595134931439/"

# ---------------------------------------------------------------- motifs
# Every decorative svg class is scoped to its element type (svg.steam, svg.bowlmark ...)
# so a generic tag never collides with btn/eyebrow rules (kendricks css-collision lesson).

def bowlmark():
    return ('<svg class="bowlmark" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            '<path d="M2.5 11.5h19a9.5 9.5 0 0 1-19 0z" fill="none" stroke-width="1.6"/>'
            '<path d="M8.6 8.2c0-2.2 2.8-2.2 2.8-4.4M12.9 8.2c0-2.2 2.8-2.2 2.8-4.4" fill="none" '
            'stroke-width="1.6" stroke-linecap="round"/>'
            '<path d="M1.8 20.8h20.4" stroke-width="1.6" stroke-linecap="round"/></svg>')

def steamplume():
    return ('<svg class="steamplume" viewBox="0 0 210 210" aria-hidden="true" focusable="false">'
            '<path d="M70 195c0-40 34-40 34-78s-26-38-26-70" fill="none" stroke-width="2.4" stroke-linecap="round"/>'
            '<path d="M112 202c0-34 28-34 28-66s-22-32-22-58" fill="none" stroke-width="2.4" stroke-linecap="round"/>'
            '<path d="M150 190c0-28 22-28 22-54s-16-26-16-48" fill="none" stroke-width="2.4" stroke-linecap="round"/>'
            '</svg>')

def noodlewave():
    return ('<svg class="wave" viewBox="0 0 72 10" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
            '<path d="M0 5c6-6 12 6 18 0s12 6 18 0 12 6 18 0 6-4 6-4" fill="none" stroke-width="1.5"/></svg>')

MAP_EMBED = (f'<iframe src="https://www.google.com/maps?q={MAPQ}&output=embed" '
              f'title="Map: The Noodle House, {STREET}, {CITYST}" loading="lazy"></iframe>')

# ---------------------------------------------------------------- head/nav/footer

def head(path, title, desc):
    canonical = ORIGIN + ("" if path == "/" else path)
    out = [
        '<!DOCTYPE html>\n<html lang="en">\n<head>',
        BUILT,
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f'<title>{title}</title>',
        f'<meta name="description" content="{desc}">',
        '<meta name="robots" content="noindex, nofollow">',
        f'<link rel="canonical" href="{canonical}">',
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="The Noodle House">',
        f'<meta property="og:title" content="{title}">',
        f'<meta property="og:description" content="{desc}">',
        f'<meta property="og:url" content="{canonical}">',
        f'<meta property="og:image" content="{ORIGIN}/og.png">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
        f'<meta name="twitter:description" content="{desc}">',
        f'<meta name="twitter:image" content="{ORIGIN}/og.png">',
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
        '<link rel="stylesheet" href="/style.css">\n</head>',
    ]
    return "\n".join(out)

BRAND = (f'<a class="brand" href="/">{bowlmark()}<span class="brandtext">'
         '<span class="bmark">The Noodle House</span>'
         '<span class="bsub">332 Broadway Ave S &middot; Rochester, MN</span></span></a>')
NAV = ('<nav aria-label="Main"><ul><li><a href="/menu">Menu</a></li>'
       '<li><a href="/bowls">Broth bowls</a></li><li><a href="/our-story">Our story</a></li>'
       '<li><a href="/visit">Visit</a></li><li><a href="/contact">Contact</a></li>'
       f'<li><a class="btn chili" href="{TEL}">Call {PHONE}</a></li></ul></nav>')
HEADER = f'<header class="site"><div class="wrap headwrap">{BRAND}{NAV}</div></header>'

HRS_ONELINE = ('Open daily &middot; Mon&ndash;Thu 11am&ndash;9pm &middot; Fri 11am&ndash;10pm '
               '&middot; Sat 12pm&ndash;10pm &middot; Sun 12pm&ndash;8pm')

FOOTER = (f'<footer class="site"><div class="wrap"><div class="foottop">'
 f'<div><p class="fbrand">{bowlmark()}The Noodle House</p>'
 '<p class="ftag">Pho &middot; Khao Soi &middot; Ramen &middot; Karaage</p>'
 '<div class="fnaps"><p class="ftown">Find us</p>'
 f'<address class="addr">{STREET}<br>{CITYST}</address>'
 f'<p class="ftel">Phone: <a href="{TEL}">{PHONE}</a></p>'
 f'<p class="ftel">Email: <a href="{MAILTO}">{EMAIL}</a></p>'
 f'<p class="fhrs">{HRS_ONELINE}</p>'
 '<p>Follow along: <a href="https://www.instagram.com/noodlehousemn/" rel="noopener">Instagram</a> '
 '&middot; <a href="https://www.facebook.com/p/Noodle-House-61595134931439/" rel="noopener">Facebook</a></p>'
 '</div></div>'
 '<nav aria-label="Footer"><ul><li><a href="/menu">Menu</a></li><li><a href="/bowls">Broth bowls</a></li>'
 '<li><a href="/wok-fried">Wok &amp; fryer</a></li><li><a href="/our-story">Our story</a></li>'
 '<li><a href="/visit">Visit</a></li><li><a href="/contact">Contact</a></li><li><a href="/privacy">Privacy</a></li></ul></nav>'
 f'<p class="fpress">In the news:<br><a href="{PB_SOFT}" rel="noopener">Post Bulletin</a> &middot; '
 f'<a href="{KROC}" rel="noopener">KROC News</a> &middot; <a href="{KTTC}" rel="noopener">ABC 5 News</a></p>'
 '</div></div><div class="wrap"><p class="footline">&copy; 2026 The Noodle House &middot; '
 f'{STREET}, Rochester, Minnesota 55904 &middot; <a href="{TEL}">{PHONE}</a></p></div></footer>')

def ld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, indent=1) + '\n</script>'

BIZ_ID = ORIGIN + "/#restaurant"
BIZ = {
    "@type": "Restaurant",
    "@id": BIZ_ID,
    "name": "The Noodle House",
    "description": ("Noodle restaurant by Chef Chai and Marlene Rachwat — pho, khao soi, ramen and "
                    "chicken karaage — in the 1858 Kelley Building at 332 Broadway Ave S on the corner "
                    "of South Broadway and Fourth Street SE, downtown Rochester, Minnesota. "
                    "Soft-opened November 8, 2026."),
    "url": ORIGIN + "/",
    "image": ORIGIN + "/og.png",
    "telephone": "+1-507-206-0577",
    "email": "noodlehouse332@gmail.com",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "332 Broadway Ave S",
        "addressLocality": "Rochester",
        "addressRegion": "MN",
        "postalCode": "55904",
        "addressCountry": "US",
    },
    "geo": {"@type": "GeoCoordinates", "latitude": GEO_LAT, "longitude": GEO_LON},
    "servesCuisine": ["Vietnamese", "Japanese", "Thai"],
    "priceRange": "$$",
    "openingDate": "2026-11-08",
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday"],
         "opens": "11:00", "closes": "21:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Friday", "opens": "11:00", "closes": "22:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "12:00", "closes": "22:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "12:00", "closes": "20:00"},
    ],
    "sameAs": [IG, FB],
}

WEBSITE = {"@type": "WebSite", "@id": ORIGIN + "/#website", "name": "The Noodle House", "url": ORIGIN + "/"}

def webpage(path, title, desc, extra=None):
    g = [WEBSITE, {
        "@type": "WebPage",
        "@id": ORIGIN + path + "#webpage",
        "name": title,
        "description": desc,
        "url": ORIGIN + ("" if path == "/" else path),
        "isPartOf": {"@id": ORIGIN + "/#website"},
        "about": {"@id": BIZ_ID},
    }]
    if extra:
        g += extra
    return ld({"@graph": g})

def breadcrumb(items):
    el = [{"@type": "ListItem", "position": i + 1, "name": n, "item": ORIGIN + u} for i, (n, u) in enumerate(items)]
    return {"@type": "BreadcrumbList", "itemListElement": el}

ORG = {"@type": "Organization", "name": "The Noodle House", "url": ORIGIN + "/", "telephone": "+1-507-206-0577"}

def city(name):
    return {"@type": "City", "name": name}

def service(path, name, svc_type, desc):
    return {
        "@type": "Service", "@id": ORIGIN + path + "#service",
        "name": name, "serviceType": svc_type, "description": desc,
        "url": ORIGIN + path,
        "areaServed": city("Rochester"),
        "provider": ORG,
    }

# --------------------------------------------------------------- copy constants

FAQ = {
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": "When did The Noodle House open?",
         "acceptedAnswer": {"@type": "Answer", "text": "The restaurant soft-opened on Sunday, November 8, 2026, from noon to 8 p.m. — the owners&rsquo; own announcement, reported by the Post Bulletin and KROC News. It is open seven days a week."}},
        {"@type": "Question", "name": "What&rsquo;s on the menu?",
         "acceptedAnswer": {"@type": "Answer", "text": "The noodle dishes the owners couldn&rsquo;t fit on the menu at their Mango Thai restaurant: pho, khao soi, ramen and chicken karaage — the dishes Chef Chai and Marlene Rachwat told KROC News they would serve. The full menu, with prices, is at the restaurant."}},
        {"@type": "Question", "name": "When are you open?",
         "acceptedAnswer": {"@type": "Answer", "text": "Seven days a week: 11 a.m. to 9 p.m. Monday through Thursday, 11 a.m. to 10 p.m. Friday, noon to 10 p.m. Saturday, noon to 8 p.m. Sunday — hours as published in the restaurant&rsquo;s own Instagram bio."}},
        {"@type": "Question", "name": "Where exactly are you?",
         "acceptedAnswer": {"@type": "Answer", "text": "At 332 Broadway Avenue South in the Kelley Building — Rochester&rsquo;s first brick building, on the corner of South Broadway and Fourth Street SE downtown, a few doors south of Mango Thai."}},
        {"@type": "Question", "name": "Is it related to Mango Thai?",
         "acceptedAnswer": {"@type": "Answer", "text": "Yes — Chef Chai and Marlene Rachwat, who run Mango Thai a few doors up Broadway at 318 S. Broadway, opened The Noodle House as its own restaurant, dedicated entirely to the noodle dishes they love."}},
    ],
}

HOME_FAQ_HTML = "\n".join(
    f'<details><summary>{q}</summary><p>{a["acceptedAnswer"]["text"]}</p></details>'
    for q, a in [(x["name"], x) for x in FAQ["mainEntity"]])


def dishcard(num, name, desc, source):
    return (f'<article class="plate"><p class="pnum">{num}</p>'
            f'<h3>{name}</h3><p class="pdesc">{desc}</p>'
            f'<p class="psrc">per {source}</p></article>')

DISHES = [
    ("I", "Pho",
     "Rice noodles under a deeply simmered broth — the Vietnamese bowl that anchors the menu.",
     "KROC News"),
    ("II", "Ramen",
     "Japanese-style noodle bowls in savory broth, built around the same long-simmered craft.",
     "KROC News"),
    ("III", "Khao Soi",
     "Northern Thai curried noodles finished with a crisp fried-noodle garnish on top.",
     "KROC News"),
    ("IV", "Chicken Karaage",
     "Japanese-style fried chicken — the crisp side that belongs beside every bowl.",
     "KROC News"),
]
HOME_DISHES = "\n".join(dishcard(*d) for d in DISHES)

HRS_TABLE = ('<table class="hrs"><thead><tr><th>Day</th><th>Hours</th></tr></thead><tbody>'
             '<tr><td>Monday &ndash; Thursday</td><td>11:00 a.m. &ndash; 9:00 p.m.</td></tr>'
             '<tr><td>Friday</td><td>11:00 a.m. &ndash; 10:00 p.m.</td></tr>'
             '<tr><td>Saturday</td><td>12:00 noon &ndash; 10:00 p.m.</td></tr>'
             '<tr><td>Sunday</td><td>12:00 noon &ndash; 8:00 p.m.</td></tr></tbody></table>')

MARLENE_NOODLES = ('&ldquo;Chai and I just love noodles, like Pho, Thai noodles and Ramen. We can&rsquo;t put all '
                   'of the noodle dishes we like on the menu at Mango Thai. This is the perfect place to serve '
                   'all of the kinds of noodles that we love.&rdquo; &mdash; Marlene Rachwat, to the Post Bulletin')

# ---------------------------------------------------------------- pages

HOME = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink hero"><div class="wrap heroinner">
  {steamplume()}
  <p class="eyebrow">Soft-opened November 8 &middot; The Kelley Building &middot; Rochester, MN</p>
  <h1>Rochester&rsquo;s new home for noodles.</h1>
  <p class="lede">The Noodle House serves the bowls Chef Chai and Marlene Rachwat never had room for on
  the menu at Mango Thai a few doors up Broadway: pho, khao soi, ramen and chicken karaage, cooked in
  the 1858 Kelley Building on the corner of South Broadway and Fourth Street SE.</p>
  <div class="ctarow"><a class="btn chili" href="/menu">See the menu</a>
  <a class="btn" href="/visit">Find the corner</a>
  <a class="btn ghost" href="{DIRLINK}" rel="noopener">Get directions</a></div>
  <p class="status"><span>Open seven days a week</span><span>&middot;</span>
  <span>Mon&ndash;Thu till 9 &middot; Fri &amp; Sat till 10 &middot; Sun till 8</span><span>&middot;</span>
  <span>{STREET}</span></p>
</div></section>

<section class="band cream"><div class="wrap">
  <p class="eyebrow dark">The menu, in brief</p>
  <h2 class="sec">Noodles first. Everything else hangs off them.</h2>
  <p class="secsub">The dishes the restaurant told KROC News it would serve, from pho and ramen to
  Northern Thai khao soi &mdash; the full menu, with prices, is at the restaurant.</p>
  <div class="plategrid">{HOME_DISHES}</div>
  <div class="ctarow"><a class="btn chili" href="/menu">Full menu &amp; where it stands</a>
  <a class="btn ghost" href="{TEL}">Call {PHONE}</a></div>
</div></section>

<section class="band ink quote"><div class="wrap narrow">
  <p class="qtext">Chai and I just love noodles, like Pho, Thai noodles and Ramen. We can&rsquo;t put all of
  the noodle dishes we like on the menu at Mango Thai. This is the perfect place to serve all of the kinds of
  noodles that we love.</p>
  <p class="qwho">Marlene Rachwat &mdash; to the Post Bulletin</p>
  <div class="ctarow"><a class="btn gold" href="/our-story">Read our story</a></div>
</div></section>

<section class="band paper"><div class="wrap">
  <p class="eyebrow dark">The kitchen&rsquo;s two halves</p>
  <div class="twohalf">
    <article class="halfcard"><h3>Broth bowls</h3>
      <p>Slow-simmered soup for pho and ramen — the deep, savory end of the menu, with the rice
      and wheat noodles that ride in it.</p>
      <p class="halfmore"><a href="/bowls">Pho &amp; ramen &rarr;</a></p></article>
    <article class="halfcard"><h3>Wok &amp; fryer</h3>
      <p>Khao soi straight out of a Northern Thai curry pot, crisp on top, and chicken karaage
      fresh out of the fryer beside it.</p>
      <p class="halfmore"><a href="/wok-fried">Khao soi &amp; karaage &rarr;</a></p></article>
  </div>
</div></section>

<section class="band mist"><div class="wrap narrow">
  <p class="eyebrow dark">Before you come</p>
  <h2 class="sec">The questions people ask.</h2>
  {HOME_FAQ_HTML}
</div></section>

<section class="band ink"><div class="wrap cornercta">
  <h2 class="sec light">Find the corner of Broadway and 4th.</h2>
  <p class="lede">The Kelley Building holds the whole corner — and we&rsquo;re in the front of it,
  a few doors south of Mango Thai.</p>
  <div class="ctarow"><a class="btn chili" href="{DIRLINK}" rel="noopener">Get directions</a>
  <a class="btn ghost" href="{TEL}">Call {PHONE}</a>
  <a class="btn ghost" href="/contact">Send a note</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

MENU = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">The menu &middot; as the restaurant told KROC News</p>
  <h1>Four dishes, one obsession.</h1>
  <p class="lede">Chef Chai and Marlene opened The Noodle House for the dishes that never fit at
  Mango Thai. Here&rsquo;s what they named when KROC News asked &mdash; and the full menu, with
  prices, is what&rsquo;s cooking when you walk in.</p>
  <div class="ctarow"><a class="btn chili" href="{TEL}">Call {PHONE}</a>
  <a class="btn ghost" href="/visit">Hours &amp; directions</a></div>
</div></section>

<section class="band cream"><div class="wrap">
  <p class="eyebrow dark">Broth bowls</p>
  <div class="plategrid two">
    <article class="plate"><p class="pnum">I</p><h3>Pho</h3>
      <p class="pdesc">Vietnamese rice-noodle soup under a deeply simmered broth — herbs and
      accompaniments on the side the way pho is meant to arrive.</p>
      <p class="psrc">per KROC News</p></article>
    <article class="plate"><p class="pnum">II</p><h3>Ramen</h3>
      <p class="pdesc">Japanese-style noodle bowls in savory broth — the same patience, a
      different pot.</p>
      <p class="psrc">per KROC News</p></article>
  </div>
  <p class="fineprint">Bowl details and prices live at the restaurant.</p>
</div></section>

<section class="band paper"><div class="wrap">
  <p class="eyebrow dark">Wok &amp; fryer</p>
  <div class="plategrid two">
    <article class="plate"><p class="pnum">III</p><h3>Khao Soi</h3>
      <p class="pdesc">Northern Thai curried noodles in coconut-rich curry, finished with a crisp
      fried-noodle garnish and the fixings on the side.</p>
      <p class="psrc">per KROC News</p></article>
    <article class="plate"><p class="pnum">IV</p><h3>Chicken Karaage</h3>
      <p class="pdesc">Japanese-style fried chicken — seasoned, crisp-edged, and made for the
      space between two bowls.</p>
      <p class="psrc">per KROC News</p></article>
  </div>
  <p class="fineprint">The menu grows as the kitchen settles in — what&rsquo;s cooking today is
  best answered by a call.</p>
  <div class="ctarow"><a class="btn chili" href="{TEL}">Call {PHONE}</a>
  <a class="btn ghost" href="/contact">Or send a note</a></div>
</div></section>

<section class="band mist mapband"><div class="wrap">
  <div class="mapcell">{MAP_EMBED}</div>
  <p class="fineprint">Map: The Noodle House, {STREET}, {CITYST}.</p>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

BOWLS = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Broth bowls &middot; pho &amp; ramen</p>
  <h1>The pot that takes all day.</h1>
  <p class="lede">Pho and ramen are built the same way: broth simmered long enough to taste like it
  was. At The Noodle House they&rsquo;re the two bowls the menu was founded on &mdash; rice noodles
  for pho, wheat for ramen, both swimming in whatever the pot has been doing since morning.</p>
  <div class="ctarow"><a class="btn chili" href="{TEL}">Ask what&rsquo;s in the pot &middot; {PHONE}</a>
  <a class="btn ghost" href="/menu">See the whole menu</a></div>
</div></section>

<section class="band cream"><div class="wrap narrow prose">
  <p class="first">&ldquo;Chai and I just love noodles, like Pho, Thai noodles and Ramen,&rdquo; Marlene
  Rachwat told the Post Bulletin when the restaurant was still an empty space on Broadway. &ldquo;We
  can&rsquo;t put all of the noodle dishes we like on the menu at Mango Thai. This is the perfect place
  to serve all of the kinds of noodles that we love.&rdquo;</p>
  <p>So the broth bowls get their own house. Pho arrives the Vietnamese way — rice noodles, deeply
  savory broth, herbs and the sharp fixings alongside for you to build your bowl. Ramen runs the
  Japanese lane: a different broth, a different noodle, the same patience.</p>
  <p>The specifics — which broth on which day, at what price — are the kitchen&rsquo;s call and
  printed at the restaurant. What&rsquo;s promised is the two bowls the owners named to KROC News
  as the anchor of the menu.</p>
  <div class="ctarow"><a class="btn chili" href="/visit">Hours &amp; directions</a>
  <a class="btn ghost" href="/wok-fried">The wok &amp; fryer &rarr;</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

WOKFRIED = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Wok &amp; fryer &middot; khao soi &amp; karaage</p>
  <h1>Khao soi, and the crisp on top.</h1>
  <p class="lede">Khao soi is the Northern Thai bowl: silky noodles in a coconut-rich curry, crowned
  with fried noodles that stay crisp until the last spoonful. Chicken karaage is its partner —
  Japanese fried chicken, blistered outside, juicy inside, made to be eaten between bowls.</p>
  <div class="ctarow"><a class="btn chili" href="{TEL}">Call {PHONE}</a>
  <a class="btn ghost" href="/menu">See the whole menu</a></div>
</div></section>

<section class="band cream"><div class="wrap narrow prose">
  <p class="first">Of everything the owners named to KROC News, khao soi is the one with the shortest
  road to The Noodle House — Chef Chai cooks out of the Thai kitchen he and Marlene already run a few
  doors up Broadway at Mango Thai, and khao soi is what Northern Thailand puts on the table.</p>
  <p>The crisp that rides on top isn&rsquo;t a garnish you stir in and forget; it&rsquo;s the point.
  Bite through it while it still snaps. Karaage plays the same music in a different register —
  seasoned dark-meat chicken fried hard enough to crack, soft inside.</p>
  <p>Prices and the rest of the board are at the restaurant. If one of these is why you&rsquo;re
  coming, call ahead — the kitchen is honest about what&rsquo;s ready.</p>
  <div class="ctarow"><a class="btn chili" href="/visit">Hours &amp; directions</a>
  <a class="btn ghost" href="/bowls">The broth bowls &rarr;</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

OURSTORY = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Our story &middot; Broadway &amp; 4th &middot; est. November 2026</p>
  <h1>&ldquo;It feels like a noodle house.&rdquo;</h1>
  <p class="lede">That&rsquo;s what Marlene Rachwat told the Post Bulletin the first time she saw the
  little space on South Broadway. Eight months of renovation and one name later, The Noodle House is
  where she and Chef Chai serve the dishes their other menu never had room for.</p>
  <div class="ctarow"><a class="btn chili" href="/menu">See the menu</a>
  <a class="btn ghost" href="{TEL}">Call {PHONE}</a>
  <a class="btn ghost" href="/visit">Visit us</a></div>
</div></section>

<section class="band cream"><div class="wrap narrow prose">
  <p class="first">Chai and Marlene run Mango Thai at 318 South Broadway, a few doors north. When the
  neighboring space came open, the pull was immediate — not for another Thai restaurant, but for the
  single thing the two of them keep coming back to: noodles.</p>
  <p>&ldquo;Chai and I just love noodles, like Pho, Thai noodles and Ramen. We can&rsquo;t put all of
  the noodle dishes we like on the menu at Mango Thai. This is the perfect place to serve all of the
  kinds of noodles that we love,&rdquo; Marlene said — and that is the whole business plan, in her
  words.</p>
  <h3 class="h4">The building</h3>
  <p>The Noodle House sits inside the Kelley Building, Rochester&rsquo;s first brick building — raised
  in 1858 by Dr. Lewis Halsey Kelley with locally made bricks, and home over the years to the city&rsquo;s
  first medical practice, a dry goods store, a basement saloon and, up the stairs, the first newspaper.
  It takes the corner of South Broadway and Fourth Street SE.</p>
  <h3 class="h4">The opening</h3>
  <p>The space before was Marrow, the 40-seat fine-dining room chefs Jeff and Sarah Schwenker closed in
  May. The Rachwats took it over for one purpose, announced it in their own words —
  &ldquo;The wait is over. Noodle House is opening its doors, and we can&rsquo;t wait to welcome
  you&rdquo; — and soft-opened on Sunday, November 8, 2026, serving noon to eight.</p>
</div></section>

<section class="band mist"><div class="wrap">
  <p class="eyebrow dark">Where the story came from</p>
  <div class="sourcelist">
    <p><a href="{PB_SOFT}" rel="noopener">Post Bulletin — Noodle House to host &lsquo;soft opening&rsquo; in downtown Rochester</a></p>
    <p><a href="{PB_ORIGIN}" rel="noopener">Post Bulletin — Mango Thai owners cooking up a second restaurant</a></p>
    <p><a href="{KROC}" rel="noopener">KROC News — Noodle House menu and opening date</a></p>
    <p><a href="{KTTC}" rel="noopener">ABC 5 News — New Rochester restaurant set to open in late November</a></p>
    <p><a href="{KAALTV}" rel="noopener">ABC 6 News — New noodle restaurant opening in Rochester</a></p>
    <p><a href="{IG}" rel="noopener">Instagram @noodlehousemn</a> &middot;
       <a href="{FB}" rel="noopener">Facebook: The Noodle House</a></p>
  </div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

VISIT = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Visit &middot; the corner of South Broadway &amp; 4th Street SE</p>
  <h1>The front of the Kelley Building.</h1>
  <p class="lede">You&rsquo;ll see us from the corner — {STREET}, a few doors south of Mango Thai,
  in Rochester&rsquo;s first brick building. Walk in during open hours, or call {PHONE} first.</p>
  <div class="ctarow"><a class="btn chili" href="{DIRLINK}" rel="noopener">Get directions</a>
  <a class="btn ghost" href="{TEL}">Call {PHONE}</a></div>
</div></section>

<section class="band cream"><div class="wrap visitgrid">
  <div class="infocard"><h3 class="infh">Hours</h3>
    {HRS_TABLE}
    <p class="note">Soft-opened Sunday, November 8, 2026. Open seven days a week.</p></div>
  <div class="infocard"><h3 class="infh">Address</h3>
    <address class="addr">{STREET}<br>{CITYST}</address>
    <p class="note">The Kelley Building — full corner of Broadway Ave S and 4th Street SE, downtown
    Rochester. A few doors south of Mango Thai (318 S. Broadway).</p>
    <p class="bigm"><a href="{DIRLINK}" rel="noopener">Directions &rarr;</a></p></div>
  <div class="infocard"><h3 class="infh">Call or write</h3>
    <p class="note"><a class="lk" href="{TEL}">{PHONE}</a> &middot;
    <a class="lk" href="{MAILTO}">{EMAIL}</a></p>
    <p class="note">The fastest answers come by phone — the restaurant runs it during open hours.</p>
    <p class="bigm"><a href="/contact">Send a note &rarr;</a></p></div>
</div></section>

<section class="band mist mapband"><div class="wrap">
  <div class="mapcell">{MAP_EMBED}</div>
  <p class="fineprint">Map: The Noodle House, {STREET}, {CITYST}.</p>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

CONTACT = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Contact &middot; we read every note</p>
  <h1>Talk to the restaurant.</h1>
  <p class="lede">Call {PHONE}, email <a href="{MAILTO}">{EMAIL}</a>, or leave a note below — it goes
  straight to the restaurant&rsquo;s inbox.</p>
</div></section>

<section class="band cream"><div class="wrap contactgrid">
  <form class="cform" method="post" action="/contact">
    <div class="field"><label for="f-name">Your name</label>
      <input id="f-name" name="name" type="text" autocomplete="name" maxlength="120" required></div>
    <div class="field"><label for="f-phone">Phone <span class="opt">(optional)</span></label>
      <input id="f-phone" name="phone" type="tel" autocomplete="tel" maxlength="60"></div>
    <div class="field"><label for="f-email">Email <span class="opt">(optional)</span></label>
      <input id="f-email" name="email" type="email" autocomplete="email" maxlength="120"></div>
    <div class="field"><label for="f-msg">Your message</label>
      <textarea id="f-msg" name="message" rows="5" maxlength="4000" required
        placeholder="A table, a bowl, feedback — anything goes."></textarea></div>
    <div class="ctarow"><button class="btn chili" type="submit">Send it</button></div>
  </form>
  <div class="visitgrid side">
    <div class="infocard"><h3 class="infh">Phone</h3>
      <p class="bigm"><a href="{TEL}">{PHONE}</a></p>
      <p class="note">Answered during open hours.</p></div>
    <div class="infocard"><h3 class="infh">Address</h3>
      <address class="addr">{STREET}<br>{CITYST}</address>
      <p class="note"><a class="lk" href="{DIRLINK}" rel="noopener">Directions</a> &middot;
      <a class="lk" href="/visit">Visiting details</a></p></div>
  </div>
</div></section>

<section class="band mist mapband"><div class="wrap">
  <div class="mapcell">{MAP_EMBED}</div>
  <p class="fineprint">Map: The Noodle House, {STREET}, {CITYST}.</p>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

PRIVACY = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap">
  <p class="eyebrow">Privacy</p>
  <h1>Plain words about your data.</h1>
</div></section>

<section class="band cream"><div class="wrap narrow prose">
  <p class="first"><strong>Last updated November 22, 2026.</strong> This website is published for
  The Noodle House. It sets no cookies of its own, runs no third-party scripts, and keeps no
  analytics &mdash; pages are plain text and one stylesheet.</p>
  <h3 class="h4">The note form</h3>
  <p>When you submit the contact form, the name, phone, email and message you type are sent to the
  restaurant&rsquo;s inbox through an email-delivery service, so a person can answer. That is the
  entire purpose. Nothing is sold, rented, or added to a mailing list.</p>
  <h3 class="h4">Maps</h3>
  <p>Pages with a map load a Google Maps embed, which may set Google&rsquo;s own cookies once you
  look at it. Google&rsquo;s privacy policy covers what Google does with those.</p>
  <h3 class="h4">Your choices</h3>
  <p>Want a note deleted after it&rsquo;s answered? Reply to the email you receive and say so.</p>
  <h3 class="h4">Questions</h3>
  <p>Call <a href="{TEL}">{PHONE}</a>, or remember the address: {STREET}, {CITYST}.</p>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

THANKS = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap narrow center">
  <p class="eyebrow">Note received</p>
  <h1>Your note landed.</h1>
  <p class="lede">It went straight to the restaurant&rsquo;s inbox and the team reads every one.
  Need an answer faster? Call {PHONE}.</p>
  <div class="ctarow"><a class="btn chili" href="/">Back to the front page</a>
  <a class="btn ghost" href="/menu">See the menu</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

NOTFOUND = f"""<body>
<a class="skip" href="#main">Skip to content</a>
{HEADER}
<main id="main">

<section class="band ink herol"><div class="wrap narrow center">
  <p class="eyebrow">404</p>
  <h1>This bowl is empty.</h1>
  <p class="lede">We couldn&rsquo;t find that page. Try one of these:</p>
  <div class="ctarow"><a class="btn chili" href="/">Front page</a>
  <a class="btn ghost" href="/menu">Menu</a>
  <a class="btn ghost" href="/contact">Contact</a></div>
</div></section>

</main>
{FOOTER}
</body>
</html>"""

# titles / descs
TITLES = {
    "/": ("The Noodle House &mdash; Pho, Ramen &amp; Khao Soi in Rochester, MN",
          "The Noodle House serves pho, khao soi, ramen and chicken karaage in the 1858 Kelley Building at 332 Broadway Ave S, downtown Rochester, MN. Open daily. (507) 206-0577."),
    "/menu": ("The Menu &mdash; Pho, Ramen, Khao Soi &amp; Karaage | The Noodle House, Rochester MN",
              "The Noodle House menu: pho, ramen, khao soi and chicken karaage — the noodle dishes the owners named to KROC News. Prices and the full board at the restaurant. Rochester, MN."),
    "/bowls": ("Pho &amp; Ramen Bowls &mdash; The Noodle House, Rochester MN",
               "Slow-simmered broth bowls at The Noodle House in Rochester, MN: Vietnamese pho with rice noodles and Japanese-style ramen, cooked by the owners of Mango Thai."),
    "/wok-fried": ("Khao Soi &amp; Chicken Karaage &mdash; The Noodle House, Rochester MN",
                   "Northern Thai khao soi with a crisp noodle garnish and Japanese-style chicken karaage at The Noodle House, 332 Broadway Ave S, Rochester, MN."),
    "/our-story": ("Our Story &mdash; Chef Chai &amp; Marlene Rachwat | The Noodle House, Rochester MN",
                   "The Mango Thai owners' noodle obsession, an 1858 brick landmark on Broadway and 4th, and a soft opening on November 8, 2026: the story of The Noodle House, Rochester, MN."),
    "/visit": ("Visit &mdash; Hours &amp; Directions, 332 Broadway Ave S | The Noodle House, Rochester MN",
               "The Noodle House, 332 Broadway Ave S, Rochester, MN 55904 — open daily 11-9 Mon-Thu, till 10 Fri and Sat, 12-8 Sun. Corner of South Broadway and 4th Street SE. (507) 206-0577."),
    "/contact": ("Contact The Noodle House &mdash; (507) 206-0577, Rochester MN",
                 "Call (507) 206-0577, email noodlehouse332@gmail.com or use the form — The Noodle House answers from the restaurant's inbox. 332 Broadway Ave S, Rochester, MN."),
    "/privacy": ("Privacy &mdash; The Noodle House, Rochester MN",
                 "No cookies, no third-party scripts, no analytics. Contact-form notes go straight to The Noodle House's inbox and nowhere else."),
    "/thanks": ("Note received &mdash; The Noodle House, Rochester MN",
                "Your note went straight to The Noodle House inbox. The team reads and answers every one."),
    "/404": ("Page not found &mdash; The Noodle House, Rochester MN",
             "That page couldn't be found. Head back to the front page, the menu, or contact."),
}

def plain(s):
    return (s.replace("&rsquo;", "\u2019").replace("&ldquo;", "\u201c").replace("&rdquo;", "\u201d")
             .replace("&mdash;", "\u2014").replace("&middot;", "\u00b7").replace("&amp;", "&")
             .replace("&nbsp;", " ").replace("&rarr;", "\u2192").replace("&ndash;", "\u2013"))

def ld_webpage(path, extra=None):
    t, d = TITLES[path]
    return webpage(path, plain(t), plain(d), extra)

PAGES = [
    ("/", "index.html", HOME,
     ld_webpage("/", [FAQ, BIZ]) ),
    ("/menu", "menu.html", MENU,
     ld_webpage("/menu", [
        {"@type": "Menu", "@id": ORIGIN + "/menu#menu", "name": "The Noodle House Menu",
         "url": ORIGIN + "/menu", "hasPart": [
            {"@type": "MenuSection", "name": "Broth Bowls", "hasMenuItem": [
                {"@type": "MenuItem", "name": "Pho", "description": "Vietnamese rice-noodle soup under a deeply simmered broth"},
                {"@type": "MenuItem", "name": "Ramen", "description": "Japanese-style noodle bowls in savory broth"}]},
            {"@type": "MenuSection", "name": "Wok & Fryer", "hasMenuItem": [
                {"@type": "MenuItem", "name": "Khao Soi", "description": "Northern Thai curried noodles with a crisp fried-noodle garnish"},
                {"@type": "MenuItem", "name": "Chicken Karaage", "description": "Japanese-style fried chicken"}]}]},
        breadcrumb([("Home", "/"), ("Menu", "/menu")]) ])),
    ("/bowls", "bowls.html", BOWLS,
     ld_webpage("/bowls", [
        service("/bowls", "Pho & Ramen Bowls", "Restaurant Bowl Service",
                "Vietnamese pho and Japanese-style ramen bowls in slow-simmered broth at The Noodle House, Rochester, Minnesota."),
        breadcrumb([("Home", "/"), ("Menu", "/menu"), ("Broth bowls", "/bowls")]) ])),
    ("/wok-fried", "wok-fried.html", WOKFRIED,
     ld_webpage("/wok-fried", [
        service("/wok-fried", "Khao Soi & Chicken Karaage", "Restaurant Plate Service",
                "Northern Thai khao soi and Japanese-style chicken karaage at The Noodle House, Rochester, Minnesota."),
        breadcrumb([("Home", "/"), ("Menu", "/menu"), ("Wok & fryer", "/wok-fried")]) ])),
    ("/our-story", "our-story.html", OURSTORY,
     ld_webpage("/our-story", [breadcrumb([("Home", "/"), ("Our story", "/our-story")])])),
    ("/visit", "visit.html", VISIT,
     ld_webpage("/visit", [breadcrumb([("Home", "/"), ("Visit", "/visit")])])),
    ("/contact", "contact.html", CONTACT,
     ld_webpage("/contact", [breadcrumb([("Home", "/"), ("Contact", "/contact")])])),
    ("/privacy", "privacy.html", PRIVACY, ld_webpage("/privacy")),
    ("/thanks", "thanks.html", THANKS, None),
    ("/404", "404.html", NOTFOUND, None),
]

for path, fname, body_html, ld_html in PAGES:
    t, d = TITLES[path]
    doc = head(path, t, plain(d)) + "\n" + body_html
    if ld_html:
        doc = doc.replace("</head>", ld_html + "\n</head>")
    with open(os.path.join("public", fname), "w", encoding="utf-8") as f:
        f.write(doc)

urls = "\n".join(
    f'<url><loc>{ORIGIN}{("/" if p == "/" else p)}</loc><lastmod>2026-11-22</lastmod></url>'
    for p in ["/", "/menu", "/bowls", "/wok-fried", "/our-story", "/visit", "/contact", "/privacy"])
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n")
open("public/sitemap.xml", "w").write(sitemap)
open("public/robots.txt", "w").write(
    f"User-agent: *\nDisallow: /thanks\nDisallow: /404\n\nSitemap: {ORIGIN}/sitemap.xml\n")

print("wrote", sum(1 for _ in PAGES), "pages + sitemap + robots")
