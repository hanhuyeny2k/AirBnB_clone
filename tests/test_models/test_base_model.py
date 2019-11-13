#!/usr/bin/python3
"""
Test BaseModel
"""

from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import path, remove


class test_BaseModel(Unittest.Unittest):
    """
    test ModelBase
    """
    def setUp(self):
        pass

    def teardown(self):
        if path.exists(file.json):
            remove(file.json)

    def test_init(self):
        """ check for name input """
        my_model = dir(BaseModel)
        self.assertIn('__init__', my_model)
        self.assertIn('__str__', my_model)
        self.assertIn('save', my_model)
        self.assertIn('to_dict', my_model)

    def test_copy(self):
        my_model = dir(BaseModel())
        self.assertIn('__init__', my_model)
        self.assertIn('__str__', my_model)
        self.assertIn('save', my_model)
        self.assertIn('to_dict', my_model)

    def test_correctly_copy(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertIsInstance(my_model.__class__, type)

    def test_for_str(self):
        my_model = BaseModel()
        string = '['+my_model.__class__.__name__+']' +' ('+my_model.id+')
                    '+str(my_model.__dict__)
        self.assertEqual(string, my_model.__str__())

    def test_save(self):
        my_model = BaseModel()
        my_storage = FileStorage()
        update = my_model.__dict__['updated_at']
        self.assertFalse(path.isfile('file.json'))
        my_model.save()
        self.assertTrue(path.isfile('file.json'))
        self.assertNotEqual(my_model.__dict__['update_at'], update)
        update = my_model.__dict__['updated_at']
        my_storage.reload()
        self.assertEqual(my_model.__dict__['update_at'], update)

    def test_to_dict
        my_model = BaseModel
        self.assertEqual(my_model.to_dict()['__class__'],
                         my_model.__class__.__name__)
        self.assertEqual(my_model.to_dict()["updated_at"],
                         my_model.updated_at.isoformat())
        self.assertEqual(my_model.to_dict()["created_at"],
                         my_model.created_at.isoformat())
