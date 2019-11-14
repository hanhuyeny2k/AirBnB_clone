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
        assertEqual(Place.city_id, "")
        assertEqual(Place.user_id, "")
        assertEqual(Place.name, "")
        assertEqual(Place.description, "")
        assertEqual(Place.number_rooms, 0)
        assertEqual(Place.number_bathrooms, 0)
        assertEqual(Place.max_guest, 0)
        assertEqual(Place.price_by_night, 0)
        assertEqual(Place.latitude, 0.0)
        assertEqual(Place.longitude, 0.0)
        assertEqual(Place.amenity_ids, [])
        assertTrue(issubclass(Place, BaseModel))

    def test_instance(self):
        """
        Test instance
        """
        my_place = Place()
        assertEqual(my_place.city_id, "")
        assertEqual(my_place.user_id, "")
        assertEqual(my_place.name, "")
        assertEqual(my_place.description, "")
        assertEqual(my_place.number_rooms, 0)
        assertEqual(my_place.number_bathrooms, 0)
        assertEqual(my_place.max_guest, 0)
        assertEqual(my_place.price_by_night, 0)
        assertEqual(my_place.latitude, 0.0)
        assertEqual(my_place.longitude, 0.0)
        assertEqual(my_place.amenity_ids, [])
        assertTrue(isinstance(my_place, BaseModel))
