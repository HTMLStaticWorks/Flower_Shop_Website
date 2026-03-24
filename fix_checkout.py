import os
import re

# 1. Update product-detail.html's script to pass params to checkout
with open('product-detail.html', 'r', encoding='utf-8') as f:
    pd_html = f.read()

injection = """            if (img) {
                const imgEl = document.querySelector('img.img-fluid.rounded-4');
                if (imgEl) imgEl.src = img;
            }
            
            // Pass params to checkout
            if (title && price && img) {
                const checkoutBtn = document.querySelector('a[href="checkout.html"]');
                if (checkoutBtn) {
                    checkoutBtn.href = `checkout.html?title=${encodeURIComponent(title)}&price=${encodeURIComponent(price)}&img=${encodeURIComponent(img)}`;
                }
            }"""

if '// Pass params to checkout' not in pd_html:
    pd_html = pd_html.replace("""            if (img) {
                const imgEl = document.querySelector('img.img-fluid.rounded-4');
                if (imgEl) imgEl.src = img;
            }""", injection)
    with open('product-detail.html', 'w', encoding='utf-8') as f:
        f.write(pd_html)


# 2. Fix checkout.html alignment and add dynamic logic
with open('checkout.html', 'r', encoding='utf-8') as f:
    ch_html = f.read()

# Fix alignment: replace 'text-center' with 'text-start' recursively inside the form
# Actually, the quickest way to fix the form alignment is to replace ' text-center' with ' text-start'
# specifically on col- classes inside left column.
ch_html = ch_html.replace('col-lg-7 col-xl-8 text-center', 'col-lg-7 col-xl-8 text-start')
ch_html = ch_html.replace('col-md-6 text-center', 'col-md-6 text-start')
ch_html = ch_html.replace('col-12 text-center', 'col-12 text-start')
ch_html = ch_html.replace('col-6 text-center', 'col-6 text-start')

# Add IDs to the summary items so JS can populate them
summary_img_target = '<img src="https://images.unsplash.com/photo-1523694576722-cbaec25026df?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80"\n                                    class="rounded-3 object-fit-cover" style="width: 70px; height: 70px;"\n                                    alt="Pastel Dreams">'
summary_img_new = '<img src="https://images.unsplash.com/photo-1523694576722-cbaec25026df?ixlib=rb-4.0.3&auto=format&fit=crop&w=150&q=80"\n                                    class="rounded-3 object-fit-cover" style="width: 70px; height: 70px;"\n                                    alt="Pastel Dreams" id="summary-img">'
ch_html = ch_html.replace(summary_img_target, summary_img_new)

ch_html = ch_html.replace('<h3 class="h6 mb-1 fw-bold">Pastel Dreams</h3>', '<h3 class="h6 mb-1 fw-bold" id="summary-title">Pastel Dreams</h3>')
ch_html = ch_html.replace('<div class="fw-bold">$85.00</div>', '<div class="fw-bold" id="summary-price">$85.00</div>')
ch_html = ch_html.replace('<span>$110.00</span>', '<span id="summary-subtotal">$110.00</span>')
ch_html = ch_html.replace('<span class="h5 fw-bold text-primary mb-0">$110.00</span>', '<span class="h5 fw-bold text-primary mb-0" id="summary-total">$110.00</span>')


params_script = """
        // Parse checkout params dynamically
        document.addEventListener("DOMContentLoaded", function () {
            const params = new URLSearchParams(window.location.search);
            const title = params.get('title');
            const priceStr = params.get('price');
            const img = params.get('img');
            
            if (title) document.getElementById('summary-title').textContent = title;
            if (img) document.getElementById('summary-img').src = img;
            
            if (priceStr) {
                document.getElementById('summary-price').textContent = priceStr;
                
                // Calculate new totals (Add-on is $25)
                const priceNum = parseFloat(priceStr.replace('$', ''));
                if (!isNaN(priceNum)) {
                    const total = priceNum + 25;
                    document.getElementById('summary-subtotal').textContent = '$' + total.toFixed(2);
                    document.getElementById('summary-total').textContent = '$' + total.toFixed(2);
                }
            }
        });
"""

# inject right before the form interactivity script
ch_html = ch_html.replace('// Form interactivity', params_script + '\n        // Form interactivity')

# Fix highlight to match shop items
ch_html = ch_html.replace("|| currentPath === 'shop.html'", "|| currentPath === 'shop.html' || currentPath.startsWith('checkout.html')")

with open('checkout.html', 'w', encoding='utf-8') as f:
    f.write(ch_html)

print("Updates completed successfully.")
