from PIL import Image
import os

def process_images(base_input_folder, base_output_folder):
    for folder_name in os.listdir(base_input_folder):
        input_folder = os.path.join(base_input_folder, folder_name)
        if os.path.isdir(input_folder):
            output_folder = os.path.join(base_output_folder, folder_name)
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            images = [Image.open(os.path.join(input_folder, f)) for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

            for index, image in enumerate(images, start=1):
                max_side = max(image.width, image.height)

                horizontal_padding = (max_side - image.width) / 2
                vertical_padding = (max_side - image.height) / 2

                padded_image = Image.new('RGB', (max_side, max_side), (255, 255, 255))  
                padded_image.paste(image, (int(horizontal_padding), int(vertical_padding)))

                image_name = f"{folder_name}_{index}.bmp"
                padded_image.save(os.path.join(output_folder, image_name), 'BMP')

base_input_folder = r'ima\norm_img'
base_output_folder = r'ima\padd_img' 
process_images(base_input_folder, base_output_folder)
