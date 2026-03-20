import urllib.request
import os
import time

os.makedirs('assets/images/products', exist_ok=True)

images = [
    "https://images.unsplash.com/photo-1542475141-94572227d81a?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1523694576722-cbaec25026df?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1457089328109-e5d9bd49f563?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1582294158913-91ea8238faec?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1508785633634-1b32d201c103?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1613539246066-78db6ec4ff0f?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1463936575829-25148e1db1b8?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1588628566587-dc51addef209?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1510265696660-f1406dc042b5?auto=format&fit=crop&w=800&q=80"
]
hero = "https://images.unsplash.com/photo-1563241598-a28a304e2808?auto=format&fit=crop&w=1200&q=80"

try:
    print("Downloading hero image...")
    req = urllib.request.Request(hero, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req) as response, open('assets/images/hero.jpg', 'wb') as out_file:
        out_file.write(response.read())

    for i, url in enumerate(images):
        print(f"Downloading product {i}...")
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as response, open(f'assets/images/products/flower-{i}.jpg', 'wb') as out_file:
            out_file.write(response.read())
        time.sleep(0.5)

    print("All images downloaded successfully!")
except Exception as e:
    print("Error:", e)
    # Fallback to loremflickr if Unsplash blocks the bot
    print("Trying fallback loremflickr...)")
    try:
        h_req = urllib.request.Request("https://loremflickr.com/1200/800/flower,shop", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(h_req) as response, open('assets/images/hero.jpg', 'wb') as out_file:
            out_file.write(response.read())
        for i in range(10):
            req = urllib.request.Request(f"https://loremflickr.com/800/600/flower?random={i+1}", headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(f'assets/images/products/flower-{i}.jpg', 'wb') as out_file:
                out_file.write(response.read())
            time.sleep(0.5)
        print("Fallback images downloaded successfully!")
    except Exception as e2:
        print("Fallback Error:", e2)
