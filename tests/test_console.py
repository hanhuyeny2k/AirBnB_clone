#!/usr/bin/python3
"""
Test console
"""

import unittest
from console import HBNBCommand
from os import chdir, getcwd, path
from pep8 import StyleGuide
from shutil import rmtree
from tempfile import mkdtemp


class TestConsole(unittest.TestCase):
    """
    Tests for console
    """
    def setUp(self):
        """
        Create a temporary directory and enter it
        """
        chdir(mkdtemp())

    def tearDown(self):
        """
        Remove temporary files and directories
        """
        rmtree(getcwd(), ignore_errors=True)

    def test_emptyline(self):
        pass

    def test_help(self):
        pass

    def test_quit(self):
        pass

    def test_EOF(self):
        pass

    def test_all(self):
        pass

    def test_count(self):
        pass

    def test_create(self):
        pass

    def test_destroy(self):
        pass

    def test_show(self):
        pass

    def test_update(self):
        pass

    def test_precmd(self):
        pass
