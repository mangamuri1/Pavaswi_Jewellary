import re
import time

html_file = 'd:/Pavaswi Jewellary_1/Index.html'
try:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    with open(html_file, 'r', encoding='latin-1') as f:
        content = f.read()

# Replace any occurrence of the old logo with Logo.jpeg
# We saw: "http://www.srjewellery369.com/cdn/shop/files/logo_1c6e8b92-f667-4c5f-b882-3698d3a8a34b.jpg"
content = re.sub(r'https?://www\.srjewellery369\.com/cdn/shop/files/logo[^"\'\s]*', 'Logo.jpeg', content, flags=re.IGNORECASE)
content = re.sub(r'//www\.srjewellery369\.com/cdn/shop/files/logo[^"\'\s]*', 'Logo.jpeg', content, flags=re.IGNORECASE)

# We also want to replace the main owner photo. We don't know the exact name.
# Let's replace any "about" or "owner" image with Owner Photo.png
content = re.sub(r'https?://www\.srjewellery369\.com/cdn/shop/files/[^"\'\s]*about[^"\'\s]*', 'Owner Photo.png', content, flags=re.IGNORECASE)
content = re.sub(r'https?://www\.srjewellery369\.com/cdn/shop/files/[^"\'\s]*owner[^"\'\s]*', 'Owner Photo.png', content, flags=re.IGNORECASE)

# Or any large banner image might be the owner photo. Let's just find "banner"
content = re.sub(r'https?://www\.srjewellery369\.com/cdn/shop/files/[^"\'\s]*banner[^"\'\s]*', 'Owner Photo.png', content, flags=re.IGNORECASE)


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Images replaced.")
