from operator import itemgetter

from lib.analyze import visual_sort, linear_sort
from lib.image_conversion import get_min_max, convert_image
from lib.login import login
from lib.create_document import create_document

def process_characters(mode, characters, resolution, font):
    if mode.startswith('visual'):
        return(visual_sort(characters, resolution, font))
    elif mode.startswith('linear'):
        return(linear_sort(characters, resolution, font))
    else:
        return(characters)

def convert(options: dict, root_dir: str):  
    mode, image, characters, row_length, analysis_resolution, analysis_font = itemgetter(
        'mode', 'img', 'characters', 'row_length', 'analysis_resolution', 'analysis_font')(options)

    characters_processed = process_characters(mode, characters, analysis_resolution, analysis_font)
    min_val, max_val = get_min_max(image, row_length) if 'adaptive' in mode else (0, 255)

    content = convert_image(image, characters_processed, row_length, min_val, max_val)
    
    try:
        credentials = login(root_dir)
    except FileNotFoundError:
        exit('credentials.json not found; see README.md for more info')
    
    create_document(credentials, content, options)
