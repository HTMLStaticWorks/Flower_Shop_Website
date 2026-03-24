import os
import glob
import re

html_files = glob.glob('e:/OfficeDownloads_/MarchWebsites/Flower_Shop_Website/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Strip out start-alignment overrides throughout the document (safe ones)
    html = re.sub(r'\btext-lg-start\b', 'text-center', html)
    html = re.sub(r'\btext-md-start\b', 'text-center', html)
    html = re.sub(r'\btext-sm-start\b', 'text-center', html)
    
    html = re.sub(r'\bjustify-content-lg-start\b', 'justify-content-center', html)
    html = re.sub(r'\bjustify-content-md-start\b', 'justify-content-center', html)
    html = re.sub(r'\bjustify-content-start\b', 'justify-content-center', html)
    
    html = re.sub(r'\balign-items-lg-start\b', 'align-items-center', html)
    html = re.sub(r'\balign-items-md-start\b', 'align-items-center', html)
    # Be careful not to replace align-items-start blindly if it's structural, but user wants center.
    html = re.sub(r'\balign-items-start\b', 'align-items-center', html)

    # Cleanup redundancies
    html = re.sub(r'\btext-center(\s+text-center)+\b', 'text-center', html)
    html = re.sub(r'\bjustify-content-center(\s+justify-content-center)+\b', 'justify-content-center', html)

    # 2. Inject text-center into specific known uncentered columns inside <main>
    main_pattern = re.compile(r'(<main[^>]*>)(.*?)(</main>)', re.DOTALL)
    
    def replacer(match):
        content = match.group(2)
        # Add text-center to relevant col divs
        def add_center(m):
            cls = m.group(1)
            # Add text-center if it doesn't have it, AND it's not a generic row container
            if 'text-center' not in cls and 'text-end' not in cls:
                return f'class="{cls} text-center"'
            return m.group(0)
            
        content = re.sub(r'class="([^"]*col-(?:lg|md|sm|12|6|8|4)[^"]*)"', add_center, content)
        return match.group(1) + content + match.group(3)

    html = main_pattern.sub(replacer, html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print(f"Processed {len(html_files)} files.")
