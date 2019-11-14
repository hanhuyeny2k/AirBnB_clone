#!/usr/bin/python3
"""
Test Amenity
"""

import unittest
from models.amenity import Amenity
from os import getcwd, chdir
from shutil import rmtree
from tempfile import mkdtemp


class test_Amenity(unittest.TestCase):
    """
    Test Amenity
    """
    def setUp(self):
        """
        Create a temporary directory and Base instance
        """
        chdir(mkdtemp())

    def tearDown(self):
        """
        Remove temporary files and directories
        """
        rmtree(getcwd(), ignore_errors=True)

    def check_name(self):
        """
        Test instance
        """
        my_model = Amenity()
        my_model.name = "Holberton"
