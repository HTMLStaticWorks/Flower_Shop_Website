import re

with open('home-2.html', 'r', encoding='utf-8') as f:
    html = f.read()

images = re.findall(r'<img[^>]+src="([^"]+)"', html)
print("Images found in home-2.html:")
for img in images:
    print(img)
