import os
from lib.parse_arguments import parse_arguments
from lib.userinput import process_arguments
from lib.convert import convert

if __name__ == '__main__':
    
    arguments = parse_arguments()
    root_dir = os.path.abspath(os.path.dirname(__file__))
    options = process_arguments(arguments, root_dir)

    match arguments.command: 
        case 'preset':
            exit(f'preset {arguments.name} successfully created')
        case 'convert':
            convert(options, root_dir)
        