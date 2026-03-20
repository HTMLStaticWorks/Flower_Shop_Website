import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

head_match = re.search(r'(<head>.*?</head>)', index_content, re.DOTALL)
header_match = re.search(r'(<header.*?</header>)', index_content, re.DOTALL)
footer_match = re.search(r'(<footer.*?</body>)', index_content, re.DOTALL)

head = head_match.group(1).replace('<title>Blossom Boutique | Premium Floral Services</title>', '<title>{TITLE} | Blossom Boutique</title>')
header = header_match.group(1)
footer = footer_match.group(1)

def write_page(file_name, title, main_content):
    html = f"""<!DOCTYPE html>
<html lang="en" data-bs-theme="light">
{head.replace('{TITLE}', title)}
<body class="bg-light">
    {header}
    {main_content}
    {footer}
</html>"""
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created {file_name}")

pages = {
    'occasions.html': ('Occasions', '''
    <main class="py-5" style="background-color: var(--bs-secondary);">
        <div class="container text-center">
            <h1 class="display-4 fw-bold text-dark mb-4">Shop by Occasion</h1>
            <p class="lead text-dark opacity-75 mx-auto" style="max-width: 600px;">Every moment deserves beautiful blooms.</p>
            <div class="row g-4 mt-4">
                <div class="col-md-6 col-lg-3"><div class="card p-4 border-0 shadow-sm h-100 d-flex justify-content-center align-items-center"><a href="occasion-birthday.html" class="h5 fw-bold text-primary text-decoration-none stretched-link">Birthday</a></div></div>
                <div class="col-md-6 col-lg-3"><div class="card p-4 border-0 shadow-sm h-100 d-flex justify-content-center align-items-center"><a href="occasion-anniversary.html" class="h5 fw-bold text-primary text-decoration-none stretched-link">Anniversary</a></div></div>
                <div class="col-md-6 col-lg-3"><div class="card p-4 border-0 shadow-sm h-100 d-flex justify-content-center align-items-center"><a href="occasion-love.html" class="h5 fw-bold text-primary text-decoration-none stretched-link">Love & Romance</a></div></div>
                <div class="col-md-6 col-lg-3"><div class="card p-4 border-0 shadow-sm h-100 d-flex justify-content-center align-items-center"><a href="occasion-sympathy.html" class="h5 fw-bold text-primary text-decoration-none stretched-link">Sympathy</a></div></div>
            </div>
        </div>
    </main>
    '''),
    'occasion-birthday.html': ('Birthday Flowers', '<main class="py-5 bg-white min-vh-100 d-flex align-items-center"><div class="container text-center"><h1 class="display-4 fw-bold mb-4">Birthday Flowers</h1><p class="lead">Celebrate with vibrant, joyous arrangements.</p></div></main>'),
    'occasion-anniversary.html': ('Anniversary Flowers', '<main class="py-5 bg-white min-vh-100 d-flex align-items-center"><div class="container text-center"><h1 class="display-4 fw-bold mb-4">Anniversary Flowers</h1><p class="lead">Express your eternal love with absolute beauty.</p></div></main>'),
    'occasion-love.html': ('Love & Romance', '<main class="py-5 bg-white min-vh-100 d-flex align-items-center"><div class="container text-center"><h1 class="display-4 fw-bold mb-4">Love & Romance</h1><p class="lead">Deep reds, passionate pinks, and romantic gestures.</p></div></main>'),
    'occasion-sympathy.html': ('Sympathy Flowers', '<main class="py-5 bg-white min-vh-100 d-flex align-items-center"><div class="container text-center"><h1 class="display-4 fw-bold mb-4">Sympathy Flowers</h1><p class="lead">Gentle, white, and peaceful arrangements.</p></div></main>'),
    'shop-roses.html': ('Roses Collection', '<main class="py-5 bg-white min-vh-100 d-flex align-items-center"><div class="container text-center"><h1 class="display-4 fw-bold mb-4">Luxury Roses</h1><p class="lead">Handpicked, premium long-stemmed roses.</p></div></main>'),
    'shop-lilies.html': ('Lilies Collection', '<main class="py-5 bg-white min-vh-100 d-flex align-items-center"><div class="container text-center"><h1 class="display-4 fw-bold mb-4">Elegant Lilies</h1><p class="lead">Stargazers, calls, and majestic pure lilies.</p></div></main>'),
    'shop-mixed.html': ('Mixed Bouquets', '<main class="py-5 bg-white min-vh-100 d-flex align-items-center"><div class="container text-center"><h1 class="display-4 fw-bold mb-4">Mixed Bouquets</h1><p class="lead">A colorful celebration of seasonal favorites.</p></div></main>'),
    'gallery.html': ('Floral Gallery', '''
    <main class="py-5 bg-light min-vh-100">
        <div class="container text-center">
            <h1 class="display-4 fw-bold mb-4">Floral Gallery</h1>
            <p class="lead mb-5 mx-auto">Get inspired by our latest masterful creations.</p>
            <div class="row g-4">
                <div class="col-md-4"><img src="https://images.unsplash.com/photo-1542475141-94572227d81a?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" class="img-fluid rounded-4 shadow-sm w-100 object-fit-cover" style="height: 300px;"></div>
                <div class="col-md-4"><img src="https://images.unsplash.com/photo-1523694576722-cbaec25026df?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" class="img-fluid rounded-4 shadow-sm w-100 object-fit-cover" style="height: 300px;"></div>
                <div class="col-md-4"><img src="https://images.unsplash.com/photo-1457089328109-e5d9bd49f563?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" class="img-fluid rounded-4 shadow-sm w-100 object-fit-cover" style="height: 300px;"></div>
                <div class="col-md-4"><img src="https://images.unsplash.com/photo-1563241598-a28a304e2808?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" class="img-fluid rounded-4 shadow-sm w-100 object-fit-cover" style="height: 300px;"></div>
                <div class="col-md-4"><img src="https://images.unsplash.com/photo-1463936575829-25148e1db1b8?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" class="img-fluid rounded-4 shadow-sm w-100 object-fit-cover" style="height: 300px;"></div>
                <div class="col-md-4"><img src="https://images.unsplash.com/photo-1510265696660-f1406dc042b5?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" class="img-fluid rounded-4 shadow-sm w-100 object-fit-cover" style="height: 300px;"></div>
            </div>
        </div>
    </main>
    ''')
}

# Only create if Missing
for fname, (title, content) in pages.items():
    write_page(fname, title, content)

# Check if product.html exists and rename it
if os.path.exists('product.html') and not os.path.exists('product-detail.html'):
    os.rename('product.html', 'product-detail.html')
    print("Renamed product.html to product-detail.html")
