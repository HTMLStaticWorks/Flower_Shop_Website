import os

updates = [
    # Birthday
    ('assets/images/products/flower-3.jpg', 'assets/images/products/Vibrant Spring.jfif'),
    ('assets/images/products/flower-5.jpg', 'assets/images/products/Pastel Dreams.jfif'),
    # Anniversary
    ('assets/images/products/flower-6.jpg', 'assets/images/products/Blush Rose and Lily Symphony.jfif'),
    ('Eternal Love', 'Blush Symphony'),
    ('assets/images/products/flower-7.jpg', 'assets/images/products/Golden Sunset.webp'),
    ('Golden Years', 'Golden Sunset'),
    # Love
    ('assets/images/products/flower-0.jpg', 'assets/images/products/Crimson Rose and Stargazer Mix.jfif'),
    ('Classic Red Roses', 'Crimson Mix'),
    ('assets/images/products/flower-9.jpg', 'assets/images/products/Velvet Romance.jfif'),
    ('Passionate Pink', 'Velvet Romance'),
    # Sympathy
    ('assets/images/products/flower-4.jpg', 'assets/images/products/Ethereal White.jfif'),
    ('Peaceful White Lily', 'Ethereal White'),
    ('assets/images/products/flower-2.jpg', 'assets/images/products/Pure White Calla.jfif'),
    ('Gentle Comfort', 'Pure White'),
]

with open('occasions.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Also remove the hardcoded fallback onerror handlers just in case they trigger
import re
content = re.sub(r' onerror="this\.src=\'assets/images/products/flower-1\.jpg\'"', '', content)

for old, new in updates:
    content = content.replace(old, new)
    
with open('occasions.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated occasions.html with beautiful new images.")
