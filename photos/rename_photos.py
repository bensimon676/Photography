# rename_jpg_to_jpeg.py
import os

def rename_jpg_to_jpeg(directory="photos"):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".jpeg"):
            base = os.path.splitext(filename)[0]
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, base + ".jpg")
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} → {base}.jpg")

if __name__ == "__main__":
    rename_jpg_to_jpeg()
