import math

diameter = float(input("Enter the diameter of the circle: "))

radius = diameter / 2
area = math.pi * radius ** 2
circumference = math.pi * diameter

print(f"Area of the circle is: {area:.2f}")
print(f"Circumference of the circle is: {circumference:.2f}")