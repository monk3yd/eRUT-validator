# import json
# import base64
# import cv2 as cv

# from PIL import Image
# from pyzbar import pyzbar


# def extract_qr(base64img):
#     '''Input base64img. Output qr data as python dict'''

#     # Create .bin file from encoded byte string
#     with open("encoded/tmp_image.bin", "wb") as file:
#         file.write(base64img)

#     # Decode base64img into png
#     with open("new_image.png", "wb") as png_image:
#         png_image.write(base64.b64decode(base64img))

#     # Load converted png img
#     filename = "new_image.png"
#     image = cv.imread(filename)

#     # Decode embedded qr
#     qr_data = pyzbar.decode(
#         image,
#         symbols=[pyzbar.ZBarSymbol.QRCODE]
#     )

#     # Filter qr data and turn into python dict
#     qr_str_dict_data = qr_data[0].data.decode("UTF-8")
#     qr_dict_data = json.loads(qr_str_dict_data)
#     # print(qr_dict_data)

#     return qr_dict_data


def clean_rut(rut):
    '''Clean input rut for validation.  # TODO - Depends on expected input format'''
    input_rut = rut[:-1].replace(".", "").replace("-", "")
    input_dv = rut[-1]
    return input_rut, input_dv


# def validate_rut(rut_empresa):
#     input_rut, input_dv = clean_rut(rut_empresa)
#     # Validate (rut empresa) input with qr data
#     if input_rut_empresa != qr_dict_data["rut"] or input_dv_empresa != qr_dict_data["dv"]:
#         print("Entered rut empresa is invalid.")
#         return False


# https://stackoverflow.com/questions/27233351/how-to-decode-a-qr-code-image-in-preferably-pure-python
# https://stackoverflow.com/questions/20778072/sniffing-an-android-app-to-find-api-url
# https://stackoverflow.com/questions/9867410/barcode-scanning-in-android-emulator
