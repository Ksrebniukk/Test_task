import math
import unittest
from main import Square, Rectangle, Circle

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

if __name__ == "__main__":
    unittest.main()
