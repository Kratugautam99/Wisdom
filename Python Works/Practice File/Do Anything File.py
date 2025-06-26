from abc import ABC, abstractmethod
import math
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c
class Quadrilateral(Polygon):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d
class Pentagon(Polygon):
    def __init__(self, side):
        self.side = side
    def area(self):
        return (5 * self.side ** 2) / (4 * math.tan(math.pi / 5))
    def perimeter(self):
        return 5 * self.side
class Hexagon(Polygon):
    def __init__(self, side):
        self.side = side
    def area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2
    def perimeter(self):
        return 6 * self.side
class Octagon(Polygon):
    def __init__(self, side):
        self.side = side
    def area(self):
        return 2 * (1 + math.sqrt(2)) * self.side ** 2
    def perimeter(self):
        return 8 * self.side
class IsoscelesTriangle(Triangle):
    def __init__(self, equal_side, base):
        super().__init__(equal_side, equal_side, base)
class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
class Rectangle(Quadrilateral):
    def __init__(self, width, height):
        super().__init__(width, height, width, height)
    def area(self):
        return self.a * self.b
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
def create_polygon():
    polygon_type = input("Enter polygon type (Triangle, Quadrilateral, Pentagon, Hexagon, Octagon, IsoscelesTriangle, EquilateralTriangle, Rectangle, Square): ")
    if polygon_type == "Triangle":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        return Triangle(a, b, c)
    elif polygon_type == "Quadrilateral":
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = float(input("Enter side c: "))
        d = float(input("Enter side d: "))
        return Quadrilateral(a, b, c, d)
    elif polygon_type == "Pentagon":
        side = float(input("Enter side: "))
        return Pentagon(side)
    elif polygon_type == "Hexagon":
        side = float(input("Enter side: "))
        return Hexagon(side)
    elif polygon_type == "Octagon":
        side = float(input("Enter side: "))
        return Octagon(side)
    elif polygon_type == "IsoscelesTriangle":
        equal_side = float(input("Enter equal side: "))
        base = float(input("Enter base: "))
        return IsoscelesTriangle(equal_side, base)
    elif polygon_type == "EquilateralTriangle":
        side = float(input("Enter side: "))
        return EquilateralTriangle(side)
    elif polygon_type == "Rectangle":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        return Rectangle(width, height)
    elif polygon_type == "Square":
        side = float(input("Enter side: "))
        return Square(side)
    else:
        print("Invalid polygon type.")
        return None
def main():
    polygon = create_polygon()
    if polygon:
        print(f"Area: {polygon.area()}")
        print(f"Perimeter: {polygon.perimeter()}")
if __name__ == "__main__":
    main()
