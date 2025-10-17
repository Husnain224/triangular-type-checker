# triangle_type.py
import math

def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def triangle_type(a, b, c):
    if not is_valid_triangle(a, b, c):
        return "Invalid Triangle"

    # Side type
    if a == b == c:
        side_type = "Equilateral"
    elif a == b or b == c or a == c:
        side_type = "Isosceles"
    else:
        side_type = "Scalene"

    # Angle type (using Pythagorean theorem)
    sides = sorted([a, b, c])
    x, y, z = sides
    if x**2 + y**2 == z**2:
        angle_type = "Right"
    elif x**2 + y**2 > z**2:
        angle_type = "Acute"
    else:
        angle_type = "Obtuse"

    return f"{side_type} and {angle_type} Triangle"

# Take input from user
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

print(triangle_type(a, b, c))
