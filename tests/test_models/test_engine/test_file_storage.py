#!/usr/bin/python3
"""
Test FileStorage
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import getcwd, chdir
from shutil import rmtree
from tempfile import mkdtemp


class test_FileStorage(unittest.TestCase, FileStorage):
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

    def test_all(self):
        """
        Test all method
        """
        my_storage = FileStorage()
        self.assertEqual(my_storage.all(), {})

    def test_new(self):
        """
        Test new method
        """
        my_storage = FileStorage()

        def obj():
            """
            Do nothing
            """
            pass
        obj.id = 10
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        my_storage.new(obj)
        self.assertEqual(my_storage.all(), {key: obj})
        self.assertRaises(AttributeError, new, "")

    def test_save(self):
        """
        Test save method
        """
        try:
            remove(self.__file_path)
        except FileNotFoundError:
            pass
        my_storage = FileStorage()
        self.assertFalse(path.isfile(self.__file_path))
        my_storage.save()
        self.assertTrue(path.isfile(self.__file_path))

    def test_reload(self):
        """
        Test reload method
        """
        my_storage = FileStorage()
        my_storage.save()
        obj = my_storage.__objects
        my_storage.reload()
        self.assertEqual(my_storage.__objects, obj)
