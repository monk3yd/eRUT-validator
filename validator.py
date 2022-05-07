import pyqrcode

from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol
from pprint import pprint


class EValidator:
    def __init__(self, base64img: bytes or str) -> bool:
        # Extract qr code from img
        qr = decode(Image.open("image.png"), symbols=[ZBarSymbol.QRCODE])
        print(qr)  # Output list
        # [Decoded(data=b'{"rut":"76745604","dv":"2","serie":"201903175410","razonSocial":"LITRO DE LUZ CHILE SPA","direccion":"ROLANDO FRODDEN 1368 LA FLORIDA"}', type='QRCODE', rect=Rect(left=364, top=942, width=145, height=146), polygon=[Point(x=364, y=942), Point(x=365, y=1087), Point(x=509, y=1088), Point(x=509, y=943)], quality=1, orientation='UP')]

        BASE_URL =
        API_KEY =
