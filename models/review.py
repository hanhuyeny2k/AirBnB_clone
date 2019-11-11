#!/usr/bin/python3
"""Provides a 'Review' class that inherits from 'BaseModel'
"""

import models

class Place(models.base_model.BaseModel):
    place_id = ""
    user_id = ""
    text = ""
