#!/usr/bin/python3
"""
Test State
"""

import unittest
from models.state import State
from os import getcwd, chdir
from shutil import rmtree
from tempfile import mkdtemp


class test_State(unittest.TestCase):
    """
    test state
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
        my_model = State()
        my_model.name = "Holberton"
