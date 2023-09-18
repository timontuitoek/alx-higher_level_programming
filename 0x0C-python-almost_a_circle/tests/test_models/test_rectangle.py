import unittest
""" importing unitest"""

import io
import sys
from tests_models.base import Base
from tests_models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(2, 2, 4)
        self.r4 = Rectangle(4, 4, 2)
        self.r5 = Rectangle(1, 2, 3, 4)
        self.r6 = Rectangle(4, 3, 2, 1)

    def test_instantiation_is_base(self):
        """Test if Rectangle is an instance of Base."""
        self.assertIsInstance(self.r1, Base)

    def test_instantiation_no_args(self):
        """Test instantiation with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_instantiation_one_arg(self):
        """Test instantiation with one argument."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_id_assignment(self):
        """Test if IDs are assigned correctly."""
        self.assertEqual(self.r1.id, self.r2.id - 1)
        self.assertEqual(self.r3.id, self.r4.id - 1)
        self.assertEqual(self.r5.id, self.r6.id - 1)

    def test_area(self):
        """Test the area() method."""
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r3.area(), 4)
        self.assertEqual(self.r5.area(), 2)

    def test_update_args(self):
        """Test the update() method with positional arguments."""
        self.r1.update(5, 2, 3, 7, 1)
        self.assertEqual(self.r1.id, 5)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 7)
        self.assertEqual(self.r1.y, 1)

    def test_update_kwargs(self):
        """Test the update() method with keyword arguments."""
        self.r3.update(height=5, width=7, x=2, y=1, id=5)
        self.assertEqual(self.r3.id, 5)
        self.assertEqual(self.r3.width, 7)
        self.assertEqual(self.r3.height, 5)
        self.assertEqual(self.r3.x, 2)
        self.assertEqual(self.r3.y, 1)

    def test_to_dictionary(self):
        """Test the to_dictionary() method."""
        expected_dict = {'id': 1, 'width': 10, 'height': 2, 'x': 0, 'y': 0}
        self.assertEqual(self.r1.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
