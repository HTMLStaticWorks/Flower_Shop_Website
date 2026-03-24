import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

new_nav = """<ul class="navbar-nav mx-lg-auto mb-4 mb-lg-0 align-items-lg-center gap-lg-3 fs-5 fs-lg-6">
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="index.html" id="homeDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">Home</a>
        <ul class="dropdown-menu border-0 shadow-sm" aria-labelledby="homeDropdown">
            <li><a class="dropdown-item" href="index.html">Classic Home</a></li>
            <li><a class="dropdown-item" href="home-2.html">Modern Home</a></li>
        </ul>
    </li>
    
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="occasions.html" id="occasionsDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">Occasions</a>
        <ul class="dropdown-menu border-0 shadow-sm" aria-labelledby="occasionsDropdown">
            <li><a class="dropdown-item fw-bold text-primary" href="occasions.html">View All Occasions</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="occasion-birthday.html">Birthday</a></li>
            <li><a class="dropdown-item" href="occasion-anniversary.html">Anniversary</a></li>
            <li><a class="dropdown-item" href="occasion-love.html">Love & Romance</a></li>
            <li><a class="dropdown-item" href="occasion-sympathy.html">Sympathy</a></li>
        </ul>
    </li>
    
    <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="shop.html" id="shopDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">Shop</a>
        <ul class="dropdown-menu border-0 shadow-sm" aria-labelledby="shopDropdown">
            <li><a class="dropdown-item fw-bold text-primary" href="shop.html">All Collections</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="shop-roses.html">Roses</a></li>
            <li><a class="dropdown-item" href="shop-lilies.html">Lilies</a></li>
            <li><a class="dropdown-item" href="shop-mixed.html">Mixed Bouquets</a></li>
        </ul>
    </li>
    
    <li class="nav-item"><a class="nav-link" href="gallery.html">Gallery</a></li>
    <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
    <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
</ul>"""

# The goal is to replace everything starting from <ul class="navbar-nav ... down to </ul> right before <div class="d-flex flex-column flex-lg-row...
pattern = re.compile(r'<ul\s+class="navbar-nav[^>]*>.*?(?=\s*(?:<!--\s*Actions\s*-->\s*)?<div\s+class="d-flex flex-column flex-lg-row)', re.DOTALL)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the duplicated chunk with new_nav
    new_content = pattern.sub(new_nav, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed Navigation in {file_path}")
    else:
        print(f"Skipped (No match) {file_path}")
