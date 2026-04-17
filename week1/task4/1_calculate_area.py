# basic function - finding area of a circle
import math
def calculate_area(radius):
    area = math.pi * radius * radius
    return round(area, 2)  # rounding to 2 decimal places
# testing with different values
print("Area with radius 5:", calculate_area(5))
print("Area with radius 7:", calculate_area(7))
#testing with my own value
r = 10
print(f"circle with radius {r} has area:", calculate_area(r))