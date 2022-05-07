from pprint import pprint


class EValidator():
    def __init__(self, base64img: bytes or str) -> bool:
        pprint(base64img)
        pprint(type(base64img))


        # Extract qr code from img
        # qr = decode(Image.open("image.png"), symbols=[ZBarSymbol.QRCODE])
        # print(qr)  # Output list
