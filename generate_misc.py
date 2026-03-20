import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header, footer, head
head_match = re.search(r'(<head>.*?</head>)', index_content, re.DOTALL)
header_match = re.search(r'(<header.*?</header>)', index_content, re.DOTALL)
footer_match = re.search(r'(<footer.*?</body>)', index_content, re.DOTALL)

if not (head_match and header_match and footer_match):
    print("Could not extract templates.")
    exit(1)

head = head_match.group(1).replace('<title>Blossom Boutique | Premium Floral Services</title>', '<title>{TITLE} | Blossom Boutique</title>')
header = header_match.group(1)
footer = footer_match.group(1)

def construct_page(title, active_file, main_content):
    h = header.replace('class="nav-link active"', 'class="nav-link"')
    h = h.replace(f'href="{active_file}"', f'href="{active_file}" class="active"')
    # Add active class back correctly
    h = h.replace(f'class="nav-link" class="active"', f'class="nav-link active"')
    
    html = f"""<!DOCTYPE html>
<html lang="en" data-bs-theme="light">
{head.replace('{TITLE}', title)}
<body class="bg-light">
    {h}
    {main_content}
    {footer}
</html>"""
    return html

# 1. Shop
shop_main = """
    <main>
        <section class="py-5" style="background-color: var(--bs-secondary);">
            <div class="container text-center">
                <h1 class="display-4 fw-bold mb-3 text-dark">Our Collections</h1>
                <p class="lead text-dark opacity-75 mx-auto" style="max-width: 600px;">Find the perfect arrangement for any occasion, handcrafted with love and the freshest blooms.</p>
            </div>
        </section>

        <section class="section-padding bg-light">
            <div class="container">
                <div class="row g-5">
                    <aside class="col-lg-3">
                        <div class="card border-0 shadow-sm p-4">
                            <h2 class="h5 fw-bold mb-4"><i class="bi bi-funnel text-primary me-2"></i> Filters</h2>
                            <div class="mb-4">
                                <h3 class="h6 fw-bold mb-3">By Occasion</h3>
                                <div class="form-check mb-2"><input class="form-check-input" type="checkbox" checked id="occ1"><label class="form-check-label" for="occ1">All Occasions</label></div>
                                <div class="form-check mb-2"><input class="form-check-input" type="checkbox" id="occ2"><label class="form-check-label" for="occ2">Birthday</label></div>
                                <div class="form-check mb-2"><input class="form-check-input" type="checkbox" id="occ3"><label class="form-check-label" for="occ3">Anniversary</label></div>
                            </div>
                            <button class="btn btn-outline-primary w-100">Apply Filters</button>
                        </div>
                    </aside>

                    <div class="col-lg-9">
                        <div class="row g-4">
                            <!-- Items -->
                            <div class="col-md-6 col-lg-4">
                                <div class="card border-0 shadow-sm h-100 product-card">
                                    <img src="https://images.unsplash.com/photo-1542475141-94572227d81a?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" class="card-img-top object-fit-cover" style="height: 250px;" alt="...">
                                    <div class="card-body p-4 d-flex flex-column">
                                        <div class="d-flex justify-content-between align-items-center mb-1">
                                            <h3 class="h5 fw-bold mb-0">Classic Red</h3>
                                            <span class="text-primary fw-bold">$65.00</span>
                                        </div>
                                        <p class="text-muted small mb-3">Anniversary, Romance</p>
                                        <a href="product.html" class="btn btn-outline-primary mt-auto w-100">View Options</a>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="col-md-6 col-lg-4">
                                <div class="card border-0 shadow-sm h-100 product-card">
                                    <div class="position-absolute top-0 start-0 m-3"><span class="badge bg-primary px-3 py-2 rounded-pill">Bestseller</span></div>
                                    <img src="https://images.unsplash.com/photo-1523694576722-cbaec25026df?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" class="card-img-top object-fit-cover" style="height: 250px;" alt="...">
                                    <div class="card-body p-4 d-flex flex-column">
                                        <div class="d-flex justify-content-between align-items-center mb-1">
                                            <h3 class="h5 fw-bold mb-0">Pastel Dreams</h3>
                                            <span class="text-primary fw-bold">$85.00</span>
                                        </div>
                                        <p class="text-muted small mb-3">Birthday, Everyday</p>
                                        <a href="product.html" class="btn btn-outline-primary mt-auto w-100">View Options</a>
                                    </div>
                                </div>
                            </div>

                            <div class="col-md-6 col-lg-4">
                                <div class="card border-0 shadow-sm h-100 product-card">
                                    <img src="https://images.unsplash.com/photo-1457089328109-e5d9bd49f563?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" class="card-img-top object-fit-cover" style="height: 250px;" alt="...">
                                    <div class="card-body p-4 d-flex flex-column">
                                        <div class="d-flex justify-content-between align-items-center mb-1">
                                            <h3 class="h5 fw-bold mb-0">Sunshine Yellow</h3>
                                            <span class="text-primary fw-bold">$55.00</span>
                                        </div>
                                        <p class="text-muted small mb-3">Birthday, Sympathy</p>
                                        <a href="product.html" class="btn btn-outline-primary mt-auto w-100">View Options</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
"""

# 2. Product
prod_main = """
    <main class="py-5 bg-white">
        <div class="container">
            <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                    <li class="breadcrumb-item"><a href="index.html" class="text-decoration-none text-muted">Home</a></li>
                    <li class="breadcrumb-item"><a href="shop.html" class="text-decoration-none text-muted">Shop</a></li>
                    <li class="breadcrumb-item active" aria-current="page">Pastel Dreams</li>
                </ol>
            </nav>

            <div class="row gy-5 mt-2">
                <div class="col-lg-6">
                    <img src="https://images.unsplash.com/photo-1523694576722-cbaec25026df?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" class="img-fluid rounded-4 shadow-sm w-100" alt="Product Image">
                </div>
                
                <div class="col-lg-6">
                    <div class="ps-lg-4">
                        <span class="badge bg-primary bg-opacity-10 text-primary mb-2 px-3 py-2 rounded-pill">Bestseller</span>
                        <h1 class="display-5 fw-bold mb-2">Pastel Dreams</h1>
                        <p class="fs-3 fw-bold text-primary mb-4">$85.00</p>
                        <p class="text-muted mb-4">A gentle, soothing arrangement of premium pastel roses, soft pink lisianthus, and fresh eucalyptus. Perfect for celebrating a birthday or welcoming a new baby.</p>
                        
                        <div class="mb-4">
                            <label class="form-label fw-bold">Size Options</label>
                            <div class="d-flex gap-2">
                                <input type="radio" class="btn-check" name="size" id="size1" autocomplete="off" checked>
                                <label class="btn btn-outline-primary" for="size1">Standard</label>
                                
                                <input type="radio" class="btn-check" name="size" id="size2" autocomplete="off">
                                <label class="btn btn-outline-primary" for="size2">Deluxe (+$20)</label>
                                
                                <input type="radio" class="btn-check" name="size" id="size3" autocomplete="off">
                                <label class="btn btn-outline-primary" for="size3">Premium (+$40)</label>
                            </div>
                        </div>

                        <a href="checkout.html" class="btn btn-primary btn-lg w-100 mb-3"><i class="bi bi-cart-plus me-2"></i> Customize & Add to Cart</a>
                    </div>
                </div>
            </div>
        </div>
    </main>
"""

# 3. 404
four_main = """
    <main class="min-vh-100 d-flex align-items-center justify-content-center py-5 text-center bg-white">
        <div class="container">
            <h1 class="display-1 fw-bold text-primary mb-3">404</h1>
            <h2 class="h3 fw-bold mb-4">Oops! The flower you're looking for hasn't bloomed yet.</h2>
            <p class="text-muted lead mb-5 mx-auto" style="max-width: 500px;">The page you are trying to visit does not exist or has been moved.</p>
            <a href="index.html" class="btn btn-primary btn-lg px-4">Back to Home</a>
        </div>
    </main>
"""

# 4. Coming Soon
cs_main = """
    <main class="min-vh-100 d-flex align-items-center justify-content-center py-5 text-center" style="background-color: var(--bs-secondary);">
        <div class="container">
            <h1 class="display-3 fw-bold text-dark mb-4">Great Things Are Sprouting</h1>
            <p class="lead text-dark opacity-75 mb-5 mx-auto" style="max-width: 600px;">We're currently working on this feature. Please check back soon!</p>
            <a href="index.html" class="btn btn-primary btn-lg px-4">Return Home</a>
        </div>
    </main>
"""

with open('shop.html', 'w', encoding='utf-8') as f:
    f.write(construct_page('Shop', 'shop.html', shop_main))

with open('product.html', 'w', encoding='utf-8') as f:
    f.write(construct_page('Product', 'product.html', prod_main))

with open('404.html', 'w', encoding='utf-8') as f:
    f.write(construct_page('Page Not Found', '404.html', four_main))

with open('coming-soon.html', 'w', encoding='utf-8') as f:
    f.write(construct_page('Coming Soon', 'coming-soon.html', cs_main))

print("All peripheral pages overwritten and styled successfully!")
