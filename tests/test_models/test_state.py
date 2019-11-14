#!/usr/bin/python3
"""
Test State
"""

import unittest
from models.base_model import BaseModel
from models.state import State
from os import chdir, getcwd, path
from pep8 import StyleGuide
from shutil import rmtree
from tempfile import mkdtemp


MODEL = path.join(getcwd(), 'models', 'state.py')


class TestState(unittest.TestCase):
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
        self.assertEqual(State.name, "")
        self.assertTrue(issubclass(State, BaseModel))

    def test_instance(self):
        """
        Test instance
        """
        my_state = State()
        self.assertEqual(my_state.name, "")
        self.assertTrue(isinstance(my_state, BaseModel))

    def test_pep8(self):
        """
        Test PEP8 conformance
        """
        style = StyleGuide(quiet=True)
        check = style.check_files([MODEL])
        self.assertEqual(check.total_errors, 0)
