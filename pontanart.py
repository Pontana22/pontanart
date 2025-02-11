import argparse
import json
import os

def process_arguments(arguments: argparse.Namespace):
    options = vars(arguments)

    fill_options = load_preset(options['preset']) # if no preset was specified, default.json will be loaded

    for key, value in options.items():
        if value == None and key != 'preset':
            options[key] = fill_options[key]

    font = locate_file(options['analysis_font'], fonts_folder, ['.ttf'])

    if font == None:
        exit(f'specified analysis font {arguments.analysis_font} was either not found or not a .ttf')
    else:
        if arguments.command == 'preset':
            save_preset(options, arguments.name)
        elif arguments.command == 'convert':
            options['analysis_font'] = font

            image_types = ['.bmp', '.dib', '.jpeg', '.jpg', '.png', '.webp', '.sr', '.ras', '.tiff', '.tif']
            image = locate_file(options['img'], img_folder, image_types)

            if image == None:
                exit(f'image {options['img']} was either not found or an unsupported file type')
            else:
                options['img'] = image

            return(options)


def save_preset(options: dict, filename: str):
    keys = ['mode', 'characters', 'font_family', 'font_size', 'row_length', 'row_spacing', 'analysis_resolution', 'analysis_font']
    save = {key: options[key] for key in keys}

    if not filename.endswith('.json'):
        filename += '.json'

    path = os.path.join(presets_folder, filename)

    with open(path, 'w') as file:
        json.dump(save, file, indent=4)


def load_preset(filename: str):
    if filename == None:
        path = locate_file('default', presets_folder, ['.json'])
    else:
        path = locate_file(filename, presets_folder, ['.json'])

    if path == None and filename == None:
        exit('default settings not found')
    elif path == None:
        exit(f'preset {filename} not found')

    with open(path, 'r') as file:
        return(json.load(file))


def locate_file(filename: str, directory: str, filetypes: list):
    if os.path.isfile(filename):
        return filename
    else:
        for file in os.listdir(directory):
            if file == filename:
                return(os.path.join(directory, filename))
            elif file.startswith(filename):
                for filetype in filetypes:
                    if file == filename + filetype:
                        return(os.path.join(directory, filename + filetype))


if __name__ == '__main__':
    parser = argparse.ArgumentParser( # main parser
        usage='pontanart.py [options] {convert,preset} <arguments>',
        description='Recommended characters: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ " (including space)',
        epilog='see README.md for more info'
    )

    # optional arguments
    parser.add_argument( # mode
        '-m', '--mode',
        type=str,
        choices=['full', 'map', 'full_lines'],
        help='conversion mode', metavar=''
    )
    parser.add_argument( # characters
        '-c', '--characters',
        type=str,
        help='the characters to be used',
        metavar=''
    )
    parser.add_argument( # characters
        '-ff', '--font-family',
        type=str,
        help='',
        metavar=''
    )
    parser.add_argument( # font size
        '-fs', '--font-size',
        type=int,
        help='document font size',
        metavar=''
    )
    parser.add_argument( # row length
        '-rl', '--row-length',
        type=int,
        help='number of characters per row',
        metavar=''
    )
    parser.add_argument( # row spacing
        '-rs', '--row-spacing',
        type=int,
        help='document row spacing',
        metavar=''
    )
    parser.add_argument( # analysis resolution
        '-ar', '--analysis-resolution',
        type=int,
        help='image resolution used during font analysis, NOTE: changing this is likely of no use, just leave it',
        metavar=''
    )
    parser.add_argument( # analysis font file
        '-af', '--analysis-font',
        type=str,
        help='font to be used during font analysis (filename of font in the fonts folder or path to font elsewhere)',
        metavar=''
    )
    parser.add_argument( # preset file
        '-p', '--preset',
        type=str,
        help='preset to be used (filename of preset in the presets folder or path to preset elsewhere), NOTE: will get overridden by any other settings',
        metavar=''
    )

    subparsers = parser.add_subparsers(
        dest='command',
        help='commands'
    )

    # commands
    conversion_parser = subparsers.add_parser( # convert
        'convert',
        usage='pontanart.py [options] convert img docname',
        help='convert image to document'
    )
    preset_parser = subparsers.add_parser( # preset
        'preset',
        usage='pontanart.py [options] preset name',
        help='create preset'
    )

    # conversion specific positional arguments
    conversion_parser.add_argument( # image
        'img',
        type=str,
        help='image to be converted (filename of image in the img folder or path to image elsewhere)'
    )
    conversion_parser.add_argument( # document name
        'docname',
        type=str,
        help='what to name the google document'
    )

    # preset creation specific positional arguments
    preset_parser.add_argument( # preset name
        'name',
        type=str,
        help='what to name the preset'
    )

    root_directory = os.path.abspath(os.path.dirname(__file__))
    fonts_folder = os.path.join(root_directory, 'fonts')
    img_folder = os.path.join(root_directory, 'img')
    lib_folder = os.path.join(root_directory, 'lib')
    presets_folder = os.path.join(root_directory, 'presets')

    arguments = parser.parse_args()
    options = process_arguments(arguments)

    if arguments.command == 'preset':
        exit(f'preset {arguments.name} successfully created')

    for key, val in options.items():
        print(key + ':' + ' '*(25 - len(key)), repr(val))
