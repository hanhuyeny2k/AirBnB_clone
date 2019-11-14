#!/usr/bin/python3
"""
Test Amenity
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from os import chdir, getcwd, path
from pep8 import StyleGuide
from shutil import rmtree
from tempfile import mkdtemp


MODEL = path.join(getcwd(), 'models', 'amenity.py')


class TestAmenity(unittest.TestCase):
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
        self.assertEqual(Amenity.name, "")
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_instance(self):
        """
        Test instance
        """
        my_amenity = Amenity()
        self.assertEqual(my_amenity.name, "")
        self.assertTrue(isinstance(my_amenity, BaseModel))

    def test_pep8(self):
        """
        Test PEP8 conformance
        """
        style = StyleGuide(quiet=True)
        check = style.check_files([MODEL])
        self.assertEqual(check.total_errors, 0)
