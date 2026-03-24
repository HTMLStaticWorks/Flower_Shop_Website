import os
import re

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Clean up literal '\n\n' text that appeared in headers
        new_content = content.replace('\\n\\n', '')
        
        # Remove Razorpay broken image block in checkout.html
        if filename == 'checkout.html':
            pattern = re.compile(r'<div class="text-center opacity-50">\s*<img[^>]+Razorpay[^>]+>\s*</div>', re.DOTALL)
            new_content = pattern.sub('', new_content)
            
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Cleaned {filename}")
