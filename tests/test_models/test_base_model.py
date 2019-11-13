#!/usr/bin/python3
"""
Test BaseModel
"""

import unittest
from models.base_model import BaseModel


class test_BaseModel(Unittest.Unittest):
    """
    test ModelBase
    """

    def check_name(self):
        """ check for name input """
        my_model = BaseModel()
        my_model.name = "Holberton"
