import csv
from PIL import Image
 
    # def list_of_int_lists(self, list):
# with .txt open as f, file is list of subarrays where each subarray is a line in the file
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


# highest_elevation_pixel_color = ("RGB", 255, 255, 255)
# 255 = white
# lowest_elevation_pixel_color = ("RGB", 0, 0, 0)
# 0 = black

this_image = Image.new("RGB", (600, 600), (125, 125, 125))
# this creates a new image ("this_image.png") that is 600px x 600px and is color 125 all over
this_image.save("this_image.png")
# we save the image file
this_image.show("this_image.png")
# we show the image file (aka open it up when run)

# def draw_point(coords, color):
#     image.putpixel(coords, color)
# pass




def elevation_to_color_formula(number):
    """
    This function takes a number, runs it through the formula and returns it as an absolute value rounded number somwhere between 0-255.
    """
    color_intensity = abs(round(((number - lowest_point) / (highest_point - lowest_point)) * 255))
    return color_intensity

print(elevation_to_color_formula(3139))

        


# class Pathfinder:

#     def __init__(self):
#         pass

    # def determine_greedy_path(self):

    # def choose_next_step(self):

# Image.new("RGB", (600, 3000))

# for y, row in enumerate(data):
#     for x, num in enumerate(row):
#         img.putpixel((x, y), (20, 120, 220))

# img.save('test.png')

# #find maximum elevation as top, minimum elevation as bottom, scale elevation by something in between