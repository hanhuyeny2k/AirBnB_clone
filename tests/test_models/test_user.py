#!/usr/bin/python3
"""
Test User
"""

import unittest
from models.base_model import BaseModel
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

    def test_class(self):
        """
        Test class
        """
        assertEqual(User.email, "")
        assertEqual(User.password, "")
        assertEqual(User.first_name, "")
        assertEqual(User.last_name, "")
        assertTrue(issubclass(User, BaseModel))

    def test_instance(self):
        """
        Test instance
        """
        my_user = User()
        assertEqual(my_user.email, "")
        assertEqual(my_user.password, "")
        assertEqual(my_user.first_name, "")
        assertEqual(my_user.last_name, "")
        assertTrue(isinstance(my_user, BaseModel))
