import math

class Shape:
    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.width = abs(x2 - x1)
        self.height = abs(y2 - y1)

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

def process_shape_data(input_data):
    shapes = []
    for line in input_data:
        parts = line.split()
        shape_type = parts[0]

        if shape_type == "Square":
            side = float(parts[5])
            shape = Square(side)
        elif shape_type == "Rectangle":
            x1, y1 = float(parts[2]), float(parts[3])
            x2, y2 = float(parts[5]), float(parts[6])
            shape = Rectangle(x1, y1, x2, y2)
        elif shape_type == "Circle":
            radius = float(parts[5])
            shape = Circle(radius)
        else:
            continue

        shapes.append(shape)
    return shapes

def print_shape_info(shapes):
    for shape in shapes:
        print(f"{shape.__class__.__name__} Perimeter {shape.perimeter():.2f} Area {shape.area():.2f}")

if __name__ == "__main__":
    input_data = [
        "Square TopRight 1 1 Side 1",
        "Rectangle TopRight 2 2 BottomLeft 0 0",
        "Circle Center 1 1 Radius 2"
    ]

    shapes = process_shape_data(input_data)
    print_shape_info(shapes)




