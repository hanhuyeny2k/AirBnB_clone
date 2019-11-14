#!/usr/bin/python3
"""
Test Review
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from os import getcwd, chdir
from shutil import rmtree
from tempfile import mkdtemp


class test_Review(unittest.TestCase):
    """
    test review
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
        assertEqual(Review.place_id, "")
        assertEqual(Review.user_id, "")
        assertEqual(Review.text, "")
        assertTrue(issubclass(Review, BaseModel))

    def test_instance(self):
        """
        Test instance
        """
        my_review = Review()
        assertEqual(my_review.place_id, "")
        assertEqual(my_review.user_id, "")
        assertEqual(my_review.text, "")
        assertTrue(isinstance(my_review, BaseModel))
