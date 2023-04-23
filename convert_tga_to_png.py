import os
from PIL import Image

tga_folder = "MapIcons"
small_png_folder = "images/icons"
big_png_folder = "map_by_region"

for image_path in os.listdir(tga_folder):
    if image_path.endswith(".TGA"):
        print("Processing " + image_path)
        tga_path = os.path.join(tga_folder, image_path)
        # big_png_path = os.path.join(big_png_folder, image_path.split(".")[0] + ".png")
        small_png_path = os.path.join(small_png_folder, image_path.split(".")[0] + ".png")
        image = Image.open(tga_path)
        image.save(small_png_path, "PNG")
        # image = image.resize((40960, 35520))
        # image.save(big_png_path)
