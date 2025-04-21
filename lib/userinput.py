import json

def process_options(options: dict):
    with open('./resources/default_options.json', 'r') as file:
        default = json.load(file)
    
    if not options['characters']:
        options['characters'] = default[options['mode']]
        options['mode'] = 'fixed' # since the characters are pre-processed there is no need for analysis
        
    if options.get('adaptive'):
        options['mode'] += '-adaptive'
        
    other_keys = [
        'font_family',
        'font_size',
        'row_length',
        'row_spacing',
        'analysis_resolution',
        'analysis_font'
    ]
    
    for key in other_keys:
        if not options.get(key):
            options[key] = default[key]
            
        elif type(options[key]) is str and options[key].isnumeric():
            options[key] = int(options[key])
