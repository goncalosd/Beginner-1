# This programs calculates the area of a circle given its radius.
import math


def area_circle():
    r = float(input('Enter radius of circle: '))
    area = round(math.pi*(r**2), 2)
    print('A circle with radius ' + str(r) + ' has an area of ' + str(area))


print('''This program will give you the area of a circle given its radius.
''')
area_circle()
