"""
Exercise 2: Shape Hierarchy
Design Shape Hierarchy Class
Problem: Build a shape hierarchy where the base class provides a shared describe() method, and each child class implements its own area() and perimeter() methods.

Requirements:

Base Shape class with a name field (protected). A describe() method that prints "Shape: [name], Area: [area], Perimeter: [perimeter]". 
Abstract-like area() and perimeter() methods that return 0 by default.

Circle: takes a radius. Area = pi r^2, Perimeter = 2 pi * r.
Rectangle: takes width and height. Area = w h, Perimeter = 2 (w + h).
describe() should work for any shape without modification because it calls area() and perimeter() internally.
"""
from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self) -> None:
        print(
            f"Shape: {self._name}, "
            f"Area: {self.area():.2f}, "
            f"Perimeter: {self.perimeter():.2f}"
        )


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__("Circle")
        self._radius = radius

    def area(self) -> float:
        return pi * self._radius ** 2

    def perimeter(self) -> float:
        return 2 * pi * self._radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle")
        self._width = width
        self._height = height

    def area(self) -> float:
        return self._width * self._height

    def perimeter(self) -> float:
        return 2 * (self._width + self._height)


circle = Circle(5)
rectangle = Rectangle(4, 6)

circle.describe()
rectangle.describe()