#!/usr/bin/python3
"""
Test User
"""

import unittest
from models.user import User
from os import getcwd, chdir
from shutil import rmtree
from tempfile import mkdtemp


class test_User(unittest.TestCase):
    """
    Test User
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

    def check_instance(self):
        """
        Test instance
        """
        my_user = User()
        my_model.last_name = "Holberton"
