import re
import os

filepath = r"e:\OfficeDownloads_\MarchWebsites\Flower_Shop_Website\home-2.html"

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Hero Section
hero_orig = """<section class="py-5 py-lg-7 hero-section" style="background-color: var(--bs-secondary);">
            <div class="container">
                <div class="row align-items-center gy-5">
                    <div class="col-lg-6 text-center text-lg-start">
                        <h1 class="display-3 fw-bold mb-4 text-dark">Modern Floral Masterpieces</h1>
                        <p class="lead opacity-75 text-dark mb-5">Beautiful, hand-crafted floral arrangements for every
                            special moment. Bringing joy to your loved ones with our fresh blooms.</p>
                        <div class="d-flex flex-wrap gap-3 justify-content-center justify-content-lg-start">
                            <a href="shop.html" class="btn btn-primary btn-lg px-4 border-0">Order Now</a>
                            <a href="occasions.html" class="btn btn-outline-dark btn-lg px-4 fw-bold">Explore
                                Occasions</a>
                        </div>
                    </div>
                    <div class="col-lg-6 text-center position-relative">
                        <img src="assets/images/hero.jpg" alt="Beautiful flower arrangement"
                            class="img-fluid rounded-4 shadow-lg w-100"
                            style="aspect-ratio: 4/3; object-fit: cover; max-width: 500px;">
                    </div>
                </div>
            </div>
        </section>"""
hero_new = """<section class="py-5 py-lg-7 hero-section position-relative overflow-hidden bg-modern-soft">
            <div class="container position-relative" style="z-index: 2;">
                <div class="row align-items-center gy-5">
                    <div class="col-lg-6 text-center text-lg-start">
                        <span class="badge bg-modern-gradient text-white px-3 py-2 rounded-pill shadow-sm mb-3 animate-fade-in-up">New Collection</span>
                        <h1 class="display-3 fw-bold mb-4 text-dark animate-fade-in-up delay-1"><span class="text-gradient">Modern Floral</span> Masterpieces</h1>
                        <p class="lead opacity-75 text-dark mb-5 animate-fade-in-up delay-2">Beautiful, hand-crafted floral arrangements for every special moment. Bringing joy to your loved ones with our fresh blooms.</p>
                        <div class="d-flex flex-wrap gap-3 justify-content-center justify-content-lg-start animate-fade-in-up delay-3">
                            <a href="shop.html" class="btn btn-primary btn-lg px-4 border-0 shadow-sm">Order Now</a>
                            <a href="occasions.html" class="btn btn-outline-primary btn-lg px-4 fw-bold bg-white shadow-sm">Explore Occasions</a>
                        </div>
                    </div>
                    <div class="col-lg-6 text-center position-relative animate-fade-in-right delay-2">
                        <div class="position-absolute rounded-circle bg-modern-gradient opacity-25 translate-middle" style="width: 400px; height: 400px; top: 50%; left: 50%; filter: blur(60px); z-index: -1;"></div>
                        <img src="assets/images/hero.jpg" alt="Beautiful flower arrangement"
                            class="img-fluid rounded-4 shadow-lg w-100 animate-breathe"
                            style="aspect-ratio: 4/3; object-fit: cover; max-width: 500px; border: 8px solid rgba(255,255,255,0.8);">
                    </div>
                </div>
            </div>
        </section>"""
html = html.replace(hero_orig, hero_new)

# 2. Features Section
features_orig = """<section class="py-5 bg-white border-bottom">
            <div class="container">
                <div class="row g-4 text-center">
                    <div class="col-md-4">
                        <div class="p-4"><i class="bi bi-truck display-4 text-primary mb-3"></i>
                            <h3 class="h5 fw-bold">Same-Day Delivery</h3>
                            <p class="text-muted text-sm">Order before 4 PM for fast delivery.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-4"><i class="bi bi-flower1 display-4 text-primary mb-3"></i>
                            <h3 class="h5 fw-bold">Farm Fresh Blooms</h3>
                            <p class="text-muted text-sm">Sourced directly from local farms.</p>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="p-4"><i class="bi bi-heart display-4 text-primary mb-3"></i>
                            <h3 class="h5 fw-bold">100% Satisfaction</h3>
                            <p class="text-muted text-sm">We guarantee perfectly arranged bouquets.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""
features_new = """<section class="py-5 bg-modern-soft border-bottom position-relative">
            <div class="container position-relative" style="z-index: 2;">
                <div class="row g-4 text-center">
                    <div class="col-md-4 animate-fade-in-up delay-1">
                        <div class="p-4 glass-panel modern-card-hover h-100 text-center">
                            <div class="bg-white text-primary d-inline-flex justify-content-center align-items-center rounded-circle mb-3 shadow-sm" style="width: 80px; height: 80px;">
                                <i class="bi bi-truck display-5 mb-0"></i>
                            </div>
                            <h3 class="h5 fw-bold">Same-Day Delivery</h3>
                            <p class="text-muted text-sm mb-0">Order before 4 PM for fast delivery.</p>
                        </div>
                    </div>
                    <div class="col-md-4 animate-fade-in-up delay-2">
                        <div class="p-4 glass-panel modern-card-hover h-100 text-center">
                            <div class="bg-white text-primary d-inline-flex justify-content-center align-items-center rounded-circle mb-3 shadow-sm" style="width: 80px; height: 80px;">
                                <i class="bi bi-flower1 display-5 mb-0"></i>
                            </div>
                            <h3 class="h5 fw-bold">Farm Fresh Blooms</h3>
                            <p class="text-muted text-sm mb-0">Sourced directly from local farms.</p>
                        </div>
                    </div>
                    <div class="col-md-4 animate-fade-in-up delay-3">
                        <div class="p-4 glass-panel modern-card-hover h-100 text-center">
                            <div class="bg-white text-primary d-inline-flex justify-content-center align-items-center rounded-circle mb-3 shadow-sm" style="width: 80px; height: 80px;">
                                <i class="bi bi-heart display-5 mb-0"></i>
                            </div>
                            <h3 class="h5 fw-bold">100% Satisfaction</h3>
                            <p class="text-muted text-sm mb-0">We guarantee perfectly arranged bouquets.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""
html = html.replace(features_orig, features_new)

# 3. Occasions Section
occasions_orig = """<section class="section-padding bg-light">
            <div class="container">
                <div class="text-center mb-5">
                    <h2 class="display-5 fw-bold mb-3">Shop by Occasion</h2>
                </div>
                <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4 g-4 justify-content-center">
                    <div class="col"><a href="occasion-birthday.html"
                            class="card h-100 text-decoration-none border-0 shadow-sm text-center">
                            <div class="card-body py-5">
                                <h3 class="h4 card-title fw-bold text-dark">Birthday</h3>
                            </div>
                        </a></div>
                    <div class="col"><a href="occasion-anniversary.html"
                            class="card h-100 text-decoration-none border-0 shadow-sm text-center">
                            <div class="card-body py-5">
                                <h3 class="h4 card-title fw-bold text-dark">Anniversary</h3>
                            </div>
                        </a></div>
                    <div class="col"><a href="occasion-love.html"
                            class="card h-100 text-decoration-none border-0 shadow-sm text-center">
                            <div class="card-body py-5">
                                <h3 class="h4 card-title fw-bold text-dark">Romance</h3>
                            </div>
                        </a></div>
                    <div class="col"><a href="occasion-sympathy.html"
                            class="card h-100 text-decoration-none border-0 shadow-sm text-center">
                            <div class="card-body py-5">
                                <h3 class="h4 card-title fw-bold text-dark">Sympathy</h3>
                            </div>
                        </a></div>
                </div>
            </div>
        </section>"""
occasions_new = """<section class="section-padding bg-white">
            <div class="container">
                <div class="text-center mb-5 animate-fade-in-up">
                    <h2 class="display-5 fw-bold mb-3 text-gradient pb-1">Shop by Occasion</h2>
                    <p class="text-muted">Find the perfect arrangement for any celebration.</p>
                </div>
                <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-4 g-4 justify-content-center">
                    <div class="col animate-fade-in-up delay-1"><a href="occasion-birthday.html"
                            class="card h-100 text-decoration-none border-0 shadow-sm text-center occasion-card-1 modern-card-hover">
                            <div class="card-body py-5 d-flex align-items-center justify-content-center">
                                <h3 class="h4 card-title fw-bold text-dark mb-0">Birthday</h3>
                            </div>
                        </a></div>
                    <div class="col animate-fade-in-up delay-2"><a href="occasion-anniversary.html"
                            class="card h-100 text-decoration-none border-0 shadow-sm text-center occasion-card-2 modern-card-hover">
                            <div class="card-body py-5 d-flex align-items-center justify-content-center">
                                <h3 class="h4 card-title fw-bold text-dark mb-0">Anniversary</h3>
                            </div>
                        </a></div>
                    <div class="col animate-fade-in-up delay-3"><a href="occasion-love.html"
                            class="card h-100 text-decoration-none border-0 shadow-sm text-center occasion-card-3 modern-card-hover">
                            <div class="card-body py-5 d-flex align-items-center justify-content-center">
                                <h3 class="h4 card-title fw-bold text-dark mb-0">Romance</h3>
                            </div>
                        </a></div>
                    <div class="col animate-fade-in-up delay-4"><a href="occasion-sympathy.html"
                            class="card h-100 text-decoration-none border-0 shadow-sm text-center occasion-card-4 modern-card-hover">
                            <div class="card-body py-5 d-flex align-items-center justify-content-center">
                                <h3 class="h4 card-title fw-bold text-dark mb-0">Sympathy</h3>
                            </div>
                        </a></div>
                </div>
            </div>
        </section>"""
html = html.replace(occasions_orig, occasions_new)

# 4. Bestsellers cards replacements using Regex to catch all 10 cards easily
# Replace Bestsellers Heading
bestsellers_heading_orig = """<h2 class="display-5 fw-bold mb-3">Featured Bestsellers</h2>"""
bestsellers_heading_new = """<h2 class="display-5 fw-bold mb-3 text-gradient pb-1">Featured Bestsellers</h2>"""
html = html.replace(bestsellers_heading_orig, bestsellers_heading_new)

# Add glass-panel and modern-card-hover to product-card
html = re.sub(
    r'class="card border-0 shadow-sm h-100 product-card"',
    r'class="card border-0 shadow-sm h-100 product-card modern-card-hover glass-panel"',
    html
)
# Update badges
html = re.sub(
    r'<span\s+class="badge bg-primary px-3 py-2 rounded-pill shadow-sm">Popular</span>',
    r'<span class="rounded-pill-badge bg-modern-gradient text-white shadow-sm">Popular</span>',
    html
)

# 5. Newsletter Section
newsletter_orig = """<section class="py-5 bg-primary text-white text-center">
            <div class="container py-4">
                <h2 class="display-5 fw-bold mb-3 text-white">Join the Blossom Club</h2>
                <p class="lead mb-4 mx-auto text-white opacity-75" style="max-width:600px;">Sign up today and get 15%
                    off your first luxury arrangement.</p>
                <div class="d-flex justify-content-center"><a href="register.html"
                        class="btn btn-light btn-lg px-5 fw-bold border-0 text-primary rounded-pill shadow">Sign Up
                        Now</a></div>
            </div>
        </section>"""
newsletter_new = """<section class="py-5 bg-modern-gradient text-white text-center position-relative overflow-hidden">
            <div class="position-absolute" style="background: rgba(255,255,255,0.1); width: 300px; height: 300px; border-radius: 50%; top: -100px; left: -100px; filter: blur(30px);"></div>
            <div class="position-absolute" style="background: rgba(255,255,255,0.1); width: 250px; height: 250px; border-radius: 50%; bottom: -100px; right: -50px; filter: blur(40px);"></div>
            <div class="container py-5 position-relative animate-fade-in-up" style="z-index:2;">
                <h2 class="display-5 fw-bold mb-3 text-white">Join the Blossom Club</h2>
                <p class="lead mb-4 mx-auto text-white opacity-90" style="max-width:600px;">Sign up today and get 15% off your first luxury arrangement.</p>
                <div class="d-flex justify-content-center">
                    <a href="register.html" class="btn btn-light btn-lg px-5 fw-bold border-0 text-primary rounded-pill shadow-lg modern-card-hover">Sign Up Now</a>
                </div>
            </div>
        </section>"""
html = html.replace(newsletter_orig, newsletter_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated successfully")
