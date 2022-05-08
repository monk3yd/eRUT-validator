import base64
import cv2 as cv

from PIL import Image
from pyzbar import pyzbar
from pprint import pprint


class EValidator:
    def __init__(self, base64img: bytes or str, rut_empresa: str) -> bool:

        # # Create .bin file from encoded byte string
        with open("encoded/tmp_image.bin", "wb") as file:
            file.write(base64img)

        # Decode base64img into png
        with open("new_image.png", "wb") as png_image:
            png_image.write(base64.b64decode(base64img))

        # Load converted png img
        filename = "new_image.png"
        image = cv.imread(filename)

        # Decode embedded qr
        qr_data = pyzbar.decode(
            image,
            symbols=[pyzbar.ZBarSymbol.QRCODE]
        )

        print(qr_data)

        # TODO - Reverse engineer API for missing data that need validation
        # BASE_URL
        # API_KEY


# https://stackoverflow.com/questions/27233351/how-to-decode-a-qr-code-image-in-preferably-pure-python
# https://stackoverflow.com/questions/20778072/sniffing-an-android-app-to-find-api-url
# https://stackoverflow.com/questions/9867410/barcode-scanning-in-android-emulator