import argparse
import os
import json

def process_options(options: dict):
    if options.get('adaptive'):
        options['mode'] += '-adaptive'
    
    options['font_size'] = verify_int(options['font_size'], 3)
    options['row_length'] = verify_int(options['row_length'], 250)
    options['row_spacing'] = verify_int(options['row_spacing'], 60)
    
    if not options['characters']:
        options['characters'] = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
        
    options['font_family'] = 'Courier Prime'
    options['analysis_resolution'] = 1000
    options['analysis_font'] = './fonts/CourierPrime-Regular.ttf'

def verify_int(val, default_val):
    if val:
        return int(val)
    else:
        return default_val
    