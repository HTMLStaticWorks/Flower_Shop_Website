import os
import re

# 1. Rebuild occasions.html using about.html as a template for header/footer
with open('about.html', 'r', encoding='utf-8') as f:
    about = f.read()

header_end = about.find('</header>') + len('</header>')
header = about[:header_end]
# Fix the title in header
header = header.replace('<title>About Us | Blossom Boutique</title>', '<title>Shop Occasions | Blossom Boutique</title>')

footer_start = about.find('<footer')
footer = about[footer_start:]

main_content = """
    <main class="bg-light">
        <!-- Hero Section -->
        <section class="py-5 position-relative overflow-hidden" style="background: linear-gradient(135deg, rgba(var(--bs-primary-rgb), 0.05) 0%, rgba(var(--bs-secondary-rgb), 0.05) 100%);">
            <div class="position-absolute top-0 start-0 translate-middle rounded-circle bg-primary opacity-10 animate-breathe" style="width: 400px; height: 400px; filter: blur(60px);"></div>
            <div class="position-absolute bottom-0 end-0 translate-middle rounded-circle bg-info opacity-10 animate-breathe delay-2" style="width: 300px; height: 300px; filter: blur(50px);"></div>
            
            <div class="container text-center position-relative z-1 glass-panel py-5 px-3 animate-fade-in-up" style="max-width: 800px; border-radius: 20px;">
                <h1 class="display-4 fw-bold mb-3 text-primary">Shop by Occasion</h1>
                <p class="lead text-muted mx-auto mb-0" style="max-width: 600px;">Every moment deserves beautiful blooms. Browse our curated collections for your special celebrations all in one place.</p>
            </div>
        </section>

        <!-- Birthday Section -->
        <section id="birthday" class="py-5 bg-white border-bottom pt-5" style="scroll-margin-top: 80px;">
            <div class="container" style="max-width: 1000px;">
                <div class="d-flex align-items-center mb-5">
                    <h2 class="h1 fw-bold mb-0 text-dark">Birthday</h2>
                    <div class="ms-4 flex-grow-1 border-top border-2 border-primary opacity-25"></div>
                </div>
                <div class="row row-cols-1 row-cols-sm-2 g-5">
                    <div class="col">
                        <div class="card border-0 shadow-sm h-100 product-card modern-card-hover animate-fade-in-up">
                            <div class="position-absolute top-0 start-0 m-3"><span class="badge bg-primary px-3 py-2 rounded-pill shadow-sm">Popular</span></div>
                            <img src="assets/images/products/flower-3.jpg" class="card-img-top object-fit-cover" style="aspect-ratio: 4/3;" alt="Birthday Brights">
                            <div class="card-body p-4 d-flex flex-column">
                                <div class="d-flex justify-content-between align-items-center mb-1">
                                    <h3 class="h5 fw-bold mb-0 text-dark">Birthday Brights</h3>
                                    <span class="text-primary fw-bold fs-5">$60</span>
                                </div>
                                <p class="text-muted small mb-4">Vibrant mixing for a perfect celebration</p>
                                <a href="product-detail.html" class="btn btn-outline-primary mt-auto w-100 py-2">View Details</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card border-0 shadow-sm h-100 product-card modern-card-hover animate-fade-in-up delay-1">
                            <img src="assets/images/products/flower-8.jpg" class="card-img-top object-fit-cover" style="aspect-ratio: 4/3;" alt="Pastel Party">
                            <div class="card-body p-4 d-flex flex-column">
                                <div class="d-flex justify-content-between align-items-center mb-1">
                                    <h3 class="h5 fw-bold mb-0 text-dark">Pastel Party</h3>
                                    <span class="text-primary fw-bold fs-5">$55</span>
                                </div>
                                <p class="text-muted small mb-4">Soft colors to brighten their day</p>
                                <a href="product-detail.html" class="btn btn-outline-primary mt-auto w-100 py-2">View Details</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Anniversary Section -->
        <section id="anniversary" class="py-5 bg-light border-bottom pt-5" style="scroll-margin-top: 80px;">
            <div class="container" style="max-width: 1000px;">
                <div class="d-flex align-items-center mb-5">
                    <h2 class="h1 fw-bold mb-0 text-dark">Anniversary</h2>
                    <div class="ms-4 flex-grow-1 border-top border-2 border-primary opacity-25"></div>
                </div>
                <div class="row row-cols-1 row-cols-sm-2 g-5">
                    <div class="col">
                        <div class="card border-0 shadow-sm h-100 product-card modern-card-hover animate-fade-in-up">
                            <div class="position-absolute top-0 start-0 m-3"><span class="badge bg-primary px-3 py-2 rounded-pill shadow-sm">Bestseller</span></div>
                            <img src="assets/images/products/flower-6.jpg" class="card-img-top object-fit-cover" style="aspect-ratio: 4/3;" alt="Eternal Love">
                            <div class="card-body p-4 d-flex flex-column">
                                <div class="d-flex justify-content-between align-items-center mb-1">
                                    <h3 class="h5 fw-bold mb-0 text-dark">Eternal Love</h3>
                                    <span class="text-primary fw-bold fs-5">$85</span>
                                </div>
                                <p class="text-muted small mb-4">Classic long-stemmed arrangements</p>
                                <a href="product-detail.html" class="btn btn-outline-primary mt-auto w-100 py-2">View Details</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card border-0 shadow-sm h-100 product-card modern-card-hover animate-fade-in-up delay-1">
                            <img src="assets/images/products/flower-7.jpg" class="card-img-top object-fit-cover" style="aspect-ratio: 4/3;" alt="Golden Years">
                            <div class="card-body p-4 d-flex flex-column">
                                <div class="d-flex justify-content-between align-items-center mb-1">
                                    <h3 class="h5 fw-bold mb-0 text-dark">Golden Years</h3>
                                    <span class="text-primary fw-bold fs-5">$75</span>
                                </div>
                                <p class="text-muted small mb-4">Golden hues for lasting memories</p>
                                <a href="product-detail.html" class="btn btn-outline-primary mt-auto w-100 py-2">View Details</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Love & Romance Section -->
        <section id="love" class="py-5 bg-white border-bottom pt-5" style="scroll-margin-top: 80px;">
            <div class="container" style="max-width: 1000px;">
                <div class="d-flex align-items-center mb-5">
                    <h2 class="h1 fw-bold mb-0 text-dark">Love & Romance</h2>
                    <div class="ms-4 flex-grow-1 border-top border-2 border-primary opacity-25"></div>
                </div>
                <div class="row row-cols-1 row-cols-sm-2 g-5">
                    <div class="col">
                        <div class="card border-0 shadow-sm h-100 product-card modern-card-hover animate-fade-in-up">
                            <img src="assets/images/products/flower-0.jpg" class="card-img-top object-fit-cover" style="aspect-ratio: 4/3;" alt="Classic Red Roses">
                            <div class="card-body p-4 d-flex flex-column">
                                <div class="d-flex justify-content-between align-items-center mb-1">
                                    <h3 class="h5 fw-bold mb-0 text-dark">Classic Red Roses</h3>
                                    <span class="text-primary fw-bold fs-5">$65</span>
                                </div>
                                <p class="text-muted small mb-4">The ultimate romantic gesture</p>
                                <a href="product-detail.html" class="btn btn-outline-primary mt-auto w-100 py-2">View Details</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card border-0 shadow-sm h-100 product-card modern-card-hover animate-fade-in-up delay-1">
                            <img src="assets/images/products/flower-9.jpg" class="card-img-top object-fit-cover" style="aspect-ratio: 4/3;" alt="Passionate Pink">
                            <div class="card-body p-4 d-flex flex-column">
                                <div class="d-flex justify-content-between align-items-center mb-1">
                                    <h3 class="h5 fw-bold mb-0 text-dark">Passionate Pink</h3>
                                    <span class="text-primary fw-bold fs-5">$70</span>
                                </div>
                                <p class="text-muted small mb-4">Exquisite pink lilies and roses</p>
                                <a href="product-detail.html" class="btn btn-outline-primary mt-auto w-100 py-2">View Details</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Sympathy Section -->
        <section id="sympathy" class="py-5 bg-light border-bottom pt-5" style="scroll-margin-top: 80px;">
            <div class="container" style="max-width: 1000px;">
                <div class="d-flex align-items-center mb-5">
                    <h2 class="h1 fw-bold mb-0 text-dark">Sympathy</h2>
                    <div class="ms-4 flex-grow-1 border-top border-2 border-primary opacity-25"></div>
                </div>
                <div class="row row-cols-1 row-cols-sm-2 g-5">
                    <div class="col">
                        <div class="card border-0 shadow-sm h-100 product-card modern-card-hover animate-fade-in-up">
                            <img src="assets/images/products/flower-4.jpg" class="card-img-top object-fit-cover" style="aspect-ratio: 4/3;" alt="Peaceful White">
                            <div class="card-body p-4 d-flex flex-column">
                                <div class="d-flex justify-content-between align-items-center mb-1">
                                    <h3 class="h5 fw-bold mb-0 text-dark">Peaceful White Lily</h3>
                                    <span class="text-primary fw-bold fs-5">$80</span>
                                </div>
                                <p class="text-muted small mb-4">Express condolences with serenity</p>
                                <a href="product-detail.html" class="btn btn-outline-primary mt-auto w-100 py-2">View Details</a>
                            </div>
                        </div>
                    </div>
                    <div class="col">
                        <div class="card border-0 shadow-sm h-100 product-card modern-card-hover animate-fade-in-up delay-1">
                            <img src="assets/images/products/flower-10.jpg" class="card-img-top object-fit-cover" style="aspect-ratio: 4/3;" alt="Gentle Comfort" onerror="this.src='assets/images/products/flower-1.jpg'">
                            <div class="card-body p-4 d-flex flex-column">
                                <div class="d-flex justify-content-between align-items-center mb-1">
                                    <h3 class="h5 fw-bold mb-0 text-dark">Gentle Comfort</h3>
                                    <span class="text-primary fw-bold fs-5">$55</span>
                                </div>
                                <p class="text-muted small mb-4">Subtle colors for thoughtful care</p>
                                <a href="product-detail.html" class="btn btn-outline-primary mt-auto w-100 py-2">View Details</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
"""

with open('occasions.html', 'w', encoding='utf-8') as f:
    f.write(header + main_content + footer)
print("Rebuilt occasions.html.")

# 2. Update remaining links in index.html and other files to point to sections in occasions.html
patterns = {
    'occasion-birthday.html': 'occasions.html#birthday',
    'occasion-anniversary.html': 'occasions.html#anniversary',
    'occasion-love.html': 'occasions.html#love',
    'occasion-sympathy.html': 'occasions.html#sympathy'
}

for root, _, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.html'):
            path = os.path.join(root, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            changed = False
            for old, new in patterns.items():
                if old in content:
                    content = content.replace(old, new)
                    changed = True
            if changed:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated links in {filename}")

# 3. Delete old files
old_files = ['occasion-birthday.html', 'occasion-anniversary.html', 'occasion-love.html', 'occasion-sympathy.html']
for filename in old_files:
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename}")
