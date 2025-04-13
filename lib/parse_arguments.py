import argparse

def parse_arguments():
    parser = argparse.ArgumentParser( # main parser
        usage='pontanart.py [options] {convert,preset} <arguments>',
        description='Recommended characters: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ " (including space)',
        epilog='see README.md for more info'
    )

    # optional arguments
    parser.add_argument( # mode
        '-m', '--mode',
        type=str,
        choices=[
            'visual', 
            'visual-adaptive', 
            'linear', 
            'linear-adaptive', 
            'fixed', 
            'fixed-adaptive'
        ],
        help='conversion mode', metavar=''
    )
    parser.add_argument( # characters
        '-c', '--characters',
        type=str,
        help='the characters to be used',
        metavar=''
    )
    parser.add_argument( # font family
        '-ff', '--font-family',
        type=str,
        help='document font, ie what the font is called in google docs, NOTE: case sensitive',
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
        default='default',
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
    
    arguments = parser.parse_args()
    
    return(arguments)