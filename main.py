import base64
import pyqrcode
from pyzbar.pyzbar import decode, ZBarSymbol

from PIL import Image
from validator import EValidator


def main():
    # Convert .jpeg into .png image and save
    # img = Image.open(r"image.jpeg")
    # img.save(r'image.png')

    # --- Input ---
    # RUT_PERSONAL = 
    RUT_EMPRESA = "76.745.604-2"
    base64img = base64.b64encode(open("image.png", "rb").read())

    # --- Blackbox ---
    validator = EValidator(str(base64img))

    
    # Load image .png .jpg or .jpeg
    # with open("image.jpeg", "rb") as image_file:
    #     # Convert image to base64img string
    #     encoded_image = base64.b64encode(image_file.read())



if __name__ == "__main__":
    main()
