import os
import re

# Available high-quality images
available_images = [
    "Blush Easter Lily.jfif",
    "Blush Peony Dream.jfif",
    "Blush Rose and Lily Symphony.jfif",
    "Crimson Rose and Stargazer Mix.jfif",
    "Crimson Stargazer.jfif",
    "Ethereal White.jfif",
    "Golden Orienpet Lily.jfif",
    "Golden Sunset.webp",
    "Midnight Calla Lily.jfif",
    "Midnight Lily.jpg",
    "Morning Dew Daylily.jfif",
    "Morning Dew.jfif",
    "Pastel Dreams.jfif",
    "Pastel Oriental.jfif",
    "Pink Asiatic Lily.jfif",
    "Pure White Calla.jfif",
    "Sunshine Yellow.jfif",
    "Velvet Romance.jfif",
    "Vibrant Spring.jfif",
    "Vibrant Tiger Lily.jfif",
    "Yellow Trumpet Lily.jfif"
]

# Simple heuristic matcher
def find_best_image(title, current_img):
    t = title.lower()
    
    # If the current image is ALREADY a named image, keep it
    if not current_img.startswith('flower-'):
        return None
        
    if 'lily' in t or 'lilies' in t or 'calla' in t or 'oriental' in t:
        if 'midnight' in t or 'dark' in t: return "Midnight Calla Lily.jfif"
        if 'pink' in t or 'blush' in t: return "Pink Asiatic Lily.jfif"
        if 'yellow' in t or 'golden' in t: return "Yellow Trumpet Lily.jfif"
        if 'white' in t or 'pure' in t: return "Blush Easter Lily.jfif" # fallback
        if 'tiger' in t or 'vibrant' in t or 'orange' in t: return "Vibrant Tiger Lily.jfif"
        if 'pastel' in t: return "Pastel Oriental.jfif"
        if 'morning' in t or 'dew' in t: return "Morning Dew Daylily.jfif"
        return "Golden Orienpet Lily.jfif"
        
    if 'rose' in t or 'romantic' in t or 'love' in t or 'velvet' in t:
        if 'crimson' in t or 'red' in t: return "Velvet Romance.jfif"
        if 'pink' in t or 'blush' in t: return "Blush Peony Dream.jfif"
        if 'white' in t or 'pure' in t: return "Ethereal White.jfif"
        if 'yellow' in t or 'golden' in t: return "Sunshine Yellow.jfif"
        return "Crimson Rose and Stargazer Mix.jfif"
        
    if 'mix' in t or 'bouquet' in t or 'spring' in t or 'pastel' in t:
        if 'crimson' in t: return "Crimson Rose and Stargazer Mix.jfif"
        if 'pastel' in t: return "Pastel Dreams.jfif"
        if 'spring' in t: return "Vibrant Spring.jfif"
        if 'blush' in t: return "Blush Rose and Lily Symphony.jfif"
        if 'morning' in t: return "Morning Dew.jfif"
        if 'golden' in t or 'sunset' in t: return "Golden Sunset.webp"
        
    # Defaults based on tone
    if 'white' in t or 'sympathy' in t or 'peace' in t: return "Pure White Calla.jfif"
    if 'bright' in t or 'vibrant' in t or 'yellow' in t or 'sun' in t: return "Sunshine Yellow.jfif"
    if 'red' in t or 'passion' in t: return "Crimson Stargazer.jfif"
    
    # If it's just some random generic flower, cycle through nice ones
    return "Vibrant Spring.jfif" # Last resort fallback

count = 0

for file in os.listdir('.'):
    if not file.endswith('.html'): continue
    
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Standard string replacement might be easier, but let's parse via regex to find blocks
    # A card block usually looks like:
    # <img src="assets/images/products/flower-X.jpg"...>
    # ... <h3 class="...">TITLE</h3>
    
    # Since regex is tricky across lines, let's use a simpler token replacement matching
    # We will find all <img src="assets/images/products/flower-X.jpg"...> occurrences,
    # look ahead 500 characters to find the <h3 ...>TITLE</h3>
    
    # Actually Soup is better but we don't have bs4 installed maybe natively. Let me check with regex.
    matches = list(re.finditer(r'<img [^>]*src="assets/images/products/([^"]+)"[^>]*>', html))
    
    if not matches: continue
        
    new_html = html
    offset = 0
    
    for match in matches:
        img_src = match.group(1) # e.g. flower-0.jpg
        # Only replace if generic
        if not img_src.startswith('flower-'): continue
        
        # Look ahead for h3
        lookahead = html[match.end():match.end()+1000]
        h3_match = re.search(r'<h[345][^>]*>([^<]+)</h[345]>', lookahead)
        if h3_match:
            title = h3_match.group(1).strip()
            new_img = find_best_image(title, img_src)
            
            if new_img:
                old_str = f'assets/images/products/{img_src}'
                new_str = f'assets/images/products/{new_img}'
                # Replace this specific occurrence accurately
                # We can replace in the new_html string
                # To be precise, we replace the old_str within the matched img tag
                start_repl = match.start() + offset
                tag_str = match.group(0)
                new_tag_str = tag_str.replace(old_str, new_str)
                new_html = new_html[:start_repl] + new_tag_str + new_html[start_repl+len(tag_str):]
                
                offset += len(new_tag_str) - len(tag_str)
                print(f"[{file}] Replaced {img_src} with {new_img} for product '{title}'")
                count += 1
                
    if new_html != html:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)

print(f"Total replacements made: {count}")
