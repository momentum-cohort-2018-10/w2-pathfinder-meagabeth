import csv

elevation = []

with open ('numbers_small.txt') as file:
    number_reader = csv.reader(file)
    for line in number_reader:
        elevation.append((line[0], line[1]))

# print(elevation)


# data = []

# with open('GeoLite2-City-Blocks-IPv6.csv') as file:
#     geolite_reader = csv.reader(file)
#     for row in geolite_reader:
#         data.append((row[0], row[7], row[8]))


# numbers = [
# [3, 5, 8],
# [6, 3, 9], 
# [1, 4, 8]
# ]

# print(numbers[0][2])