import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace old URLs with local ones sequentially
i = 0
def repl(m):
    global i
    ret = f'assets/images/products/flower-{i % 10}.jpg'
    i += 1
    return ret

new_content = re.sub(
    r'https://images\.unsplash\.com/[^"]*',
    repl,
    content
)

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    print("Gallery fixed.")
