#!/usr/bin/env python3
"""Inserting into a new document in a collection
"""

def insert_school(mongo_collection, **kwargs):
    """A function that inserts into a collection
    """
    result = {k: v for k, v in kwargs.items()}
    new_collection = mongo_collection.insert_one(result)
    return new_collection
