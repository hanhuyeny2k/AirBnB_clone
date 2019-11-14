#!/usr/bin/python3
"""
Test Review
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from os import chdir, getcwd, path
from pep8 import StyleGuide
from shutil import rmtree
from tempfile import mkdtemp


MODEL = path.join(getcwd(), 'models', 'review.py')


class TestReview(unittest.TestCase):
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
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertTrue(issubclass(Review, BaseModel))

    def test_instance(self):
        """
        Test instance
        """
        my_review = Review()
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")
        self.assertTrue(isinstance(my_review, BaseModel))

    def test_pep8(self):
        """
        Test PEP8 conformance
        """
        style = StyleGuide(quiet=True)
        check = style.check_files([MODEL])
        self.assertEqual(check.total_errors, 0)
