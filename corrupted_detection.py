import os
from PIL import Image

def is_image_corrupted(image_path):
    try:
        with Image.open(image_path) as img:
            img.verify()  # Verify does not decode the image, but ensures it's intact
        return False  # Image is not corrupted
    except (IOError, SyntaxError) as e:
        print(f"\nCorrupted: {image_path} - {e}")
        return True  # Image is corrupted

def check_images_in_folder(main_folder):
    corrupted_images = []
    for root, _, files in os.walk(main_folder):
        for file in files:
            image_path = os.path.join(root, file)
            if is_image_corrupted(image_path):
                corrupted_images.append(image_path)

    if corrupted_images:
        print(f"\nFound {len(corrupted_images)} corrupted images.")
        for img in corrupted_images:
            print(img)
    else:
        print("No corrupted images found.")

# Check images in the 'dinosaurs' folder
main_folder_path = 'dinosaurs'
check_images_in_folder(main_folder_path)