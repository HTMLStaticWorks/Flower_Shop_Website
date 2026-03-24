import os
import re
import urllib.parse

count = 0
for file in os.listdir('.'):
    if not file.endswith('.html') or file == 'product-detail.html': 
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    new_html = ""
    last_idx = 0
    
    for match in re.finditer(r'href="product-detail\.html(?=")', html):
        idx = match.start()
        
        # Look backwards 1500 characters
        search_start = max(0, idx - 1500)
        card_content = html[search_start:idx]
            
        img_matches = list(re.finditer(r'<img[^>]+src="([^"]+)"', card_content))
        title_matches = list(re.finditer(r'<h[345][^>]*>([^<]+)</h[345]>', card_content))
        price_matches = list(re.finditer(r'(\$[\d\.]+)', card_content))
        
        if img_matches and title_matches and price_matches:
            img_m = img_matches[-1]
            title_m = title_matches[-1]
            price_m = price_matches[-1]
            
            img = urllib.parse.quote(img_m.group(1))
            title = urllib.parse.quote(title_m.group(1).strip())
            price = urllib.parse.quote(price_m.group(1))
            
            new_href = f'href="product-detail.html?title={title}&price={price}&img={img}'
            
            new_html += html[last_idx:idx] + new_href
            last_idx = match.end()
            count += 1
        else:
            new_html += html[last_idx:match.end()]
            last_idx = match.end()
            
    new_html += html[last_idx:]
    
    if new_html != html:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated {file}")

print(f"Total dynamic links updated: {count}")
