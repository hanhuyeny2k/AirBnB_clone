#!/usr/bin/python3
"""
Test BaseModel
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import chdir, getcwd, path
from pep8 import StyleGuide
from shutil import rmtree
from tempfile import mkdtemp


MODEL = path.join(getcwd(), 'models', 'base_model.py')


class TestBaseModel(unittest.TestCase):
    """
    Test BaseModel
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

    def test_type(self):
        """
        Test type
        """
        my_model = dir(BaseModel)
        self.assertIn('__init__', my_model)
        self.assertIn('__str__', my_model)
        self.assertIn('save', my_model)
        self.assertIn('to_dict', my_model)

    def test_instance(self):
        """
        Test instance
        """
        my_model = dir(BaseModel())
        self.assertIn('__init__', my_model)
        self.assertIn('__str__', my_model)
        self.assertIn('save', my_model)
        self.assertIn('to_dict', my_model)

    def test_attributes(self):
        """
        Test attributes
        """
        my_model = BaseModel()
        self.assertIs(type(my_model.id), str)
        self.assertIs(type(my_model.created_at), datetime)
        self.assertIs(type(my_model.updated_at), datetime)
        self.assertIs(type(my_model.__class__), type)

    def test_str(self):
        """
        Test __str__ method
        """
        my_model = BaseModel()
        string = '[{}] ({}) {}'.format(
            my_model.__class__.__name__,
            my_model.id,
            my_model.__dict__,
        )
        self.assertEqual(string, str(my_model))

    def test_save(self):
        """
        Test save method
        """
        my_model = BaseModel()
        my_storage = FileStorage()
        update = my_model.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        my_model.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(my_model.__dict__['updated_at'], update)
        update = my_model.__dict__['updated_at']
        my_storage.reload()
        self.assertEqual(my_model.__dict__['updated_at'], update)

    def test_to_dict(self):
        """
        Test to_dict method
        """
        my_model = BaseModel()
        self.assertEqual(my_model.to_dict()['__class__'],
                         my_model.__class__.__name__)
        self.assertEqual(my_model.to_dict()["updated_at"],
                         my_model.updated_at.isoformat())
        self.assertEqual(my_model.to_dict()["created_at"],
                         my_model.created_at.isoformat())

    def test_pep8(self):
        """
        Test PEP8 conformance
        """
        style = StyleGuide(quiet=True)
        check = style.check_files([MODEL])
        self.assertEqual(check.total_errors, 0)
