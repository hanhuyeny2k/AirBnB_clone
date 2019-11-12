#!/usr/bin/python3
"""
Provides the 'models' package
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
