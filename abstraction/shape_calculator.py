"""
Exercise 1: Shape Calculator
Design Shape Calculator Class
Problem: Build a shape calculation system using an abstract class. The abstract Shape class has abstract methods 
for calculating area and perimeter, plus a concrete describe() method that all shapes inherit.

Requirements:

Abstract Shape class with: abstract area() and perimeter() methods, 
plus a concrete describe() method that prints "Shape: [name], Area: [area], Perimeter: [perimeter]"

Circle: takes a radius. Area = pi r^2, Perimeter = 2 pi * r
Rectangle: takes width and height. Area = w h, Perimeter = 2 (w + h)
describe() should work for any shape without modification
"""

from abc import abstractmethod, ABC
from math import pi


class Shape(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"Shape: {self.__class__.__name__}, Area: {self.area()}, Perimeter: {self.perimeter()}")


class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return pi*self.radius**2
    
    def perimeter(self):
        return 2*pi*self.radius
    
class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)
    

if __name__ == "__main__":
    circle = Circle(4)
    rectangle = Rectangle(2, 2)

    print(circle.area())
    print(circle.perimeter())
    circle.describe()

    print(rectangle.area())
    print(rectangle.perimeter())
    rectangle.describe()