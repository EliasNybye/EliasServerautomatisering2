def list_ends(input_list):
    if not input_list:
        return None, None
    return input_list[0,3,4,6], input_list[-1,-2]
