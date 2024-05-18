#!/usr/bin/env python3
"""A module for finding a list of schools with a topic
"""


def schools_by_topic(mongo_collection, topic):
    """A function that finds all schools with a specific topic
    """
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
