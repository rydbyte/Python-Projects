from PIL import Image, ImageOps

# Ordered from darkest (sparse) to lightest (dense) visual weight
ASCII_CHARACTERS = list(" .'`^,:;Ii!l><-~+?][}{1)(|\\/Q0OZmwqpdbkhao#MW&8%B$@")

NEW_WIDTH = 120  # bump this up/down for more/less detail

def RESIZE_IMAGE(IMAGE):
    WIDTH, HEIGHT = IMAGE.size
    RATIO = HEIGHT / WIDTH
    NEW_HEIGHT = int(RATIO * NEW_WIDTH * 0.45)  # 0.45 compensates for character aspect ratio
    return IMAGE.resize((NEW_WIDTH, NEW_HEIGHT))

def GRAYSCALE_IMAGE(IMAGE):
    return ImageOps.autocontrast(ImageOps.grayscale(IMAGE).convert("L"))  # stretches contrast to use full 0-255 range

def PIXELS_TO_ASCII(IMAGE):
    PIXELS = IMAGE.getdata()
    SCALE = len(ASCII_CHARACTERS) - 1
    CHARACTERS = "".join(ASCII_CHARACTERS[PIXEL * SCALE // 255] for PIXEL in PIXELS)
    return CHARACTERS

PATH = input("Enter a valid pathname to an image: \n")

try:
    IMAGE = Image.open(PATH)
    NEW_IMAGE = PIXELS_TO_ASCII(GRAYSCALE_IMAGE(RESIZE_IMAGE(IMAGE)))

    PIXEL_COUNT = len(NEW_IMAGE)
    ASCII_IMAGE = "\n".join(NEW_IMAGE[i:(i + NEW_WIDTH)] for i in range(0, PIXEL_COUNT, NEW_WIDTH))

    print(ASCII_IMAGE)

except Exception as e:
    print(PATH, "is not a valid pathname to an image.", e)