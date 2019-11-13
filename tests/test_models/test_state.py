#!/usr/bin/python3
"""
Test State
"""

import unittest
from models.state import state


class test_state(Unittest.Unittest):
    """
    test state
    """

    def check_name(self):
        """ check for state name input """
        my_model = BaseModel()
        my_model.name = "Holberton"

