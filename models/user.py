#!/usr/bin/python3
"""
Provides a class 'User' that inherits from 'BaseModel'
"""
import models


class User(models.base_model.BaseModel):
    """
    Defines a user model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
