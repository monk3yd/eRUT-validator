import base64
from validator import EValidator


def main():
    # Input data to be validated
    # RUT_PERSONAL
    RUT_EMPRESA = "76.745.604-2"

    # Testing --- Create base64 encoded image from png file
    with open("test/image.png", "rb") as raw_image:
        base64img = base64.b64encode(raw_image.read())

    # Blackbox --- Validate data
    validator = EValidator(base64img, RUT_EMPRESA)


if __name__ == "__main__":
    main()
