#!/usr/bin/python3
"""
Provides a class 'State' that inherits from 'BaseModel'
"""
import models


class State(models.base_model.BaseModel):
    """
    Defines a state model
    """
    name = ""
