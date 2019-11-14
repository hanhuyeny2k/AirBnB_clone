#!/usr/bin/python3
"""
Test Place
"""

import unittest
from models.place import Place
from os import getcwd, chdir
from shutil import rmtree
from tempfile import mkdtemp


class test_Place(unittest.TestCase):
    """
    Test Place
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
        my_model = Place()
        my_model.name = "Holberton"
