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
            <li><a class="dropdown-item fw-bold" href="occasions.html">View All Occasions</a></li>
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
            <li><a class="dropdown-item fw-bold" href="shop.html">All Collections</a></li>
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

old_js_snippet = """<script>
    // Make desktop dropdown toggles clickable links instead of just opening menus
    document.querySelectorAll('.dropdown-toggle').forEach(item => {
        item.addEventListener('click', function(e) {
            if(window.innerWidth >= 1100 && this.getAttribute('href') && this.getAttribute('href') !== '#') {
                window.location.href = this.getAttribute('href');
            }
        });
    });
</script>"""

new_js_snippet = """<script>
    // Make desktop dropdown toggles clickable links instead of just opening menus
    document.querySelectorAll('.dropdown-toggle').forEach(item => {
        item.addEventListener('click', function(e) {
            if(window.innerWidth >= 1100 && this.getAttribute('href') && this.getAttribute('href') !== '#') {
                window.location.href = this.getAttribute('href');
            }
        });
    });

    // Highlight active menu item
    document.addEventListener("DOMContentLoaded", function() {
        let currentPath = window.location.pathname.split("/").pop();
        if (currentPath === "") currentPath = "index.html";
        
        const navLinks = document.querySelectorAll('.navbar-nav .nav-link, .dropdown-menu .dropdown-item');
        
        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (href === currentPath) {
                link.classList.add('active');
                const parentDropdown = link.closest('.dropdown');
                if (parentDropdown) {
                    const toggle = parentDropdown.querySelector('.dropdown-toggle');
                    if (toggle) toggle.classList.add('active');
                }
            }
        });
        
        if (currentPath.startsWith('shop-')) {
            const shopDropdown = document.getElementById('shopDropdown');
            if (shopDropdown) shopDropdown.classList.add('active');
        } else if (currentPath.startsWith('occasion-')) {
            const occasionsDropdown = document.getElementById('occasionsDropdown');
            if (occasionsDropdown) occasionsDropdown.classList.add('active');
        } else if (currentPath === 'home-2.html') {
            const homeDropdown = document.getElementById('homeDropdown');
            if (homeDropdown) homeDropdown.classList.add('active');
        }
    });
</script>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Strip the old JS snippet if it exists so we don't duplicate
    if old_js_snippet in content:
        content = content.replace(old_js_snippet, '')
    if new_js_snippet in content:
        content = content.replace(new_js_snippet, '')
        
    # 2. Replace the main UL
    pattern = re.compile(r'<ul\s+class="navbar-nav[^>]*>.*?</ul>', re.DOTALL)
    new_content = pattern.sub(new_nav, content)
    
    # 3. Append the JS before body close
    if '</body>' in new_content:
        new_content = new_content.replace('</body>', f'{new_js_snippet}\\n</body>')
        
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated Navigation in {file_path}")
