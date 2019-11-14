#!/usr/bin/python3
"""
Test FileStorage
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import chdir, getcwd, path, remove
from pep8 import StyleGuide
from shutil import rmtree
from tempfile import mkdtemp


MODEL = path.join(getcwd(), 'models', 'engine', 'file_storage.py')


class TestFileStorage(unittest.TestCase):
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
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        my_storage = FileStorage()
        self.assertIs(type(my_storage.all()), dict)

    def test_new(self):
        """
        Test new method
        """
        try:
            remove("file.json")
        except FileNotFoundError:
            pass
        my_storage = FileStorage()
        obj = BaseModel()
        key = '{}.{}'.format('BaseModel', obj.id)
        my_storage.new(obj)
        self.assertIn(key, my_storage.all())
        self.assertRaises(AttributeError, my_storage.new, "")

    def test_save(self):
        """
        Test save method
        """
        try:
            remove('file.json')
        except FileNotFoundError:
            pass
        my_storage = FileStorage()
        self.assertFalse(path.isfile('file.json'))
        my_storage.save()
        self.assertTrue(path.isfile('file.json'))

    def test_reload(self):
        """
        Test reload method
        """
        my_storage = FileStorage()
        my_storage.save()
        objects = my_storage.all()
        my_storage.reload()
        self.assertEqual(my_storage.all(), objects)

    def test_pep8(self):
        """
        Test PEP8 conformance
        """
        style = StyleGuide(quiet=True)
        check = style.check_files([MODEL])
        self.assertEqual(check.total_errors, 0)
