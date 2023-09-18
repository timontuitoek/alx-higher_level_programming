import unittest
""" importing unitest"""


from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        rect = Rectangle(5, 4, 1, 2, 10)

        # check if the area calculation is correct
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 10)

    def test_area(self):
        rect = Rectangle(5, 4)

        self.assertEqual(rect.perimeter(), 18)


if __name__ == '__main':
    unittest.main()
