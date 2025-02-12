from analyze import analyze
from image_conversion import get_min_max, convert_image
from login import login

def convert(options: dict, root_dir: str):
    characters_sorted = analyze(options['characters'], options['analysis_resolution'], options['analysis_font'])
        
    if options['mode'] == 'full':
        min_val, max_val = get_min_max(options['img'], options['row_length'])
        content = convert_image(options['img'], characters_sorted, options['row_length'], min_val, max_val)
    elif options['mode'] == 'map':
        content = convert_image(options['img'], characters_sorted, 0, 255)
    
    try:
        credentials = login(root_dir)
    except FileNotFoundError:
        exit('credentials.json not found; see README.md for more info')