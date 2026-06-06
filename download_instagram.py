import os
import re
import instaloader

L = instaloader.Instaloader(
    download_pictures=False,
    download_comments=False,
    save_metadata=False,
    post_metadata_txt_pattern=""
)

OUTPUT_FOLDER = "downloads"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

with open("urls.txt", "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

for url in urls:
    try:
        shortcode = re.search(r"/(reel|p)/([^/]+)/", url).group(2)

        post = instaloader.Post.from_shortcode(
            L.context,
            shortcode
        )

        L.dirname_pattern = OUTPUT_FOLDER
        L.download_post(post, target=shortcode)

        print(f"Downloaded: {url}")

    except Exception as e:
        print(f"Failed: {url}")
        print(e)

print("Done")