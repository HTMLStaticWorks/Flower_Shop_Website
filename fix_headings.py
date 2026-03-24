import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

target_string1 = 'class="dropdown-item fw-bold text-primary" href="occasions.html"'
replacement1 = 'class="dropdown-item fw-bold" href="occasions.html"'

target_string2 = 'class="dropdown-item fw-bold text-primary" href="shop.html"'
replacement2 = 'class="dropdown-item fw-bold" href="shop.html"'

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(target_string1, replacement1).replace(target_string2, replacement2)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed hardcoded text-primary in {file_path}")
