import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def setUp(self):
        # Base._Base__nb_objects = 0
        pass

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        rect = Rectangle(10, 7, 2, 8, 22)
        dictionary = rect.to_dictionary()
        json_dct = '[{"x": 2, "y": 8, "id": 22, "height": 7, "width": 10}]'
        self.assertEqual(Base.to_json_string([dictionary]), json_dct)

        sq = Square(5, 3, 3, 88)
        dictionary = sq.to_dictionary()
        json_dct = '[{"id": 88, "x": 3, "size": 5, "y": 3}]'
        self.assertEqual(Base.to_json_string([dictionary]), json_dct)

        sq = Square(15, 4, 4, 66)
        self.assertEqual(Base.to_json_string([]), "[]")

        sq = Square(15, 4, 4, 66)
        self.assertEqual(Base.to_json_string(None), "[]")
