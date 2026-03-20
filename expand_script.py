import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

head_match = re.search(r'(<head>.*?</head>)', content, re.DOTALL)
header_match = re.search(r'(<header.*?</header>)', content, re.DOTALL)
footer_match = re.search(r'(<footer.*?</body>)', content, re.DOTALL)

if not head_match or not header_match or not footer_match:
    print("Failed to find base chunks.")
    exit(1)

head = head_match.group(1)
header = header_match.group(1)
footer = footer_match.group(1)
head = re.sub(r'<title>.*?</title>', '<title>{TITLE} | Blossom Boutique</title>', head)

def build_html(title, main_content):
    html = f"""<!DOCTYPE html>\n<html lang="en" data-bs-theme="light">\n{head.replace('{TITLE}', title)}\n<body class="bg-light">\n{header}\n{main_content}\n{footer}\n</html>"""
    return html

names = ["Classic Red", "Pastel Dreams", "Sunshine Yellow", "Ethereal White", "Vibrant Spring", "Blush Peony Dream", "Velvet Romance", "Morning Dew", "Golden Sunset", "Midnight Lily"]

items_html = ""
for i in range(10):
    badge = '<div class="position-absolute top-0 start-0 m-3"><span class="badge bg-primary px-3 py-2 rounded-pill shadow-sm">Popular</span></div>' if i in [0, 4] else ''
    items_html += f"""
    <div class="col">
        <div class="card border-0 shadow-sm h-100 product-card">
            {badge}
            <img src="assets/images/products/flower-{i}.jpg" class="card-img-top object-fit-cover" style="aspect-ratio: 4/3;" alt="{names[i]}">
            <div class="card-body p-4 d-flex flex-column">
                <div class="d-flex justify-content-between align-items-center mb-1">
                    <h3 class="h5 fw-bold mb-0 text-dark">{names[i]}</h3>
                    <span class="text-primary fw-bold fs-5">${60 + (i*5)}</span>
                </div>
                <p class="text-muted small mb-4">Premium Collection</p>
                <a href="product-detail.html" class="btn btn-outline-primary mt-auto w-100 py-2">View Details</a>
            </div>
        </div>
    </div>
    """

ten_grid = f'<div class="row row-cols-1 row-cols-sm-2 g-5">\n{items_html}\n</div>'

def subpage_template(title, desc):
    return f"""
    <main class="bg-light">
        <section class="py-5" style="background-color: var(--bg-white);">
            <div class="container text-center">
                <h1 class="display-4 fw-bold mb-3">{title}</h1>
                <p class="lead text-muted mx-auto" style="max-width: 600px;">{desc}</p>
            </div>
        </section>
        <section class="py-3 bg-white border-bottom shadow-sm">
            <div class="container d-flex flex-wrap justify-content-between align-items-center gap-3">
                <div class="fw-bold text-muted">Showing 10 beautiful arrangements</div>
                <div class="d-flex gap-2">
                    <select class="form-select form-select-sm w-auto"><option>Sort by Popularity</option><option>Price: Low to High</option></select>
                </div>
            </div>
        </section>
        <section class="section-padding bg-light">
            <div class="container" style="max-width: 1000px;">
                {ten_grid}
            </div>
        </section>
        <section class="py-5 bg-white text-center">
            <div class="container">
                <h2 class="h3 fw-bold mb-3">Can't decide? Let us help!</h2>
                <p class="text-muted mb-4">Our florists are ready to craft a custom arrangement specifically for your needs.</p>
                <a href="contact.html" class="btn btn-primary px-4 py-2">Contact a Florist</a>
            </div>
        </section>
    </main>
    """

def home_template(hero_title):
    return f"""
    <main class="bg-light">
        <section class="py-5 py-lg-7" style="background-color: var(--bs-secondary);">
            <div class="container">
                <div class="row align-items-center gy-5">
                    <div class="col-lg-6 text-center text-lg-start">
                        <h1 class="display-3 fw-bold mb-4 text-dark">{hero_title}</h1>
                        <p class="lead opacity-75 text-dark mb-5">Beautiful, hand-crafted floral arrangements for every special moment. Bringing joy to your loved ones with our fresh blooms.</p>
                        <div class="d-flex flex-wrap gap-3 justify-content-center justify-content-lg-start">
                            <a href="shop.html" class="btn btn-primary btn-lg px-4 border-0">Order Now</a>
                            <a href="occasions.html" class="btn btn-outline-dark btn-lg px-4 fw-bold">Explore Occasions</a>
                        </div>
                    </div>
                    <div class="col-lg-6 text-center position-relative">
                        <img src="assets/images/hero.jpg" alt="Beautiful flower arrangement" class="img-fluid rounded-4 shadow-lg w-100" style="aspect-ratio: 4/3; object-fit: cover; max-width: 500px;">
                    </div>
                </div>
            </div>
        </section>
        <section class="py-5 bg-white border-bottom">
            <div class="container">
                <div class="row g-4 text-center">
                    <div class="col-md-4"><div class="p-4"><i class="bi bi-truck display-4 text-primary mb-3"></i><h3 class="h5 fw-bold">Same-Day Delivery</h3><p class="text-muted text-sm">Order before 4 PM for fast delivery.</p></div></div>
                    <div class="col-md-4"><div class="p-4"><i class="bi bi-flower1 display-4 text-primary mb-3"></i><h3 class="h5 fw-bold">Farm Fresh Blooms</h3><p class="text-muted text-sm">Sourced directly from local farms.</p></div></div>
                    <div class="col-md-4"><div class="p-4"><i class="bi bi-heart display-4 text-primary mb-3"></i><h3 class="h5 fw-bold">100% Satisfaction</h3><p class="text-muted text-sm">We guarantee perfectly arranged bouquets.</p></div></div>
                </div>
            </div>
        </section>
        <section class="section-padding bg-light">
            <div class="container">
                <div class="text-center mb-5"><h2 class="display-5 fw-bold mb-3">Shop by Occasion</h2></div>
                <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4 g-4 justify-content-center">
                    <div class="col"><a href="occasion-birthday.html" class="card h-100 text-decoration-none border-0 shadow-sm text-center"><div class="card-body py-5"><h3 class="h4 card-title fw-bold text-dark">Birthday</h3></div></a></div>
                    <div class="col"><a href="occasion-anniversary.html" class="card h-100 text-decoration-none border-0 shadow-sm text-center"><div class="card-body py-5"><h3 class="h4 card-title fw-bold text-dark">Anniversary</h3></div></a></div>
                    <div class="col"><a href="occasion-love.html" class="card h-100 text-decoration-none border-0 shadow-sm text-center"><div class="card-body py-5"><h3 class="h4 card-title fw-bold text-dark">Romance</h3></div></a></div>
                    <div class="col"><a href="occasion-sympathy.html" class="card h-100 text-decoration-none border-0 shadow-sm text-center"><div class="card-body py-5"><h3 class="h4 card-title fw-bold text-dark">Sympathy</h3></div></a></div>
                </div>
            </div>
        </section>
        <section class="section-padding bg-white border-top">
            <div class="container" style="max-width: 1000px;">
                <div class="text-center mb-5"><h2 class="display-5 fw-bold mb-3">Featured Bestsellers</h2></div>
                {ten_grid}
            </div>
        </section>
        <section class="py-5 bg-primary text-white text-center">
            <div class="container py-4">
                <h2 class="display-5 fw-bold mb-3 text-white">Join the Blossom Club</h2>
                <p class="lead mb-4 mx-auto text-white opacity-75" style="max-width:600px;">Sign up today and get 15% off your first luxury arrangement.</p>
                <div class="d-flex justify-content-center"><a href="register.html" class="btn btn-light btn-lg px-5 fw-bold border-0 text-primary rounded-pill shadow">Sign Up Now</a></div>
            </div>
        </section>
    </main>
    """

files_to_update = {
    'index.html': ('Home', home_template('Send Love with Flowers Today')),
    'home-2.html': ('Home 2', home_template('Modern Floral Masterpieces')),
    'shop.html': ('All Collections', subpage_template('All Collections', 'Browse our complete catalog of stunning floral arrangements.')),
    'occasions.html': ('All Occasions', subpage_template('Shop by Occasion', 'Every moment deserves beautiful blooms. Browse our occasion categories.')),
    'occasion-birthday.html': ('Birthday Flowers', subpage_template('Birthday Flowers', 'Celebrate with vibrant, joyous arrangements perfect for birthdays.')),
    'occasion-anniversary.html': ('Anniversary Flowers', subpage_template('Anniversary Flowers', 'Express your eternal love with absolute beauty and grace.')),
    'occasion-love.html': ('Love & Romance', subpage_template('Love & Romance', 'Deep reds, passionate pinks, and beautiful romantic gestures.')),
    'occasion-sympathy.html': ('Sympathy Flowers', subpage_template('Sympathy Flowers', 'Gentle, white, and peaceful arrangements to show you care.')),
    'shop-roses.html': ('Luxury Roses', subpage_template('Luxury Roses', 'Handpicked, premium long-stemmed roses for every romantic occasion.')),
    'shop-lilies.html': ('Elegant Lilies', subpage_template('Elegant Lilies', 'Stargazers, callas, and majestic pure lilies.')),
    'shop-mixed.html': ('Mixed Bouquets', subpage_template('Mixed Bouquets', 'A colorful celebration of seasonal favorites crafted together.'))
}

for fname, (title, content) in files_to_update.items():
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(build_html(title, content))
    print(f"Expanded {fname} successfully.")
