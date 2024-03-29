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

        with self.assertRaises(TypeError):
            self.s1.size = "2"

        with self.assertRaises(ValueError):
            self.s1.size = -5

    def test_square_update(self):
        self.s1 = Square(8, 8, 8, 8)

        self.s1.update(11)
        self.assertEqual(self.s1.id, 11)
        self.assertEqual(self.s1.size, 8)
        self.assertEqual(self.s1.x, 8)
        self.assertEqual(self.s1.y, 8)

        self.s1.update(11, 17)
        self.assertEqual(self.s1.id, 11)
        self.assertEqual(self.s1.size, 17)
        self.assertEqual(self.s1.x, 8)
        self.assertEqual(self.s1.y, 8)

        self.s1.update(12, 18, 4)
        self.assertEqual(self.s1.id, 12)
        self.assertEqual(self.s1.size, 18)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s1.y, 8)

        self.s1.update(30, 8, 2, 3)
        self.assertEqual(self.s1.id, 30)
        self.assertEqual(self.s1.size, 8)
        self.assertEqual(self.s1.x, 2)
        self.assertEqual(self.s1.y, 3)

        self.s1 = Square(7, 7, 7, 7)

        self.s1.update(id=22)
        self.assertEqual(self.s1.id, 22)
        self.assertEqual(self.s1.size, 7)
        self.assertEqual(self.s1.x, 7)
        self.assertEqual(self.s1.y, 7)

        self.s1.update(id=28, size=33)
        self.assertEqual(self.s1.id, 28)
        self.assertEqual(self.s1.size, 33)
        self.assertEqual(self.s1.x, 7)
        self.assertEqual(self.s1.y, 7)

        self.s1.update(id=99, size=19, x=9)
        self.assertEqual(self.s1.id, 99)
        self.assertEqual(self.s1.size, 19)
        self.assertEqual(self.s1.x, 9)
        self.assertEqual(self.s1.y, 7)

        self.s1.update(id=14, size=20, x=2, y=2)
        self.assertEqual(self.s1.id, 14)
        self.assertEqual(self.s1.size, 20)
        self.assertEqual(self.s1.x, 2)
        self.assertEqual(self.s1.y, 2)

    def test_square_to_dictionary(self):
        self.s1 = Square(8, 1, 1, 80)
        dct = {'y': 1, 'x': 1, 'id': 80, 'size': 8}
        self.assertEqual(self.s1.to_dictionary(), dct)
