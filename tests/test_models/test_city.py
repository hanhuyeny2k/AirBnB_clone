#!/usr/bin/python3
"""
Test City
"""

import unittest
from models.city import City
from os import getcwd, chdir
from shutil import rmtree
from tempfile import mkdtemp


class test_City(unittest.TestCase):
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

    def test_instance(self):
        """
        Test instance
        """
        my_model = City()
        my_model.name = "Holberton"
