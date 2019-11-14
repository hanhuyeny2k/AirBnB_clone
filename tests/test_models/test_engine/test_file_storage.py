#!/usr/bin/python3
"""
Test FileStorage
"""

import unittest
from models.engine.file_storage import FileStorage
from os import getcwd, chdir
from shutil import rmtree
from tempfile import mkdtemp


class test_FileStorage(unittest.TestCase):
    """
    Test FileStorage
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

    def test_init(self):
        """
        Test instance
        """
        my_model = FileStorage()
