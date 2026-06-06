import bs4
import random

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
names = [
    'Elegant Black Beads',
    'Classic Black Beads',
    'Premium Black Beads',
    'Modern Black Beads',
    "Men's Bracelet",
    'Traditional Thali Chain'
]

grid_html = """
<section style="padding: 40px 20px; background-color: #fcfcfc;">
    <h2 style="text-align: center; font-size: 2em; margin-bottom: 30px; font-family: serif; color: #222;">Our Featured Collections</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 30px; max-width: 1200px; margin: 0 auto;">
"""

for i in range(30):
    img = images[i % len(images)]
    name = names[i % len(names)]
    grid_html += f"""
        <div style="background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease;">
            <img src="{img}" alt="{name}" style="width: 100%; height: 250px; object-fit: cover;">
            <div style="padding: 15px; text-align: center;">
                <h3 style="font-size: 1.1em; margin: 0 0 10px 0; color: #333; font-family: sans-serif;">{name}</h3>
                <a href="#" style="display: inline-block; padding: 8px 20px; background-color: #d4af37; color: white; text-decoration: none; border-radius: 4px; font-weight: bold; font-family: sans-serif;">View Details</a>
            </div>
        </div>
    """

grid_html += """
    </div>
</section>
"""

new_grid = bs4.BeautifulSoup(grid_html, 'html.parser')

footer = soup.find('footer')
if footer:
    footer.insert_before(new_grid)
else:
    if soup.body:
         soup.body.append(new_grid)
    else:
         soup.append(new_grid)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('New grid injected successfully.')
