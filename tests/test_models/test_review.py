#!/usr/bin/python3
"""
Test Review
"""

import unittest
from models.review import Review
from os import getcwd, chdir
from shutil import rmtree
from tempfile import mkdtemp


class test_Review(unittest.TestCase):
    """
    test review
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
        my_model = Review()
        my_model.name = "Holberton"
