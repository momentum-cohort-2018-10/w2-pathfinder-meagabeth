# import csv
import random
# import pdb
# from PIL import Image


with open("elevation_small.txt", 'r') as f:
    all_elevations = [line.strip('\n').split() for line in f]
    print(all_elevations[0][1])

elevation_list = [[int(elevation) for elevation in row] for row in all_elevations]
print (elevation_list[0][0:2])
print (elevation_list[3][1:4])
print(len(elevation_list[0]))

def get_maximum_elevation(list):
    # highest_ints_in_list = []
    # for row in list:
    #     highest_ints_in_list.append(max(row))
    # this is the original for loop that was transformed into a list comprehension beginning on line 22

    highest_ints_in_list = [max(row) for row in list]
    highest_point = max(highest_ints_in_list)
    print(highest_point)
    return highest_point
highest_point = get_maximum_elevation(elevation_list)
    
def get_minimum_elevation(list):
    lowest_ints_in_list = [min(row) for row in list]
    lowest_point = min(lowest_ints_in_list)
    print(lowest_point)
    return lowest_point
lowest_point = get_minimum_elevation(elevation_list)

"""
this_image = Image.new("RGB", (600, 600), (125, 125, 125))
# this creates a new image ("this_image.png") that is 600px x 600px and is color 125 all over
this_image.save("this_image.png")
# we save the image file
this_image.show("this_image.png")
# we show the image file (aka open it up when run)
"""

def elevation_to_color_formula(number):
    """
    This function takes a number, runs it through the formula and returns it as an absolute value rounded number somwhere between 0-255.
    """
    color_intensity = abs(round(((number - lowest_point) / (highest_point - lowest_point)) * 255))
    return color_intensity
# create a new list of color intensities by looping over the list of elevations and applying the formula
intensity_list = [[elevation_to_color_formula(number) for number in row] for row in elevation_list]
print(len(intensity_list))


def print_something(list):
    map_image = Image.new("RGB", (600, 600))
    for y, row in enumerate(list):
        for x, value, in enumerate(row):
            map_image.putpixel((x, y), (value, value, value))
    map_image.save("map.png")
    map_image.show("map.png")

#the next line puts a single blue pixel at index (300,300), saves image and then shows image
    map_image.putpixel((300, 300), (0, 0, 200))
    map_image.save("map_dot.png")
    map_image.show("map_dot.png")

# the next lines put a straight blue line vertically down the middle of the image
    for x, row in (enumerate(list)):
        map_image.putpixel((x, 300), (0, 0, 200))
    map_image.save("map_vertical_line.png")
    map_image.show("map_vertical_line.png")

# print_something(intensity_list)

def starting_point():
    y = random.randint(0, 600)
    x = 0
    return (x, y)
# print(starting_point())

def next_step_options(row, elevation):
    """
    Taking the current location and returning the location & value for possible options (fwd, up; fwd; fwd, dwn) for the next step.
    """
    # y = [row for row in elevation_list]
    # x = [elevation for elevation in y]
    (x, y) = starting_point()
    print(x, y)
    step_options = {}
    
    if y == 0:
        step_options['straight'] = (x+1, y)
        step_options['down'] = (x+1, y+1)
    if y == 599:
        step_options['straight'] = (x+1, y)
        step_options['up'] = (x+1, y-1)
    else:
        step_options['straight'] = (x+1, y)
        step_options['up'] = (x+1, y-1)
        step_options['down'] = (x+1, y+1)
        # step_options['down'] = coordinates([x+1][y+1])
    # elif y == (len(elevation_list) - 1):
    #     step_options['up'] = coordinates([x+1][y-1])
    #     step_options['straight'] = coordinates([x+1][y])
    # else:
    #     step_options['up'] = (coordinates([x+1][y-1]))
    #     step_options['straight'] = coordinates([x+1][y])   
    #     step_options['down'] = coordinates([x+1][y+1])  
    print(step_options)

next_step_options(2, 1)
 
# def step_up(coordinates):
#     for y in elevation_list:
#         for x in y:
#             current_step = elevation_list[0][0]
#             step_up = (current_step[x+1][y-1])
#             return step_up

# step_up(elevation_list[2][5])

#     # if y is the top row, the options would be move fwd or dwn
#     if y == 0:
#         step_forward = ([x+1],[y])
#         step_down = elevation_list([x+1],[y+1])
#     # if y is bottom row, the options would be move fwd or up
#     elif y == (len(elevation_list) -1):
#         step_forward = ([x+1],[y])
#         step_up = ([x+1],[y-1])
#     # if y is not top or bottom row, options are move up, fwd or dwn
#     else:
#         step_forward = ([x+1],[y])
#         step_up = ([x+1],[y-1])  
#         step_down = ([])    
#         pass