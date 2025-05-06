class Triangle:
    def __init__(self, base, height):  # Fixed: Added space between def and __init__
        self.base = base
        self.height = height

    def calculate_area(self):  # Fixed: Corrected spelling of "calculate"
        area = 0.5 * self.base * self.height  # Fixed: Used self.base and self.height
        print(f"Area: {area}")


t1 = Triangle(10, 20)
t1.calculate_area()  # Fixed: Corrected method name

t2 = Triangle(20, 30)
t2.calculate_area()  # Fixed: Corrected method name
