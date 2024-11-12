"""
    Name: pig.py
    Author: Jonathan Georgiades
    Created: 26 September 2024
    Purpose: Python homesteading pig management program that tracks
    the breed, age, health, monthly weight, and feed amount consumed
"""

import datetime
from animal import Animal
# ------------------------------------- PIG CLASS ------------------------------------ #

class Pig(Animal):
    # Initialize pig object with parameters given
    def __init__(self, id_number, breed, age, health_issues, weekly_weight, feed_consumed, weekly_meat_collected=0):
        self.id_number = id_number
        self.breed = breed
        self.age = age
        self.health_issues = health_issues
        self.weekly_weight = weekly_weight
        self.feed_consumed = feed_consumed
        self.weekly_meat_collected = weekly_meat_collected
    
    def get_species(self):
        return "Pig"

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

    def get_weekly_meat_collected(self):
        return self.weekly_meat_collected

    # TODO: Create setters
    def set_health_issues(self, health_issues):
        self.health_issues = health_issues

    def set_weekly_weight(self, weekly_weight):
        self.weekly_weight = weekly_weight

    def set_feed_consumed(self, feed_consumed):
        self.feed_consumed = feed_consumed

    def set_weekly_meat_collected(self, meat_amount):
        self.weekly_meat_collected = meat_amount
