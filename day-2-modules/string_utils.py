
import math

def halve_string(input_string):
    # global math
    char = len(input_string)
    x = (input_string[0:math.ceil(char/2)])
    y = (input_string[math.ceil(char/2):char])
    return(x,y)


