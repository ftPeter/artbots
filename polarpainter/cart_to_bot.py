import math

def cartbot (x,y):
    #input is cartesian x y starting at the top left of the board
    #return value is length of left and right strings
    distance_between_robots =32 #values in inches
    left_length = math.sqrt(x*x + y*y)
    right_length = math.sqrt((2-x)*(2-x) + y*y)
    return left_length, right_length

