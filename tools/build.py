"""Build LogoPack static pages. Usage: python3 tools/build.py <site_dir>"""
import json, os, sys, html

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://logopack.ca"
EMAIL = "logopackca@gmail.com"
TODAY = "2026-11-20"
V = "1"

ICONS = {
    "cup": '<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="9" y="7" width="30" height="6" rx="3" fill="#2b1d14"/><path d="M11 13h26l-3 29a2.5 2.5 0 0 1-2.5 2.2h-15A2.5 2.5 0 0 1 14 42z" fill="#fff" stroke="#2b1d14" stroke-width="2"/><path d="M12.6 22h22.8l-1.2 11H13.8z" fill="#e8553a"/></svg>',
    "sleeve": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M8 14h32l-3 22H11z" fill="#e8553a"/><path d="M8 14h32l-.4 3H8.4z" fill="#c9422a"/><path d="M11 33h26l-.4 3H11.4z" fill="#c9422a"/><path d="M19 25l3.5 3.5L30 21" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "bag": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M17 15c0-7 14-7 14 0" fill="none" stroke="#9c6f45" stroke-width="3" stroke-linecap="round"/><path d="M8 15h32l-2 28H10z" fill="#c9a073"/><path d="M8 15h32l-.3 3H8.3z" fill="#b8875a"/><rect x="17" y="24" width="14" height="10" rx="2" fill="#2b1d14"/></svg>',
    "sleevebag": '<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M13 9l3-3 3 3 3-3 3 3 3-3 3 3 3-3 3 3v33H13z" fill="#fbf7f0" stroke="#2b1d14" stroke-width="2" stroke-linejoin="round"/><circle cx="24" cy="23" r="6" fill="#e8553a"/><rect x="18" y="33" width="12" height="2.5" rx="1.2" fill="#2b1d14" opacity=".6"/></svg>',
}

PRODUCTS = [
    {
        "slug": "custom-paper-cups", "icon": "cup", "nav": "Custom paper cups",
        "title": "Custom Printed Paper Coffee Cups with Your Logo | LogoPack Vancouver",
        "desc": "Custom printed paper coffee cups for cafés, coffee shops and restaurants. Hot and cold cups in popular sizes, printed with your logo. Get a quote from LogoPack in Vancouver, BC.",
        "h1": "Custom printed paper cups with your logo",
        "card": "Hot and cold paper cups printed with your logo, in the sizes your menu uses.",
        "intro": "Every coffee that leaves your counter is a walking ad. LogoPack prints paper cups with your logo and colours for coffee shops, cafés, restaurants and bubble tea shops.",
        "includes": [
            "Single-wall and double-wall hot cups",
            "Paper cold cups for iced drinks",
            "Popular sizes, from espresso cups to large to-go cups",
            "One-colour logos or full-colour designs",
            "Matching sleeves and lids available on request",
            "Recyclable or compostable materials on request",
        ],
        "body": "<p>Tell us the sizes you serve and roughly how many cups you go through each month, and send your logo. We'll recommend a cup and print style, quote it, and send a digital proof of your cup so you can see exactly how it will look before anything is printed.</p><p>Double-wall cups keep hands comfortable without a sleeve. Single-wall cups paired with a branded sleeve are often the more economical choice.</p>",
        "faq": [
            ("What's the minimum order for custom printed cups?", "It depends on the cup type, size and print method. Tell us your sizes and estimated quantities and we'll quote the best option for your volume."),
            ("Can you match my brand colours?", "Yes. Send your logo and brand colours and we'll match them as closely as the print process allows, and show you a proof first."),
            ("Do you have compostable cups?", "Tell us if you need recyclable or compostable cups and we'll quote suitable options."),
        ],
    },
    {
        "slug": "coffee-cup-sleeves", "icon": "sleeve", "nav": "Coffee cup sleeves",
        "title": "Custom Printed Coffee Cup Sleeves | Branded Sleeves | LogoPack",
        "desc": "Custom printed coffee cup sleeves with your logo. An affordable way to brand plain cups for cafés and coffee shops. Get a quote from LogoPack, Vancouver BC.",
        "h1": "Custom printed coffee cup sleeves",
        "card": "Branded sleeves that turn plain cups into your cups, and protect hands from heat.",
        "intro": "A printed sleeve is one of the most affordable ways to put your brand on every hot drink. Use them with plain stock cups and switch designs for seasons or promotions.",
        "includes": [
            "Sleeves sized for standard hot cup sizes",
            "Kraft or white sleeves",
            "One-colour logos or full-colour designs",
            "Space for a website, social handle or QR code",
            "Seasonal or limited-edition designs",
            "Shipped flat for easy storage behind the counter",
        ],
        "body": "<p>Sleeves are a good fit if you're not ready for fully printed cups, or want to change your design more often. Send us your logo and cup sizes and we'll quote sleeves that fit, with a digital proof before printing.</p>",
        "faq": [
            ("Will your sleeves fit my cups?", "Tell us the brand or sizes of the cups you use and we'll make sure the sleeves fit."),
            ("Can I add a QR code?", "Yes. Many cafés add a QR code for their menu, loyalty program or social media."),
            ("Are sleeves cheaper than printed cups?", "Usually, yes, especially at lower volumes, because you can use plain stock cups and only brand the sleeve."),
        ],
    },
    {
        "slug": "paper-bags", "icon": "bag", "nav": "Paper takeout bags",
        "title": "Custom Printed Paper Bags for Restaurants & Takeout | LogoPack",
        "desc": "Custom printed kraft and white paper bags with handles for restaurants, cafés and takeout. Branded paper bags with your logo from LogoPack, Vancouver BC.",
        "h1": "Custom printed paper bags for takeout",
        "card": "Kraft and white paper bags with handles, printed with your logo for takeout and delivery.",
        "intro": "Takeout and delivery orders travel all over town. A printed paper bag puts your name on every one. LogoPack supplies branded paper bags for restaurants, cafés, bakeries and food trucks.",
        "includes": [
            "Kraft (brown) and white paper bags",
            "Twisted or flat paper handles",
            "Square-bottom bags that stand up for takeout containers",
            "Sizes for single drinks up to large family orders",
            "One-colour or multi-colour logo printing",
            "Grease-resistant options on request",
        ],
        "body": "<p>Tell us what goes in the bag (drinks, bowls, boxed meals) and your typical order sizes, and we'll suggest bag sizes that fit. Your quote comes with a digital proof of your printed bag.</p>",
        "faq": [
            ("What size bag do I need?", "It depends on your containers. Tell us what you pack, for example two drinks or a family meal, and we'll recommend sizes."),
            ("Kraft or white bags?", "Kraft has a natural, rustic look and hides marks well. White makes colourful logos stand out. We can show you both."),
            ("Can you print on both sides?", "Yes, ask for one-side or two-side printing in your quote request."),
        ],
    },
    {
        "slug": "paper-sleeve-bags", "icon": "sleevebag", "nav": "Paper sleeve bags",
        "title": "Custom Paper Sleeve Bags for Bakeries, Sandwiches & Pastries | LogoPack",
        "desc": "Custom printed paper sleeve bags and flat bags for sandwiches, pastries, cookies and baked goods. Branded with your logo by LogoPack, Vancouver BC.",
        "h1": "Paper sleeve bags for sandwiches and pastries",
        "card": "Flat paper sleeve bags for sandwiches, pastries and baked goods, with your logo.",
        "intro": "Croissants, cookies, sandwiches and wraps leave the counter in a paper sleeve bag. LogoPack prints them with your logo so grab-and-go items are branded too.",
        "includes": [
            "Flat paper bags and sleeve bags",
            "Sandwich, wrap and panini sizes",
            "Pastry, cookie and bakery sizes",
            "Kraft or white paper",
            "Grease-resistant paper for buttery baked goods",
            "Window bags so customers can see what's inside",
        ],
        "body": "<p>Tell us what you serve and roughly how many you use each week, and we'll recommend bag sizes and paper. We send a digital proof of your printed bag before production.</p>",
        "faq": [
            ("What's the difference between a sleeve bag and a takeout bag?", "Sleeve bags are flat, open-ended or folded bags for single items like a pastry or sandwich. Takeout bags have a square bottom and handles for full orders."),
            ("Do you have grease-resistant bags?", "Yes, ask for grease-resistant paper in your quote request, which is ideal for croissants and other buttery items."),
            ("Can I get window bags?", "Yes. Tell us the size and we'll quote window bags with your logo."),
        ],
    },
]

HOME_FAQ = [
    ("Who is LogoPack for?", "Coffee shops, cafés, restaurants, bakeries, bubble tea shops and food trucks that want their own branded cups, sleeves and paper bags."),
    ("What's the minimum order?", "It depends on the product and print method. Tell us what you need and roughly how many, and your quote will include options for your volume."),
    ("How long does it take?", "It depends on the product and quantity. Your quote includes an estimated production and delivery time."),
    ("Do I need a designer?", "No. Send us your logo, ideally as a PDF, AI, SVG or high-resolution PNG, and we'll place it on your packaging and send a digital proof for approval."),
    ("Do you have eco-friendly options?", "Tell us if you need recyclable or compostable materials and we'll quote suitable options."),
    ("Where are you based?", "LogoPack is based in Vancouver, BC. Ask us about delivery to your area."),
]


def head(title, desc, url, prefix, schema, og_type="website"):
    return f"""<!doctype html>
<html lang="en-CA">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="robots" content="index,follow">
    <link rel="canonical" href="{url}">
    <link rel="icon" href="/favicon.ico" sizes="48x48">
    <link rel="icon" type="image/svg+xml" href="/logo.svg">
    <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <meta name="theme-color" content="#2b1d14">
    <meta property="og:site_name" content="LogoPack">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="{og_type}">
    <meta property="og:url" content="{url}">
    <meta property="og:locale" content="en_CA">
    <meta property="og:image" content="{SITE}/images/og-logopack.png">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{prefix}styles.css?v={V}">
    <script type="application/ld+json">
{json.dumps(schema, indent=2, ensure_ascii=False)}
    </script>
  </head>
  <body>
    <header class="site-header">
      <div class="container nav">
        <a class="brand" href="{prefix}">
          <img src="{prefix}logo.svg" alt="" width="40" height="40">
          <span>Logo<b>Pack</b></span>
        </a>
        <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="Open menu">
          <span></span><span></span><span></span>
        </button>
        <nav id="nav-links" class="nav-links">
          <a href="{prefix}#products">Products</a>
          <a href="{prefix}#how">How it works</a>
          <a href="{prefix}#faq">FAQ</a>
          <a class="btn btn-small" href="{prefix}#quote">Get a quote</a>
        </nav>
      </div>
    </header>
"""


def footer(prefix):
    links = " · ".join(f'<a href="{prefix}{p["slug"]}/">{p["nav"]}</a>' for p in PRODUCTS)
    return f"""    <footer class="site-footer">
      <div class="container footer-grid">
        <a class="brand" href="{prefix}">
          <img src="{prefix}logo.svg" alt="" width="32" height="32">
          <span>Logo<b>Pack</b></span>
        </a>
        <p>{links}</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p>© <span id="year">2026</span> LogoPack · Vancouver, BC</p>
      </div>
    </footer>

    <script src="{prefix}script.js?v={V}"></script>
  </body>
</html>
"""


def faq_html(faq):
    return "\n".join(f"          <details>\n            <summary>{q}</summary>\n            <p>{a}</p>\n          </details>" for q, a in faq)


def faq_schema(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


BUSINESS = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "LogoPack",
    "url": SITE + "/",
    "logo": SITE + "/icon-512.png",
    "image": SITE + "/images/og-logopack.png",
    "email": EMAIL,
    "description": "Custom printed paper cups, coffee cup sleeves, paper takeout bags and paper sleeve bags for coffee shops, cafés and restaurants. Based in Vancouver, BC.",
    "address": {"@type": "PostalAddress", "addressLocality": "Vancouver", "addressRegion": "BC", "addressCountry": "CA"},
    "areaServed": {"@type": "Country", "name": "Canada"},
    "knowsAbout": ["Custom printed paper cups", "Coffee cup sleeves", "Paper bags", "Paper sleeve bags", "Food packaging", "Coffee shop packaging"],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Custom printed packaging", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Product", "name": p["nav"], "url": f"{SITE}/{p['slug']}/"}} for p in PRODUCTS]},
}


def quote_section():
    chips = "\n".join(f'                <label><input type="checkbox" name="products" value="{p["nav"]}"> {p["nav"]}</label>' for p in PRODUCTS)
    return f"""      <section id="quote" class="section quote">
        <div class="container quote-grid">
          <div>
            <p class="eyebrow">Free quote</p>
            <h2>Let's put your logo on it</h2>
            <p>Tell us what you need and roughly how many. We'll reply with pricing and a digital proof of your packaging. You can also email us at <a href="mailto:{EMAIL}">{EMAIL}</a>, and attach your logo.</p>
          </div>
          <form id="quote-form" class="quote-form">
            <label>Your name<input name="name" required autocomplete="name"></label>
            <label>Business name<input name="business" required autocomplete="organization"></label>
            <label>Email<input name="email" type="email" required autocomplete="email"></label>
            <label>Phone (optional)<input name="phone" type="tel" autocomplete="tel"></label>
            <fieldset class="full">
              <legend>What do you need?</legend>
              <div class="chips">
{chips}
              </div>
            </fieldset>
            <label>Rough quantity<input name="quantity" placeholder="e.g. 5,000 x 12 oz cups"></label>
            <label>When do you need it?
              <select name="timeline">
                <option>Just getting prices</option>
                <option>Within a month</option>
                <option>1–3 months</option>
                <option>For a new opening</option>
              </select>
            </label>
            <label class="full">Tell us more<textarea name="details" rows="4" placeholder="Sizes, colours, kraft or white, anything else…"></textarea></label>
            <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" aria-hidden="true">
            <button class="btn full" type="submit">Request a quote</button>
            <p class="form-status full" role="status" aria-live="polite"></p>
          </form>
        </div>
      </section>
"""


def home():
    cards = "\n".join(f"""            <a class="card card-link" href="./{p['slug']}/">
              <div class="icon">{ICONS[p['icon']]}</div>
              <h3>{p['nav']}</h3>
              <p>{p['card']}</p>
              <span class="more">See options →</span>
            </a>""" for p in PRODUCTS)
    schema = [BUSINESS, faq_schema(HOME_FAQ), {"@context": "https://schema.org", "@type": "WebSite", "name": "LogoPack", "url": SITE + "/"}]
    return head("LogoPack | Custom Printed Coffee Cups, Sleeves & Paper Bags | Vancouver",
                "Custom printed paper cups, coffee cup sleeves, paper takeout bags and sleeve bags with your logo, for coffee shops, cafés and restaurants. Based in Vancouver, BC.",
                SITE + "/", "./", schema) + f"""
    <main id="top">
      <section class="hero">
        <div class="container hero-grid">
          <div>
            <p class="eyebrow">Branded packaging for cafés &amp; restaurants</p>
            <h1>Your logo on every <em>cup</em> and bag.</h1>
            <p class="lead">LogoPack makes custom printed paper cups, coffee sleeves and paper bags for coffee shops, cafés and restaurants, so every order that leaves your counter carries your brand.</p>
            <div class="hero-actions">
              <a class="btn" href="#quote">Get a free quote</a>
              <a class="btn btn-ghost" href="#products">See products</a>
            </div>
            <ul class="hero-points">
              <li>Digital proof before printing</li>
              <li>Help placing your logo</li>
              <li>Based in Vancouver, BC</li>
            </ul>
          </div>
          <div class="hero-art">
            <img src="./images/hero-packaging.svg" alt="Illustration of a coffee cup with a branded sleeve, a kraft takeout bag and a paper sleeve bag, each showing a custom logo" width="560" height="480" fetchpriority="high">
          </div>
        </div>
      </section>

      <div class="strip" aria-label="Who we work with">
        <ul class="container">
          <li>Coffee shops</li><li>Cafés</li><li>Restaurants</li><li>Bakeries</li><li>Bubble tea</li><li>Food trucks</li>
        </ul>
      </div>

      <section id="products" class="section">
        <div class="container">
          <p class="eyebrow">Products</p>
          <h2>Custom packaging, printed with your brand</h2>
          <div class="cards">
{cards}
          </div>
        </div>
      </section>

      <section class="section section-dark">
        <div class="container">
          <p class="eyebrow">Why branded packaging</p>
          <h2>Plain cups don't bring customers back</h2>
          <div class="who">
            <div><h3>Free advertising</h3><p>Cups and bags travel through offices, streets and social media feeds. Your logo goes with them.</p></div>
            <div><h3>Looks established</h3><p>Branded packaging makes a new café or restaurant look polished from day one.</p></div>
            <div><h3>One supplier</h3><p>Cups, sleeves and bags from one place, in matching colours, on one quote.</p></div>
          </div>
        </div>
      </section>

      <section id="how" class="section section-alt">
        <div class="container">
          <p class="eyebrow">How it works</p>
          <h2>From logo to counter in four steps</h2>
          <ol class="steps">
            <li><span class="step-num">1</span><h3>Tell us what you need</h3><p>Products, sizes and rough quantities. Send your logo if you have it.</p></li>
            <li><span class="step-num">2</span><h3>Get a quote</h3><p>We reply with pricing options and an estimated timeline.</p></li>
            <li><span class="step-num">3</span><h3>Approve your proof</h3><p>See a digital mockup of your packaging. Nothing prints until you approve it.</p></li>
            <li><span class="step-num">4</span><h3>Production &amp; delivery</h3><p>Your branded packaging is produced and delivered, ready for service.</p></li>
          </ol>
        </div>
      </section>

      <section id="faq" class="section">
        <div class="container narrow">
          <p class="eyebrow">FAQ</p>
          <h2>Questions we get a lot</h2>
{faq_html(HOME_FAQ)}
        </div>
      </section>

{quote_section()}
    </main>

{footer('./')}"""


def product(p):
    url = f"{SITE}/{p['slug']}/"
    schema = [
        {"@context": "https://schema.org", "@type": "Product", "name": html.unescape(p["h1"]), "description": p["desc"],
         "url": url, "image": f"{SITE}/images/og-logopack.png", "brand": {"@type": "Brand", "name": "LogoPack"}},
        faq_schema(p["faq"]),
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": p["nav"], "item": url}]},
    ]
    inc = "\n".join(f"              <li>{i}</li>" for i in p["includes"])
    rel = "\n".join(f'            <li><a href="../{o["slug"]}/">{o["nav"]}</a></li>' for o in PRODUCTS if o is not p)
    big_icon = ICONS[p["icon"]].replace('aria-hidden="true"', 'role="img" aria-label="' + p["nav"] + '"')
    return head(p["title"], p["desc"], url, "../", schema) + f"""
    <main>
      <section class="page-hero">
        <div class="container page-hero-grid">
          <div>
            <nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a> / {p['nav']}</nav>
            <h1>{p['h1']}</h1>
            <p class="lead">{p['intro']}</p>
            <div class="hero-actions">
              <a class="btn" href="../#quote">Get a free quote</a>
              <a class="btn btn-ghost" href="mailto:{EMAIL}">Email your logo</a>
            </div>
          </div>
          <div class="product-art">{big_icon}</div>
        </div>
      </section>

      <section class="section">
        <div class="container split">
          <div>
            <h2>Options</h2>
            <ul class="checklist">
{inc}
            </ul>
          </div>
          <div class="prose">
            <h2>How ordering works</h2>
            {p['body']}
            <p>Nothing is printed until you approve your proof.</p>
          </div>
        </div>
      </section>

      <section class="section section-alt">
        <div class="container narrow">
          <p class="eyebrow">FAQ</p>
          <h2>Common questions</h2>
{faq_html(p['faq'])}
        </div>
      </section>

      <section class="section">
        <div class="container">
          <h2>Pair it with</h2>
          <ul class="related">
{rel}
          </ul>
        </div>
      </section>

      <section class="cta-band">
        <div class="container cta-inner">
          <h2>Ready to brand your {p['nav'].lower()}?</h2>
          <a class="btn" href="../#quote">Get a free quote</a>
        </div>
      </section>
    </main>

{footer('../')}"""


def main():
    open(os.path.join(OUT, "index.html"), "w").write(home())
    for p in PRODUCTS:
        d = os.path.join(OUT, p["slug"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w").write(product(p))
    urls = [("", "1.0")] + [(p["slug"] + "/", "0.8") for p in PRODUCTS]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr in urls:
        sm += ["  <url>", f"    <loc>{SITE}/{u}</loc>", f"    <lastmod>{TODAY}</lastmod>", f"    <priority>{pr}</priority>", "  </url>"]
    sm.append("</urlset>")
    open(os.path.join(OUT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    lines = [
        "# LogoPack", "",
        f"> LogoPack supplies custom printed paper cups, coffee cup sleeves, paper takeout bags and paper sleeve bags for coffee shops, cafés, restaurants, bakeries and food trucks. Based in Vancouver, British Columbia, Canada. Contact: {EMAIL}. Website: {SITE}", "",
        "Customers send their logo, products and rough quantities; LogoPack replies with a quote and a digital proof before anything is printed.", "",
        "## Products", "",
    ] + [f"- [{p['nav']}]({SITE}/{p['slug']}/): {p['card']}" for p in PRODUCTS] + [
        "", "## Contact", "", f"- Quote request form: {SITE}/#quote", f"- Email: {EMAIL}", ""]
    open(os.path.join(OUT, "llms.txt"), "w").write("\n".join(lines))
    print("built", len(urls), "pages")


if __name__ == "__main__":
    main()
