import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BIKE_IMG_DIR = os.path.join(BASE_DIR, "personalWebsite/static/bike_img")


def main():
    os.chdir(BIKE_IMG_DIR)

    dir_items = os.listdir()
    for item in dir_items:
        if item.startswith("."):
            continue

        if os.path.isdir(item):
            os.chdir(os.path.abspath(item))
            img_dir = os.getcwd()
            for img in os.listdir(img_dir):
                if img.startswith("."):
                    continue

                print(item, img)
                current_img = Image.open(img)
                if current_img.mode in ("RGBA", "P"):
                    current_img = current_img.convert("RGB")
                current_img.save(img, optimize=True, quality=60)
     
        os.chdir(BIKE_IMG_DIR)

if __name__ == "__main__":
    main()