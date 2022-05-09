import json
import base64
import cv2 as cv

from PIL import Image
from pyzbar import pyzbar
from zeep import Client, Settings

from utils import clean_rut


class EValidator:
    def __init__(self, base64img: bytes or str, rut_persona: str, rut_empresa: str) -> bool:
        self.rut_persona = rut_persona
        self.rut_empresa = rut_empresa

        # Create .bin file from encoded byte string
        with open("encoded/tmp_image.bin", "wb") as file:
            file.write(base64img)

        # Decode base64img into png
        with open("new_image.png", "wb") as png_image:
            png_image.write(base64.b64decode(base64img))

        # Load converted png img
        filename = "new_image.png"
        image = cv.imread(filename)

        # Decode embedded qr  # TODO - catch image blur exception
        qr_data = pyzbar.decode(
            image,
            symbols=[pyzbar.ZBarSymbol.QRCODE]
        )

        # Filter qr data and turn into python dict
        qr_str_dict_data = qr_data[0].data.decode("UTF-8")
        self.qr_dict_data = json.loads(qr_str_dict_data)

    def check(self):
        input_rut_empresa, input_dv_empresa = clean_rut(self.rut_empresa)

        # Validate (rut empresa) input, with QR data
        if input_rut_empresa != str(self.qr_dict_data["rut"]) or input_dv_empresa != str(self.qr_dict_data["dv"]):
            print("Entered rut empresa is invalid.")
            return False

        # Reverse engineer API for missing data that need validation
        WSDL_URL = "https://ws1.sii.cl/WSCREP/crepwsservice.wsdl"
        header = {}
        settings = Settings(strict=False, extra_http_headers=header)
        client = Client(
            wsdl=WSDL_URL,
            settings=settings
        )

        # Serach missing data with qr data
        request_data = {
            "rut": self.qr_dict_data["rut"],  # rut empresa
            "dv": self.qr_dict_data["dv"],  # digito verificador
            "serie": self.qr_dict_data["serie"]
        }
        response = client.service.verificacionCedulaSmp(**request_data)

        input_rut_persona, input_dv_persona = clean_rut(self.rut_persona)

        # Validate (rut persona) input with API response data
        if input_rut_persona != str(response["rutUsuario"]) or input_dv_persona != str(response["dvUsuario"]):
            print("Entered rut persona is invalid.")
            return False

        print("All input data is valid.")
        return True
