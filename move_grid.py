import bs4

html_file = 'd:/Pavaswi Jewellary_1/Index.html'
try:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open(html_file, 'r', encoding='latin-1') as f:
        content = f.read()

soup = bs4.BeautifulSoup(content, 'html.parser')

# Find the injected grid section
injected_grid = None
for h2 in soup.find_all('h2'):
    if h2.text.strip() == 'Our Featured Collections':
        injected_grid = h2.find_parent('section')
        break

# Find the old sections
our_collections_section = None
featured_products_section = None

for text in soup.find_all(string=True):
    stripped = text.strip()
    if stripped == 'Our Collections':
        parent = text.parent.find_parent('section') or text.parent.find_parent('div', class_='shopify-section')
        if parent:
            our_collections_section = parent
    elif stripped == 'Featured Products':
        parent = text.parent.find_parent('section') or text.parent.find_parent('div', class_='shopify-section')
        if parent:
            featured_products_section = parent

if injected_grid and our_collections_section:
    # Insert injected_grid before our_collections_section
    our_collections_section.insert_before(injected_grid.extract())
    
    # Decompose the old sections
    our_collections_section.decompose()
    if featured_products_section:
        featured_products_section.decompose()
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print('Successfully moved and replaced.')
else:
    print('Could not find necessary sections.')

