import base64
import pyqrcode
from pyzbar.pyzbar import decode, ZBarSymbol


from PIL import Image
from validator import EValidator


def main():
    # --- Input ---

    # RUT_PERSONAL = 
    RUT_EMPRESA = "76.745.604-2"

    # Convert .jpeg to .png
    img = Image.open(r"image.jpeg")
    img.save(r'image.png')

    # Create qr code
    # qr = pyqrcode.create("QR_Validator")
    # qr.png("qr.png", scale=3, quiet_zone=4)
    # image_as_str = qr.png_as_base64_str(scale=5)

    # Extract qr code from img
    # qr = qrtools.QR()
    qr = decode(Image.open("image.png"), symbols=[ZBarSymbol.QRCODE])
    print(qr)

    # Load image .png .jpg or .jpeg
    # with open("image.jpeg", "rb") as image_file:
    #     # Convert image to base64img string
    #     encoded_image = base64.b64encode(image_file.read())

    # validator = EValidator(base64img=encoded_image)


if __name__ == "__main__":
    main()
