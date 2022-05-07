
# Project: eRUT image validator
# Objective: Create object in charge of validation (EValidator)

# input
rut personal
not in qr data, 
issue: need to reconstruct api for getting missing data
solutions:
    1. run apk and monitor network -- https://stackoverflow.com/questions/20778072/sniffing-an-android-app-to-find-api-url
    2. run script that extract api -- https://github.com/alessandrodd/apk_api_key_extractor
    3. reverse engineer source code to rebuild api  -- https://medium.com/@thomas_shone/reverse-engineering-apis-from-android-apps-part-1-ea3d07b2a6c


rut empresa
imagen base64 (.png/.jpg/.jpeg)

# blackbox
Manage base64img byte string to extract qr code & scan - done
Validate - in progress

    1. issue -- rut personal not in qr data (valid), need to reconstruct api for getting missing data and validate all
    solutions:
        a. run apk and monitor network -- https://stackoverflow.com/questions/20778072/sniffing-an-android-app-to-find-api-url
        b. run script that extract api -- https://github.com/alessandrodd/apk_api_key_extractor
        c. reverse engineer source code to rebuild api  -- https://medium.com/@thomas_shone/reverse-engineering-apis-from-android-apps-part-1-ea3d07b2a6c

    2. nombre personal
    3. rut empresa
    4. ...



# output
error - image blur
true - correct validation - input == validation return data
false - incorrect validation - input != validation return data



# Related
https://www.sii.cl/destacados/erut/  - main homepage
https://2captcha.com/  - manage captchas
