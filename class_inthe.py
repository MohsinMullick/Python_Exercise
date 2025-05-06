class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2


class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print(f"Area of Triangle: {area}")


class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print(f"Area of Rectangle: {area}")  # Fixed the shape name here


# Example usage
t1 = Triangle(10, 20)
t1.area()  # Output: Area of Triangle: 100.0

r1 = Rectangle(10, 20)
r1.area()  # Output: Area of Rectangle: 200