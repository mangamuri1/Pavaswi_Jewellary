import bs4

html_file = 'd:/Pavaswi Jewellary_1/Index.html'
try:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open(html_file, 'r', encoding='latin-1') as f:
        content = f.read()

soup = bs4.BeautifulSoup(content, 'html.parser')

images = [
    'Blackbids_1.jpg',
    'Blackbids_2.jpg',
    'Blackbids_3.jpg',
    'Blackbids_4.jpg',
    'Mens_Bracelet.jpg',
    'Thali Chains.jpg'
]

# Find product cards
cards = soup.find_all(lambda tag: tag.name == 'a' and tag.get('class') and 'product-card__link' in tag.get('class'))

if not cards:
    # try another way
    cards = soup.find_all(class_=lambda c: c and ('product-card' in c or 'grid__item' in c))

print(f"Found {len(cards)} products.")

for i, card in enumerate(cards):
    # Find img tags in this product
    parent = card.find_parent('li')
    if not parent:
        parent = card.find_parent('div', class_=lambda c: c and 'grid__item' in c)
    if not parent:
        parent = card
        
    imgs = parent.find_all('img')
    img_name = images[i % len(images)]
    
    for img in imgs:
        img['src'] = img_name
        if 'srcset' in img.attrs:
            del img['srcset']

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('Product images added.')
