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
                                    <li><a class="dropdown-item" href="shop-roses.html">Roses</a></li>
                                    <li><a class="dropdown-item" href="shop-lilies.html">Lilies</a></li>
                                    <li><a class="dropdown-item" href="occasions.html">Occasions</a></li>
                                </ul>
                            </li>
                            
                            <li class="nav-item"><a class="nav-link" href="gallery.html">Gallery</a></li>
                            <li class="nav-item"><a class="nav-link" href="about.html">About</a></li>
                            <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
                        </ul>"""

for f in os.listdir('.'):
    if not f.endswith('.html'): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    pat = re.compile(r'(<div class="offcanvas-body d-flex flex-column align-items-lg-center">\s*)(<ul.*?)(<!-- Actions -->|<div\s+class="d-flex flex-column flex-lg-row align-items-lg-center)', re.DOTALL)
    
    match = pat.search(content)
    if match:
        content = content[:match.start(2)] + new_nav + '\\n\\n                        ' + content[match.start(3):]

    
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated nav in {f}")
    else:
        print(f"Could not find nav in {f}")
