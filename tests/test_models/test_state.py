#!/usr/bin/python3
"""
Test State
"""

import unittest
from models.base_model import BaseModel
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

    def test_class(self):
        """
        Test class
        """
        assertEqual(State.name, "")
        assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        """
        Test instance
        """
        my_state = State()
        assertEqual(my_state.name, "")
        assertTrue(isinstance(my_state, BaseModel))
