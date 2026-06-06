import bs4

html_file = 'd:/Pavaswi Jewellary_1/Index.html'
try:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open(html_file, 'r', encoding='latin-1') as f:
        content = f.read()

soup = bs4.BeautifulSoup(content, 'html.parser')

text_to_find = 'Authentic sacred five-metal jewellery'
found_elem = None
for el in soup.find_all(string=True):
    if text_to_find in el:
        found_elem = el.parent
        break

if found_elem:
    address_html = """
    <p style="margin-top: 15px; font-size: 0.9em; opacity: 0.9;">
        Nacharam - Mallapur Rd, below HDFC Bank and central bank,<br>
        IICT Colony, Habsiguda, Hyderabad,<br>
        Secunderabad, Telangana 500076<br>
        <strong>Phone:</strong> 093906 40430
    </p>
    """
    new_p = bs4.BeautifulSoup(address_html, 'html.parser')
    found_elem.insert_after(new_p)
    print("Address added after the description.")
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
else:
    print("Element not found.")

