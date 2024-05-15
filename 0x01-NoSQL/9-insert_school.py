#!/usr/bin/env python3
"""Inserting into a new document in a collection
"""

def insert_school(mongo_collection, **kwargs):
    """A function that inserts into a collection
    """
    new_collection = mongo_collection.insert_one(kwargs)
    return new_collection.inserted_id
