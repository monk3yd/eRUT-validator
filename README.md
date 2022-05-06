
# Project: eRUT image validator
# Objective: Create object in charge of validation (EValidator)

# input
rut personal
rut empresa
imagen base64 (.png/.jpg/.jpeg)

# blackbox
extract qr code from image string
scan qr code
validate if input same as output of scan

# output
error - image blur
true - correct validation - input == validation return data
false - incorrect validation - input != validation return data



# Related
https://www.sii.cl/destacados/erut/  - main homepage
https://2captcha.com/  - manage captchas
