import cv2 as cv
import numpy as np

def convert_image(image_path: str, characters: str, row_length: int, min: int, max: int):
    image = open_resize(image_path, row_length)
    output = ''
    input_range = max - min
    output_range = (len(characters) - 1)
    
    for row in image:
        
        for val in row:
            character_index = int(round(((val - min) / input_range) * output_range))
            output += characters[character_index]

        output += '\n'

    return(output)

def get_min_max(image_path: str, row_length: int):
    image = open_resize(image_path, row_length)
    image_values = np.array(image)
    return(image_values.min(), image_values.max())

def open_resize(image_path: str, row_length: int):
    image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    num_rows = int(len(image) * (row_length / len(image[0])))
    resized = cv.resize(image, (row_length, num_rows))
    return(resized)
