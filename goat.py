"""
    Name: goat.py
    Author: Jonathan Georgiades
    Created: 12 September 2024
    Edited: 24 October 2024
    Purpose: Python homesteading goat class module that tracks
    the breed, age, health, weekly milk production, and feed amount consumed.
"""

# import datetime, to track date/time of health issues, egg production
# and feed consumption. 
import datetime


# --------------------------------- GOAT CLASS ----------------------------------- #
class Goat:
    # Initialize goat object with parameters given
    def __init__(self, id_number, breed, age, health_issues, weekly_weight, feed_consumed, weekly_milk_collected=0):
        self.id_number = id_number
        self.breed = breed
        self.age = age
        self.health_issues = health_issues
        self.weekly_weight = weekly_weight
        self.feed_consumed = feed_consumed
        self.weekly_milk_collected = weekly_milk_collected

    # TODO: Create getters
    def get_id_number(self):
        return self.id_number

    def get_breed(self):
        return self.breed

    def get_age(self):
        return self.age

    def get_health_issues(self):
        return self.health_issues

    def get_weekly_weight(self):
        return self.weekly_weight

    def get_feed_consumed(self):
        return self.feed_consumed

    def get_weekly_milk_collected(self):
        return self.weekly_milk_collected

    # TODO: Create setters
    def set_health_issues(self, health_issues):
        self.health_issues = health_issues

    def set_weekly_weight(self, weekly_weight):
        self.weekly_weight = weekly_weight

    def set_feed_consumed(self, feed_consumed):
        self.feed_consumed = feed_consumed

    def set_weekly_milk_collected(self, milk_amount):
        self.weekly_milk_collected = milk_amount
