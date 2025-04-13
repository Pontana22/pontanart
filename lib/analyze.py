import os
import cv2 as cv
import numpy as np

from PIL import Image, ImageDraw, ImageFont
from lib.interpolate import get_interp

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

    return(pixels)
        
def visual_sort(characters: str, resolution: int, font_path: str):
    character_weights = analyze(characters, resolution, font_path)
    
    interp = get_interp(0, 255, min(character_weights), max(character_weights))
    target_vals = list(map(interp, range(256)))
    possible_indexes = range(len(character_weights))
    mapped_characters = ''
        
    for i in reversed(target_vals):
        index = min(possible_indexes, key=lambda j: abs(character_weights[j]-i))
        mapped_characters += characters[index]

    return(mapped_characters)

def linear_sort(characters: str, resolution: int, font_path: str):
    character_weights = analyze(characters, resolution, font_path)
    
    sorted_tuples = sorted(zip(character_weights, characters), reverse=True)
    sorted_characters = ''
    
    for tuple in sorted_tuples:
        sorted_characters += tuple[1]
    
    return(sorted_characters)
