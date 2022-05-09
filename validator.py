from zeep import Client, Settings
from utils import extract_qr, validate_rut


class EValidator:
    def __init__(self, base64img: bytes or str, rut_persona: str, rut_empresa: str) -> bool:
        # Input base64img. Output qr data as python dict
        qr_dict_data = extract_qr(base64img=base64img)

        if not validate_rut(rut_empresa):
            return False

        # Reverse engineer API for missing data that need validation
        WSDL_URL = "https://ws1.sii.cl/WSCREP/crepwsservice.wsdl"
        header = {}
        settings = Settings(strict=False, extra_http_headers=header)
        client = Client(
            wsdl=WSDL_URL,
            settings=settings
        )

        request_data = {
            "rut": qr_dict_data["rut"],  # rut empresa
            "dv": qr_dict_data["dv"],  # digito verificador
            "serie": qr_dict_data["serie"]
        }

        response = client.service.verificacionCedulaSmp(**request_data)
        # print(response)

        # Clean input rut persona for validation  # Depends on expected input format
        input_rut_persona = rut_persona[:-1].replace(".", "").replace("-", "")
        input_dv_persona = rut_persona[-1]

        # Validate (rut persona) input with API response data
        if input_rut_persona == response["rutUsuario"] and input_dv_persona == response["dvUsuario"]:
            print("All input data is valid.")
            return True
        else:
            print("Entered rut persona is invalid.")
            return False


# https://stackoverflow.com/questions/27233351/how-to-decode-a-qr-code-image-in-preferably-pure-python
# https://stackoverflow.com/questions/20778072/sniffing-an-android-app-to-find-api-url
# https://stackoverflow.com/questions/9867410/barcode-scanning-in-android-emulator
