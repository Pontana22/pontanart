import argparse
import os
import json

def process_arguments(arguments: argparse.Namespace, root_dir: str):
    fonts_dir = os.path.join(root_dir, 'fonts')
    img_dir = os.path.join(root_dir, 'img')
    presets_dir = os.path.join(root_dir, 'presets')

    options = vars(arguments)

    fill_options = load_preset(options['preset'], presets_dir) # if no preset was specified, default.json will be loaded

    for key, value in options.items():
        if value == None and key != 'preset':
            options[key] = fill_options[key]

    font = locate_file(options['analysis_font'], fonts_dir, ['.ttf'])

    if font == None:
        exit(f'specified analysis font {arguments.analysis_font} was either not found or not a .ttf')
    else:
        if arguments.command == 'preset':
            save_preset(options, arguments.name, presets_dir)
        elif arguments.command == 'convert':
            options['analysis_font'] = font

            image_types = ['.bmp', '.dib', '.jpeg', '.jpg', '.png', '.webp', '.sr', '.ras', '.tiff', '.tif']
            image = locate_file(options['img'], img_dir, image_types)

            if image == None:
                exit(f'image {options['img']} was either not found or an unsupported file type')
            else:
                options['img'] = image

            return(options)


def save_preset(options: dict, filename: str, presets_dir: str):
    keys = ['mode', 'characters', 'font_family', 'font_size', 'row_length', 'row_spacing', 'analysis_resolution', 'analysis_font']
    save = {key: options[key] for key in keys}

    if not filename.endswith('.json'):
        filename += '.json'

    path = os.path.join(presets_dir, filename)

    with open(path, 'w') as file:
        json.dump(save, file, indent=4)

def load_preset(filename: str, presets_dir: str):
    if filename == None:
        path = locate_file('default', presets_dir, ['.json'])
    else:
        path = locate_file(filename, presets_dir, ['.json'])

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
