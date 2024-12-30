import math
import unittest
from main import Square, Rectangle, Circle, Triangle

class TestShapes(unittest.TestCase):
    def test_square(self):
        square = Square(2)
        self.assertAlmostEqual(square.perimeter(), 8)
        self.assertAlmostEqual(square.area(), 4)

    def test_rectangle(self):
        rectangle = Rectangle(0, 0, 3, 4)
        self.assertAlmostEqual(rectangle.perimeter(), 14)
        self.assertAlmostEqual(rectangle.area(), 12)

    def test_circle(self):
        circle = Circle(1)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi)
        self.assertAlmostEqual(circle.area(), math.pi)

    def test_triangle(self):
        triangle = Triangle(0, 0, 4, 4, 0, 8)
        self.assertAlmostEqual(triangle.perimeter(), 19.31370849898476)
        self.assertAlmostEqual(triangle.area(), 15.999999999999993)

    def test_triangle2(self):
        triangle = Triangle(1, 1, 2, 2, 0, 5)
        self.assertAlmostEqual(triangle.perimeter(), 9.142870463454745)
        self.assertAlmostEqual(triangle.area(), 2.5000000000000004)


if __name__ == "__main__":
    unittest.main()
