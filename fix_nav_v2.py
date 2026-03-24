import os
import re

new_nav = """                        <ul class="navbar-nav mx-lg-auto mb-4 mb-lg-0 align-items-lg-center gap-lg-3 fs-5 fs-lg-6">
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="index.html" id="homeDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">Home</a>
                                <ul class="dropdown-menu border-0 shadow-sm" aria-labelledby="homeDropdown">
                                    <li><a class="dropdown-item" href="index.html">Classic Home</a></li>
                                    <li><a class="dropdown-item" href="home-2.html">Modern Home</a></li>
                                </ul>
                            </li>
                            
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="shop.html" id="shopDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">Shop</a>
                                <ul class="dropdown-menu border-0 shadow-sm" aria-labelledby="shopDropdown">
                                    <li><h6 class="dropdown-header text-primary fw-bold">Flowers</h6></li>
                                    <li><a class="dropdown-item fw-bold" href="shop.html">All Collections</a></li>
                                    <li><a class="dropdown-item" href="shop-roses.html">Roses</a></li>
                                    <li><a class="dropdown-item" href="shop-lilies.html">Lilies</a></li>
                                    <li><a class="dropdown-item" href="shop-mixed.html">Mixed Bouquets</a></li>
                                    <li><hr class="dropdown-divider"></li>
                                    <li><h6 class="dropdown-header text-primary fw-bold">Occasions</h6></li>
                                    <li><a class="dropdown-item fw-bold" href="occasions.html">View All Occasions</a></li>
                                    <li><a class="dropdown-item" href="occasion-birthday.html">Birthday</a></li>
                                    <li><a class="dropdown-item" href="occasion-anniversary.html">Anniversary</a></li>
                                    <li><a class="dropdown-item" href="occasion-love.html">Love & Romance</a></li>
                                    <li><a class="dropdown-item" href="occasion-sympathy.html">Sympathy</a></li>
                                </ul>
                            </li>
                            
                            <li class="nav-item"><a class="nav-link" href="gallery.html">Gallery</a></li>
                            <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
                            <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
                        </ul>"""

new_js_snippet = """    <script>
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
            
            if (currentPath.startsWith('shop-') || currentPath.startsWith('occasion-') || currentPath === 'occasions.html' || currentPath === 'shop.html') {
                const shopDropdown = document.getElementById('shopDropdown');
                if (shopDropdown) shopDropdown.classList.add('active');
            } else if (currentPath === 'home-2.html') {
                const homeDropdown = document.getElementById('homeDropdown');
                if (homeDropdown) homeDropdown.classList.add('active');
            }
        });
    </script>
</body>"""

for f in os.listdir('.'):
    if not f.endswith('.html'): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Find start and end using regex
    pat = re.compile(r'(<div class="offcanvas-body d-flex flex-column align-items-lg-center">\s*)(<ul.*?)(<!-- Actions -->)', re.DOTALL)
    
    match = pat.search(content)
    if match:
        content = content[:match.start(2)] + new_nav + '\\n\\n                        ' + content[match.start(3):]
    else:
        print(f"Could not find nav in {f}")
        
    # Replace scripts
    pat_script = re.compile(r'(<script>\s*// Make desktop dropdown toggles clickable links.*)(</body>\s*</html>|</body>\s*|</html>\s*)', re.DOTALL)
    match_script = pat_script.search(content)
    if match_script:
        content = content[:match_script.start(1)] + new_js_snippet + '\\n</html>'
    else:
        print(f"Could not find scripts in {f}")

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
    print(f"Fixed {f}")
