#!/usr/bin/python3
""" This module contains the Base class """


import json
from os.path import exists


class Base:
    """ This is the base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiates the id attribute """
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    #def __del__(self):
        #type(self).__nb_objects -= 1

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        f = open(cls.__name__ + '.json', 'w', encoding='utf-8')
        if not list_objs:
            f.write('[]')
        else:
            dct_list = []
            for obj in list_objs:
                dct_list.append(obj.to_dictionary())

            s = Base.to_json_string(dct_list)

            f.write(s)

        f.close()

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if not json_string or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        r = cls(10, 5, 0, 0)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        if not exists(cls.__name__ + '.json'):
            return []
        else:
            with open(cls.__name__ + '.json', encoding='utf-8') as f:
                json_str = f.read()
                dct_list = cls.from_json_string(json_str)
                obj_list = []
                for dct in dct_list:
                    obj_list.append(cls.create(**dct))
                return obj_list
