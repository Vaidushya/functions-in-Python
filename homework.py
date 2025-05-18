import math

def circumference(radius):
    return 2 * math.pi * radius

radius = float(input("Enter the radius of the circle: "))
print(f"The circumference of the circle is: {circumference(radius)}")