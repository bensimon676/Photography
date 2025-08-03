# rename_and_update_index.py
import os
import re

PHOTO_DIR = "photos"
INDEX_FILE = "index.html"

def rename_photos():
    images = sorted(
        [f for f in os.listdir(PHOTO_DIR) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    )

    renamed = []
    for i, original in enumerate(images, 1):
        ext = os.path.splitext(original)[1].lower()
        new_name = f"photo{i}{ext}"
        src = os.path.join(PHOTO_DIR, original)
        dst = os.path.join(PHOTO_DIR, new_name)
        if src != dst:
            os.rename(src, dst)
        renamed.append(new_name)
    return renamed

def update_index_html(renamed_files):
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    new_gallery_html = "\n".join([
        f'''          <a href="{PHOTO_DIR}/{file}" data-aos="zoom-in">
            <img src="{PHOTO_DIR}/{file}" alt="" class="rounded-xl shadow hover:scale-105 transition duration-300" loading="lazy">
          </a>''' for file in renamed_files
    ])

    updated = re.sub(
        r"(<div id=\"lightgallery\".*?>)(.*?)(</div>)",
        f"\\1\n{new_gallery_html}\n          \\3",
        content,
        flags=re.DOTALL
    )

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    renamed_files = rename_photos()
    update_index_html(renamed_files)
    print("✅ Renamed images and updated index.html gallery.")
