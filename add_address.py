import bs4
import os

html_file = 'd:/Pavaswi Jewellary_1/Index.html'
try:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open(html_file, 'r', encoding='latin-1') as f:
        content = f.read()

soup = bs4.BeautifulSoup(content, 'html.parser')

print('Adding address...')
footer = soup.find('footer')
if not footer:
    # If no footer, append to body
    footer = soup.body

# Check if we already added it
if 'Nacharam - Mallapur Rd' not in str(footer):
    address_html = """
    <div style="text-align: center; padding: 20px; background-color: #f8f8f8; color: #333; font-family: sans-serif; border-top: 1px solid #ddd; margin-top: 40px;">
        <h3 style="margin-bottom: 10px;">Visit Our Store</h3>
        <p style="margin: 5px 0;"><strong>PAVASWI JEWELLARY</strong></p>
        <p style="margin: 5px 0;">Nacharam - Mallapur Rd, below HDFC Bank and central bank,</p>
        <p style="margin: 5px 0;">IICT Colony, Habsiguda, Hyderabad,</p>
        <p style="margin: 5px 0;">Secunderabad, Telangana 500076</p>
        <p style="margin: 5px 0; font-weight: bold;">Phone: 093906 40430</p>
    </div>
    """
    new_div = bs4.BeautifulSoup(address_html, 'html.parser')
    footer.append(new_div)

print('Saving file...')
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('Done')
