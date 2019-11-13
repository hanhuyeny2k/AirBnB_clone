#!/usr/bin/python3
"""
Test Amenity
"""

import unittest
from models.amenity import amenity


class test_amenity(Unittest.Unittest):
    """
    test amenity
    """

    def check_name(self):
        """ check for amenity input """
        my_model = BaseModel()
        my_model.name = "Holberton"

