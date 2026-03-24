import os
import re

exact_mappings = {
    'Classic Red': 'Crimson Stargazer.jfif',
    'Pastel Dreams': 'Pastel Dreams.jfif',
    'Sunshine Yellow': 'Sunshine Yellow.jfif',
    'Ethereal White': 'Ethereal White.jfif',
    'Vibrant Spring': 'Vibrant Spring.jfif',
    'Blush Peony Dream': 'Blush Peony Dream.jfif',
    'Velvet Romance': 'Velvet Romance.jfif',
    'Morning Dew': 'Morning Dew.jfif',
    'Golden Sunset': 'Golden Sunset.webp',
    'Midnight Lily': 'Midnight Lily.jpg',
    'Elegant Lilies': 'Golden Orienpet Lily.jfif',
    'Signature Roses': 'Crimson Rose and Stargazer Mix.jfif',
    'Mixed Bouquets': 'Blush Rose and Lily Symphony.jfif',
}

files_to_check = ['shop.html', 'index.html', 'home-2.html', 'shop-roses.html', 'shop-mixed.html', 'shop-lilies.html']

for f in files_to_check:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
            
        # Regex to find img tag followed eventually by the h3 title tag in the card body
        pattern = re.compile(r'(<img[^>]*src=")(assets/images/products/[^"]+)("[^>]*>.*?<h[345][^>]*>)([^<]+)(</h[345]>)', re.DOTALL)
        
        def replacer(match):
            prefix = match.group(1)
            old_src = match.group(2)
            mid = match.group(3)
            title = match.group(4).strip()
            suffix = match.group(5)
            
            if title in exact_mappings:
                new_src = 'assets/images/products/' + exact_mappings[title]
                if old_src != new_src:
                    print(f"[{f}] Replaced {old_src} with {new_src} for '{title}'")
                return prefix + new_src + mid + title + suffix
            return match.group(0)

        new_html = pattern.sub(replacer, html)
        
        if new_html != html:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_html)

gallery_images = [
    "Blush Peony Dream.jfif",
    "Golden Sunset.webp",
    "Midnight Calla Lily.jfif",
    "Velvet Romance.jfif",
    "Vibrant Tiger Lily.jfif",
    "Morning Dew Daylily.jfif"
]

if os.path.exists('gallery.html'):
    with open('gallery.html', 'r', encoding='utf-8') as f:
        gh = f.read()
        
    for i in range(6):
        gh = gh.replace(f'assets/images/products/flower-{i}.jpg', f'assets/images/products/{gallery_images[i]}')
        
    with open('gallery.html', 'w', encoding='utf-8') as f:
        f.write(gh)
    print("Fixed gallery images")
