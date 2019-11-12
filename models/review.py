#!/usr/bin/python3
"""
Provides a class 'Review' that inherits from 'BaseModel'
"""
import models


class Review(models.base_model.BaseModel):
    """
    Defines a review model
    """
    place_id = ""
    user_id = ""
    text = ""
