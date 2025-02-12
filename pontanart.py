import os
from lib.parse_arguments import parse_arguments
from lib.userinput import process_arguments
from lib.analyze import analyze
from lib.image_conversion import get_min_max, convert_image
from lib.login import login

if __name__ == '__main__':
    
    arguments = parse_arguments()
    root_dir = os.path.abspath(os.path.dirname(__file__))
    options = process_arguments(arguments, root_dir)

    if arguments.command == 'preset':
        exit(f'preset {arguments.name} successfully created')
    elif arguments.command == 'convert':
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
        
        
