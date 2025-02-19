import os
import cv2 as cv
import numpy as np

from PIL import Image, ImageDraw, ImageFont

# sorts the characters in a given string
def analyze(characters: str, resolution: int, font_path: str):
    font = ImageFont.truetype(font=font_path, size=resolution)
    pixels = []

    for char in characters:
        image = Image.new(mode='L', size=(resolution, resolution), color=255)
        canvas = ImageDraw.Draw(im=image, mode='L')

        canvas.text(xy=(0, 0), text=char, fill=0, font=font)
        image.save(fp='character.bmp', format='BMP')

        image_data = cv.imread('character.bmp', cv.IMREAD_GRAYSCALE)
        pixels.append(int(np.sum(image_data != 255)))

    os.remove('character.bmp')

    sorted_tuples = sorted(zip(pixels, characters), reverse=True)

    sorted_characters = ''
    for tuple in sorted_tuples : sorted_characters += tuple[1]

    return(sorted_characters)
