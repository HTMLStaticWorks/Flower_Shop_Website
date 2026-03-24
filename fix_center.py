import glob
import re

files = glob.glob('e:/OfficeDownloads_/MarchWebsites/Flower_Shop_Website/shop*.html') + \
        glob.glob('e:/OfficeDownloads_/MarchWebsites/Flower_Shop_Website/occasion*.html')

pattern = re.compile(
    r'(<h2 class="h3 fw-bold mb-3">Can\'t decide\? Let us help!</h2>\s*<p class="text-muted mb-4">)(.*?)(</p>)',
    re.DOTALL
)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replacer(match):
        return match.group(1).replace('class="text-muted mb-4"', 'class="text-muted mb-4 mx-auto text-center" style="max-width: 600px;"') + match.group(2) + match.group(3)
        
    new_content = pattern.sub(replacer, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Processed {len(files)} files.")
