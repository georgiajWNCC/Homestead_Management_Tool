"""
    Name: chicken.py
    Author: Jonathan Georgiades
    Created: 01 September 2024
    Edited: 24 October 2024
    Purpose: Create a python chicken module program that tracks
    the breed, age, health, weekly egg production, and feed amount consumed.
"""

import datetime

# ----------------------------- CHICKEN CLASS ----------------------------------- #
class Chicken:
    # Initialize chicken object with parameters given
    def __init__(self, id_number, breed, age, health_issues, weekly_weight, feed_consumed, weekly_egg_collected=0):
        self.id_number = id_number
        self.breed = breed
        self.age = age
        self.health_issues = health_issues
        self.weekly_weight = weekly_weight
        self.feed_consumed = feed_consumed
        self.weekly_egg_collected = weekly_egg_collected

    # TODO: Create getters
    # TODO: Method to get/return id number
    def get_id_number(self):
        return self.id_number

    # TODO: Method to get/return breed
    def get_breed(self):
        return self.breed

    # TODO: Method to get/return age
    def get_age(self):
        return self.age

    # TODO: Method to get/return health issues
    def get_health_issues(self):
        return self.health_issues

    # TODO: Method to get/return weekly weight
    def get_weekly_weight(self):
        return self.weekly_weight

    # TODO: Method to get/return weekly feed consumed
    def get_feed_consumed(self):
        return self.feed_consumed

    # TODO: Method to get/return weekly eggs collected
    def get_weekly_egg_collected(self):
        return self.weekly_egg_collected

    # TODO: Create setters
    # TODO: Method to set health issues
    def set_health_issues(self, health_issues):
        self.health_issues = health_issues

    # TODO: Method to set weekly weight
    def set_weekly_weight(self, weekly_weight):
        self.weekly_weight = weekly_weight

    # TODO: Method to set weely feed amount consumed
    def set_feed_consumed(self, feed_consumed):
        self.feed_consumed = feed_consumed

    # TODO: Method to set weekly egg amount collected
    def set_weekly_egg_collected(self, egg_amount):
        self.weekly_egg_collected = egg_amount
