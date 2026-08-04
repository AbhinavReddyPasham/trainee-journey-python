from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
def print_area(shape):
    print(f"{shape.__class__.__name__} Area = {shape.area():.2f}")

def main():
    circle = Circle(5)
    rectangle = Rectangle(10, 4)
    shapes = [circle, rectangle]
    for shape in shapes:
        print_area(shape)
main()
