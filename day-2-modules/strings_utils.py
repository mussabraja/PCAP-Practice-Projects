import string_utils

def halve_strings(string_list):
    result = []
    for s in string_list:
        result.append(string_utils.halve_string(s))
    return result

