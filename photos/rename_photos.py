import os

def rename_jpg_to_jpeg(directory='.'):
    for filename in os.listdir(directory):
        # Check if it's a file and ends with .jpg (case-insensitive)
        if os.path.isfile(os.path.join(directory, filename)) and filename.lower().endswith('.jpg'):
            base = os.path.splitext(filename)[0]
            new_name = base + '.jpeg'
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            os.rename(old_file, new_file)
            print(f'Renamed: {filename} -> {new_name}')

if __name__ == "__main__":
    rename_jpg_to_jpeg()

