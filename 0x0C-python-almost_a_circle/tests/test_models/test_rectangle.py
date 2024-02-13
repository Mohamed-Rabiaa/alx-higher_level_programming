import unittest
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch, call


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10, 5, 5)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        # del self.r1
        # del self.r2
        pass

    def test_attributes(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)
        # self.assertEqual(self.r1.id, 1)

        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r2.x, 5)
        self.assertEqual(self.r2.y, 5)
        # self.assertEqual(self.r2.id, 2)

        self.assertEqual(self.r3.width, 10)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(self.r3.id, 12)

    def test_setters(self):
        self.r1.width = 20
        self.r1.height = 50
        self.r1.x = 8
        self.r1.y = 6

        self.assertEqual(self.r1.width, 20)
        self.assertEqual(self.r1.height, 50)
        self.assertEqual(self.r1.x, 8)
        self.assertEqual(self.r1.y, 6)

        with self.assertRaises(TypeError):
            self.r1.width = "2"
        with self.assertRaises(ValueError):
            self.r1.width = -1

        with self.assertRaises(TypeError):
            self.r1.height = "5"
        with self.assertRaises(ValueError):
            self.r1.height = 0

        with self.assertRaises(TypeError):
            self.r1.x = 5.5
        with self.assertRaises(ValueError):
            self.r1.x = -2

        with self.assertRaises(TypeError):
            self.r1.y = []
        with self.assertRaises(ValueError):
            self.r1.y = -4

    def test_area(self):
        self.r1.width = 5
        self.r1.height = 10
        self.assertEqual(self.r1.area(), 50)

    def test_display(self):
        self.r1.width = 3
        self.r1.height = 2

        with patch('builtins.print') as mocked_print:
            self.r1.display()
            expected_calls = [call('', end=''), call('', end=''), call('###'),
                              call('', end=''), call('###')]
            mocked_print.assert_has_calls(expected_calls)

    def test___str__(self):
        self.r1 = Rectangle(6, 2, 1, 1, 15)

        s = "[Rectangle] (15) 1/1 - 6/2"
        self.assertEqual(self.r1.__str__(), s)

        self.r2 = Rectangle(7, 4, id=20)
        s = "[Rectangle] (20) 0/0 - 7/4"
        self.assertEqual(self.r2.__str__(), s)

    def test_update(self):
        self.r1 = Rectangle(10, 10, 10, 10, 10)

        self.r1.update(11)
        self.assertEqual(self.r1.id, 11)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        self.r1.update(11, 22)
        self.assertEqual(self.r1.id, 11)
        self.assertEqual(self.r1.width, 22)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        self.r1.update(11, 20, 12)
        self.assertEqual(self.r1.id, 11)
        self.assertEqual(self.r1.width, 20)
        self.assertEqual(self.r1.height, 12)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        self.r1.update(11, 9, 7, 12)
        self.assertEqual(self.r1.id, 11)
        self.assertEqual(self.r1.width, 9)
        self.assertEqual(self.r1.height, 7)
        self.assertEqual(self.r1.x, 12)
        self.assertEqual(self.r1.y, 10)

        self.r1.update(13, 25, 15, 5, 5)
        self.assertEqual(self.r1.id, 13)
        self.assertEqual(self.r1.width, 25)
        self.assertEqual(self.r1.height, 15)
        self.assertEqual(self.r1.x, 5)
        self.assertEqual(self.r1.y, 5)

        self.r1 = Rectangle(10, 10, 10, 10, 10)

        self.r1.update(id=5)
        self.assertEqual(self.r1.id, 5)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        self.r1.update(id=5, width=12)
        self.assertEqual(self.r1.id, 5)
        self.assertEqual(self.r1.width, 12)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        self.r1.update(id=5, width=12, height=18)
        self.assertEqual(self.r1.id, 5)
        self.assertEqual(self.r1.width, 12)
        self.assertEqual(self.r1.height, 18)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        self.r1.update(id=5, width=12, height=18, x=1)
        self.assertEqual(self.r1.id, 5)
        self.assertEqual(self.r1.width, 12)
        self.assertEqual(self.r1.height, 18)
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r1.y, 10)

        self.r1.update(id=5, width=12, height=18, x=1, y=2)
        self.assertEqual(self.r1.id, 5)
        self.assertEqual(self.r1.width, 12)
        self.assertEqual(self.r1.height, 18)
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r1.y, 2)

    def test_to_dictionary(self):
        self.r1 = Rectangle(5, 7, 4, 4, 55)
        dct = {'y': 4, 'width': 5, 'x': 4, 'id': 55, 'height': 7}
        self.assertEqual(self.r1.to_dictionary(), dct)
