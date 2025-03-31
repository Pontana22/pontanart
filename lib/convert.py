from lib.analyze import analyze
from lib.image_conversion import get_min_max, convert_image
from lib.login import login
from lib.create_document import create_document

def convert(options: dict, root_dir: str):
    characters_sorted = analyze(options['characters'], options['analysis_resolution'], options['analysis_font'])
        
    match options['mode']:
        case 'full':
            min_val, max_val = get_min_max(options['img'], options['row_length'])
            content = convert_image(options['img'], characters_sorted, options['row_length'], min_val, max_val)
        case 'map':
            content = convert_image(options['img'], characters_sorted, options['row_length'], 0, 255)
    
    try:
        credentials = login(root_dir)
    except FileNotFoundError:
        exit('credentials.json not found; see README.md for more info')
    
    create_document(credentials, content, options)
    