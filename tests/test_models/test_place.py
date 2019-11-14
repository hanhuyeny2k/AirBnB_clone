#!/usr/bin/python3
"""
Test Place
"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from os import getcwd, chdir
from shutil import rmtree
from tempfile import mkdtemp


class test_Place(unittest.TestCase):
    """
    Test Place
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
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
        self.assertTrue(issubclass(Place, BaseModel))

    def test_instance(self):
        """
        Test instance
        """
        my_place = Place()
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.name, "")
        self.assertEqual(my_place.description, "")
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guest, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertEqual(my_place.amenity_ids, [])
        self.assertTrue(isinstance(my_place, BaseModel))
