#!/usr/bin/python3
"""
Provides a class 'Place' that inherits from 'BaseModel'
"""
import models


class Place(models.base_model.BaseModel):
    """
    Defines a place model
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
