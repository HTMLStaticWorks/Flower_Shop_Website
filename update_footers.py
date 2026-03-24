import os
import re

new_footer_cols = """                <div class="col-6 col-md-4 col-lg-2">
                    <h4 class="h6 fw-bold mb-3 text-dark">Company</h4>
                    <ul class="list-unstyled mb-0 d-flex flex-column gap-2 small">
                        <li><a href="about.html" class="text-muted text-decoration-none text-primary-hover">About Us</a></li>
                        <li><a href="contact.html" class="text-muted text-decoration-none text-primary-hover">Contact Us</a></li>
                        <li><a href="gallery.html" class="text-muted text-decoration-none text-primary-hover">Our Gallery</a></li>
                        <li><a href="occasions.html" class="text-muted text-decoration-none text-primary-hover">Occasions</a></li>
                    </ul>
                </div>
                <div class="col-6 col-md-4 col-lg-2">
                    <h4 class="h6 fw-bold mb-3 text-dark">Quick Links</h4>
                    <ul class="list-unstyled mb-0 d-flex flex-column gap-2 small">
                        <li><a href="shop.html" class="text-muted text-decoration-none text-primary-hover">Shop All Flowers</a></li>
                        <li><a href="shop-roses.html" class="text-muted text-decoration-none text-primary-hover">Roses Collection</a></li>
                        <li><a href="login.html" class="text-muted text-decoration-none text-primary-hover">My Account</a></li>
                        <li><a href="register.html" class="text-muted text-decoration-none text-primary-hover">Register</a></li>
                    </ul>
                </div>"""

# Find the generic Company and Support columns
# The pattern spans from <div class="col-6 col-md-4 col-lg-2"> with "Company" down to the end of the "Support" column's closing </div>
# Since the spaces/newlines might differ, we can use a robust regex.

pattern = re.compile(
    r'<div class="col-6 col-md-4 col-lg-2">\s*<h4[^>]*>Company</h4>.*?</ul\s*>\s*</div\s*>\s*<div class="col-6 col-md-4 col-lg-2">\s*<h4[^>]*>Support</h4>.*?</ul\s*>\s*</div\s*>',
    re.DOTALL | re.IGNORECASE
)

count = 0
for file in os.listdir('.'):
    if not file.endswith('.html'): continue
    
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    new_html = pattern.sub(new_footer_cols, html)
    
    if new_html != html:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        count += 1
        print(f"Updated footer in {file}")

print(f"Total files updated: {count}")
