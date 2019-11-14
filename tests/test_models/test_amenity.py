#!/usr/bin/python3
"""
Test Amenity
"""

import unittest
from models.base_model import BaseModel
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

    def test_class(self):
        """
        Test class
        """
        assertEqual(Amenity.name, "")
        assertTrue(issubclass(Amenity, BaseModel))

    def test_instance(self):
        """
        Test instance
        """
        my_amenity = Amenity()
        assertEqual(my_amenity.name, "")
        assertTrue(isinstance(my_amenity, BaseModel))
