import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.s1 = Square(5, 3)
        self.s2 = Square(7, 2, 3)
        self.s3 = Square(10, 6, 4, 8)

    def tearDown(self):
        pass

    def test_square_attributes(self):
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s1.x, 3)
        self.assertEqual(self.s1.y, 0)
        # self.assertEqual(self.s1.id, 1)

        self.assertEqual(self.s2.size, 7)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 3)
        # self.assertEqual(self.s2.id, 2)

        self.assertEqual(self.s3.size, 10)
        self.assertEqual(self.s3.x, 6)
        self.assertEqual(self.s3.y, 4)
        self.assertEqual(self.s3.id, 8)

    def test_square__str__(self):
        self.s1 = Square(14, 2, 2, 4)
        s = "[Square] (4) 2/2 - 14"
        self.assertEqual(self.s1.__str__(), s)

        self.s2 = Square(11, id=22)
        s = "[Square] (22) 0/0 - 11"
        self.assertEqual(self.s2.__str__(), s)

        self.s3 = Square(9, 6, 4, 10)
        s = "[Square] (10) 6/4 - 9"
        self.assertEqual(self.s3.__str__(), s)

    def test_square_size_setter(self):
        self.s1.size = 25
        self.assertEqual(self.s1.size, 25)
