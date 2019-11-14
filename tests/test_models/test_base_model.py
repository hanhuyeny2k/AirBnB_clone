#!/usr/bin/python3
"""
Test BaseModel
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import getcwd, chdir, path
from shutil import rmtree
from tempfile import mkdtemp


class test_BaseModel(unittest.TestCase):
    """
    Test BaseModel
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
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertIsInstance(my_model.__class__, type)

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
        self.assertEqual(string, my_model.__str__())

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
