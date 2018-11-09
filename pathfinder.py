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




def get_maximum_elevation(list):
    # highest_ints_in_list = []
    # for row in list:
    #     highest_ints_in_list.append(max(row))
    # this is the original for loop that was transformed into a list comprehension beginning on line 22

    highest_ints_in_list = [max(row) for row in list]
    highest_point = max(highest_ints_in_list)
    print(highest_point)
    return highest_point
highest_elevation = get_maximum_elevation(elevation_list)
    

def get_minimum_elevation(list):
    lowest_ints_in_list = [min(row) for row in list]
    lowest_point = min(lowest_ints_in_list)
    print(lowest_point)
    return lowest_point
lowest_point = get_minimum_elevation(elevation_list)


# highest_elevation_pixel_color = ("RGB", 255, 255, 255)
# #white
# lowest_elevation_pixel_color = ("RGB", 0, 0, 0)
# #black

this_image = Image.new("RGB", (3000, 600), (125, 125, 125))
this_image.save("this_image.png")
this_image.show("this_image.png")

def draw_point(coords, color)
    image.putpixel(coords, color)

draw_point(([50][300]), (125, 125, 125)

 
# def determine_pixel_color(list):
#     """
#     Takes elevation, divides by highest elevation, multiplies that by 255 and rounds to the nearest whole number-- this gives us a number between 0 and 255 to determine color intensity at pixel point in map.
#     """
#     color_formula = round(elevation_list[1][3] / highest_elevation * 255)
#     color_intensity = [color_formula(item) for item in elevation_list]
#     print(color_intensity)   

# determine_pixel_color(list=elevation_list[0][1:3])
    

        


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