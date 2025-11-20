import math
class Shape:
    def area(self):
        return 0
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
print("Area Calculations:)
b = float(input("Enter base of triangle: "))
h = float(input("Enter height of triangle: "))
triangle = Triangle(b, h)
print(f"Area of Triangle: {triangle.area():.2f}")
l = float(input("\nEnter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
rectangle = Rectangle(l, w)
print(f"Area of Rectangle: {rectangle.area():.2f}")
r = float(input("\nEnter radius of circle: "))
circle = Circle(r)
print(f"Area of Circle: {circle.area():.2f}")
