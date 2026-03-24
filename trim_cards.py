import os

files = ['occasion-birthday.html', 'occasion-anniversary.html', 'occasion-love.html', 'occasion-sympathy.html', 'occasions.html']

for f in files:
    if not os.path.exists(f):
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    content = content.replace("Showing 10 beautiful arrangements", "Showing 2 beautiful arrangements")
    
    parts = content.split('<div class="col">')
    if len(parts) >= 11:
        new_content = parts[0] + '<div class="col">' + parts[1] + '<div class="col">' + parts[2]
        
        last_part = parts[-1]
        
        idx = last_part.rfind('                </div>')
        if idx != -1:
            closing_tags = last_part[idx:]
            
            new_content += closing_tags
            
            with open(f, 'w', encoding='utf-8') as out:
                out.write(new_content)
            print(f"Trimmed {f} to 2 cards.")
        else:
            print(f"Could not find closing tags in {f}")
    else:
        print(f"Could not split by cols in {f}")
