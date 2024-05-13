#!/usr/bin/env python3
"""A file that allows the listing of all collections
"""


def list_all(mongo_collection):
    """A function that lists all documents in a collection
    """
    if not mongo_collection:
        return []
    return [doc for doc in mongo_collection.find()]
