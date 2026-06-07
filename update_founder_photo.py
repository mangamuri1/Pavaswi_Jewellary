import re

file_path = r'd:\Pavaswi Jewellary_1\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace hero section image
content = content.replace('src="Owner%20Photo.png"', 'src="Founder_Photo.png"')

# Replace about section base64 image
# The tag starts with <img alt="Pavaswi Owner" class="about-owner-img" src="data:image/png;base64,
import re
pattern = r'<img alt="Pavaswi Owner" class="about-owner-img" src="data:image/png;base64,[^"]*"/>'
content = re.sub(pattern, '<img alt="Pavaswi Owner" class="about-owner-img" src="Founder_Photo.png" />', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replacement complete.")
