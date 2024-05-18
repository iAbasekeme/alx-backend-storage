#!/usr/bin/env python3
"""A module for finding a list of schools with a topic
"""


def schools_by_topic(mongo_collection, topic):
    """A function that finds all schools with a specific topic
    """
    schools = []
    all_schools = mongo_collection.find({topic})
    for i in all_schools:
        schools.append(i)
    return schools
