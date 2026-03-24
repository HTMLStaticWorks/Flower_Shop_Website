import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Florist image
html = re.sub(
    r'https://images\.unsplash\.com/photo-1544733422-251e532ca221\?ixlib=[^"]+',
    'assets/images/products/flower-1.jpg',
    html
)

# Replace Gallery Images in order
gallery_images = [
    'assets/images/products/Velvet%20Romance.jfif',
    'assets/images/products/Ethereal%20White.jfif',
    'assets/images/products/Sunshine%20Yellow.jfif',
    'assets/images/products/Pastel%20Dreams.jfif'
]

unsplash_links = [
    r'https://images\.unsplash\.com/photo-1463936575829-25148e1db1b8\?ixlib=[^"]+',
    r'https://images\.unsplash\.com/photo-1510265696660-f1406dc042b5\?ixlib=[^"]+',
    r'https://images\.unsplash\.com/photo-1542475141-94572227d81a\?ixlib=[^"]+',
    r'https://images\.unsplash\.com/photo-1523694576722-cbaec25026df\?ixlib=[^"]+'
]

for unsplash_url, local_img in zip(unsplash_links, gallery_images):
    html = re.sub(unsplash_url, local_img, html)

# Just in case there are any remaining Unsplash links 
# (e.g. if I missed a query string format)
# I will use a generic regex for the remaining gallery images if they didn't match:
if 'unsplash.com' in html:
    print("Warning: Some unsplash links remain!")

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Images replaced in about.html successfully!")
