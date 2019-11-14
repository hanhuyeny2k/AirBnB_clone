#!/usr/bin/python3
"""
Test City
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from os import chdir, getcwd, path
from pep8 import StyleGuide
from shutil import rmtree
from tempfile import mkdtemp


MODEL = path.join(getcwd(), 'models', 'city.py')


class TestCity(unittest.TestCase):
    """
    Test City
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
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")
        self.assertTrue(issubclass(City, BaseModel))

    def test_instance(self):
        """
        Test instance
        """
        my_city = City()
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")
        self.assertTrue(isinstance(my_city, BaseModel))

    def test_pep8(self):
        """
        Test PEP8 conformance
        """
        style = StyleGuide(quiet=True)
        check = style.check_files([MODEL])
        self.assertEqual(check.total_errors, 0)
