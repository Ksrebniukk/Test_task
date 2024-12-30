import math

class Shape:
    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.width = abs(x2 - x1)
        self.height = abs(y2 - y1)

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(0, 0, side, side)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.a, self.b, self.c = self.sides()

    def sides(self):
        a = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        b = math.sqrt((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)
        c = math.sqrt((self.x1 - self.x3)**2 + (self.y1 - self.y3)**2)
        return a, b, c

    def height(self):
        p = (self.a + self.b + self.c)/2
        h = (2 / self.a * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))
        return h

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

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



