import base64
import pyqrcode

from PIL import Image
from validator import EValidator


def main():
    # rut_personal = 
    rut_empresa = "76.745.604-2"

    img = Image.open(r"image.jpeg")
    img.save(r'image.png')

    # qr = pyqrcode.create("image.png")
    # image_as_str = qr.png_as_base64_str(scale=5)

    # Load image .png .jpg or .jpeg
    # with open("image.jpeg", "rb") as image_file:
    #     # Convert image to base64img string
    #     encoded_image = base64.b64encode(image_file.read())

    # validator = EValidator(base64img=encoded_image)


if __name__ == "__main__":
    main()
