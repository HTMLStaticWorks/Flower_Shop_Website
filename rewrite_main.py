import re

filepath = r"e:\OfficeDownloads_\MarchWebsites\Flower_Shop_Website\home-2.html"

with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract from <main class="bg-light"> to </main>
main_pattern = re.compile(r'<main class="bg-light">.*?</main>', re.DOTALL)

new_main = """<main class="bg-light">
        <!-- 1. Hero Overlay Section -->
        <section class="position-relative d-flex align-items-center justify-content-center" style="min-height: 85vh; background: url('assets/images/hero.jpg') center/cover no-repeat;">
            <div class="position-absolute w-100 h-100 top-0 start-0 bg-dark opacity-50"></div>
            <div class="container position-relative text-center text-white animate-fade-in-up" style="z-index: 2;">
                <span class="badge bg-primary px-3 py-2 rounded-pill shadow-sm mb-3 text-uppercase tracking-wide">Modern Collection</span>
                <h1 class="display-1 fw-bold mb-4 text-white">The Art of Gifting</h1>
                <p class="lead mb-5 mx-auto text-white opacity-75" style="max-width: 600px;">Elevate your special moments with our exclusive, hand-crafted luxury floral arrangements.</p>
                <div class="d-flex justify-content-center gap-3">
                    <a href="shop.html" class="btn btn-primary btn-lg px-5 border-0 shadow">Shop Collection</a>
                </div>
            </div>
        </section>

        <!-- 2. Minimalist Categories (Circles) -->
        <section class="py-5 bg-white border-bottom position-relative" style="margin-top: -60px; z-index: 10;">
            <div class="container glass-panel shadow-sm px-4 py-5 mb-3" style="border-radius: 20px;">
                <div class="text-center mb-5 animate-fade-in-up">
                    <h2 class="h3 fw-bold text-dark mb-0">Browse by Collection</h2>
                </div>
                <div class="row g-4 justify-content-center text-center">
                    <div class="col-6 col-md-3 animate-fade-in-up delay-1">
                        <a href="shop-roses.html" class="text-decoration-none text-dark category-link">
                            <div class="rounded-circle overflow-hidden mb-3 mx-auto shadow-sm transition category-img" style="width: 130px; height: 130px;">
                                <img src="assets/images/products/flower-0.jpg" alt="Roses" class="w-100 h-100 object-fit-cover">
                            </div>
                            <h3 class="h6 fw-bold mb-0">Signature Roses</h3>
                        </a>
                    </div>
                    <div class="col-6 col-md-3 animate-fade-in-up delay-2">
                        <a href="shop-lilies.html" class="text-decoration-none text-dark category-link">
                            <div class="rounded-circle overflow-hidden mb-3 mx-auto shadow-sm transition category-img" style="width: 130px; height: 130px;">
                                <img src="assets/images/products/flower-9.jpg" alt="Lilies" class="w-100 h-100 object-fit-cover">
                            </div>
                            <h3 class="h6 fw-bold mb-0">Elegant Lilies</h3>
                        </a>
                    </div>
                    <div class="col-6 col-md-3 animate-fade-in-up delay-3">
                        <a href="shop-mixed.html" class="text-decoration-none text-dark category-link">
                            <div class="rounded-circle overflow-hidden mb-3 mx-auto shadow-sm transition category-img" style="width: 130px; height: 130px;">
                                <img src="assets/images/products/flower-4.jpg" alt="Mixed" class="w-100 h-100 object-fit-cover">
                            </div>
                            <h3 class="h6 fw-bold mb-0">Mixed Bouquets</h3>
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. Spotlight / Highlighted Product -->
        <section class="py-0 bg-light overflow-hidden mt-5">
            <div class="container">
                <div class="row g-0 align-items-center bg-white rounded-4 shadow-sm overflow-hidden">
                    <div class="col-lg-6 animate-fade-in-right">
                        <img src="assets/images/products/flower-6.jpg" alt="Velvet Romance" class="img-fluid w-100" style="object-fit: cover; min-height: 450px;">
                    </div>
                    <div class="col-lg-6 px-5 py-5 py-lg-0 text-center text-lg-start animate-fade-in-up delay-2">
                        <div class="mx-auto mx-lg-0 px-lg-4" style="max-width: 450px;">
                            <span class="text-primary fw-bold text-uppercase tracking-wide small mb-2 d-block">Spotlight</span>
                            <h2 class="display-6 fw-bold mb-4 text-dark">Velvet Romance</h2>
                            <p class="text-muted mb-4">A breathtaking composition of deep red velvety blooms, perfectly curated to express profound passion and timeless elegance.</p>
                            <a href="product-detail.html" class="btn btn-outline-primary px-4 rounded-pill">View Details</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. Trending Now (3-col layout) -->
        <section class="py-5 py-lg-7 bg-light mt-4">
            <div class="container">
                <div class="d-flex flex-column flex-md-row justify-content-between align-items-center mb-5 animate-fade-in-up">
                    <h2 class="display-6 fw-bold text-dark mb-0">Trending Now</h2>
                    <a href="shop.html" class="text-primary text-decoration-none fw-bold mt-3 mt-md-0 btn-link">View All Products <i class="bi bi-arrow-right"></i></a>
                </div>
                <div class="row row-cols-1 row-cols-md-3 g-4">
                    <div class="col animate-fade-in-up delay-1">
                        <div class="card h-100 border-0 shadow-sm product-card modern-card-hover rounded-4">
                            <img src="assets/images/products/flower-7.jpg" alt="Morning Dew" class="card-img-top rounded-top-4" style="aspect-ratio: 1/1; object-fit: cover;">
                            <div class="card-body p-4 text-center">
                                <h3 class="h5 fw-bold mb-1 text-dark">Morning Dew</h3>
                                <p class="text-muted small mb-3">Fresh & Vibrant</p>
                                <span class="text-primary fw-bold fs-5 d-block mb-3">$95.00</span>
                            </div>
                        </div>
                    </div>
                    <div class="col animate-fade-in-up delay-2">
                        <div class="card h-100 border-0 shadow-sm product-card modern-card-hover rounded-4 position-relative">
                            <div class="position-absolute top-0 start-0 m-3"><span class="badge bg-primary px-3 py-2 rounded-pill shadow-sm">Bestseller</span></div>
                            <img src="assets/images/products/flower-2.jpg" alt="Sunshine Yellow" class="card-img-top rounded-top-4" style="aspect-ratio: 1/1; object-fit: cover;">
                            <div class="card-body p-4 text-center">
                                <h3 class="h5 fw-bold mb-1 text-dark">Sunshine Yellow</h3>
                                <p class="text-muted small mb-3">Bright & Cheerful</p>
                                <span class="text-primary fw-bold fs-5 d-block mb-3">$70.00</span>
                            </div>
                        </div>
                    </div>
                    <div class="col animate-fade-in-up delay-3">
                        <div class="card h-100 border-0 shadow-sm product-card modern-card-hover rounded-4">
                            <img src="assets/images/products/flower-5.jpg" alt="Blush Peony" class="card-img-top rounded-top-4" style="aspect-ratio: 1/1; object-fit: cover;">
                            <div class="card-body p-4 text-center">
                                <h3 class="h5 fw-bold mb-1 text-dark">Blush Peony Dream</h3>
                                <p class="text-muted small mb-3">Soft & Romantic</p>
                                <span class="text-primary fw-bold fs-5 d-block mb-3">$85.00</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. Testimonials Section -->
        <section class="py-5 bg-white border-top">
            <div class="container py-4 text-center animate-fade-in-up">
                <i class="bi bi-star-fill text-primary mb-3 display-6 d-block"></i>
                <blockquote class="blockquote mx-auto mb-4" style="max-width: 700px;">
                    <p class="h4 fw-normal lh-base text-dark text-center">"The most exquisite flowers I have ever received. The arrangement was phenomenal, fresh, and delivered right on time. Highly recommended!"</p>
                </blockquote>
                <figcaption class="blockquote-footer fs-6 mt-0">
                    Sarah Jenkins, <cite title="Source Title">Verified Buyer</cite>
                </figcaption>
            </div>
        </section>
    </main>"""

html = main_pattern.sub(new_main, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated home-2.html main block successfully.")
