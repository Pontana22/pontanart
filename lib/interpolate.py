def get_interp(left_min: int, left_max: int, right_min: int, right_max: int): 
    left_span = left_max - left_min
    right_span = right_max - right_min
    scale_factor = float(right_span) / float(left_span)
    
    interp_fn = lambda value: right_min + (value-left_min)*scale_factor
    
    return(interp_fn)