"""
    Name: cow.py
    Author: Jonathan Georgiades
    Created: 26 September 2024
    1st Revision: 24 October 2024
    2nd Revision: 12 November 2024
    Purpose: Python homesteading cow module that tracks
    the breed, age, health, weekly weight, weekly milk production, and feed amount consumed.
"""

import datetime
from animal import Animal
# ----------------------------------- COW CLASS --------------------------------------- #
# TODO: Create cow class
class Cow(Animal):
    # Initialize Cow object with parameters
    # def __int__(self, etc..)
    def __init__(self, id_number, breed, age, health_issues, weekly_weight, feed_consumed, weekly_milk_collected):
        super().__init__(id_number, breed, age, health_issues, weekly_weight, feed_consumed)
        self.weekly_milk_collected = weekly_milk_collected

    def get_species(self):
        return "Cow"

    # TODO: Create getters
    # TODO: Method get/return cow ID number
    def get_id_number(self):
        return self.id_number

    # TODO: Method get/return breed of the cow
    def get_breed(self):
        return self.breed

    # TODO: Method get/return age of the cow
    def get_age(self):
        return self.age

    # TODO: Method get/return the health status of the cow
    def get_health_issues(self):
        return self.health_issues

    # TODO: Method get/return the weekly weight of the cow
    def get_weekly_weight(self):
        return self.weekly_weight

    # TODO: Method get/return the weekly feed consumed by the cow
    def get_feed_consumed(self):
        return self.feed_consumed

    # TODO: Method get/return the weekly milk collected (gallons)
    def get_weekly_milk_collected(self):
        return self.weekly_milk_collected

    # TODO: Create setters
    # TODO: Method to update the cow's health status
    def set_health_issues(self, health_issues):
        self.health_issues = health_issues

    # TODO: Method to update the cow's weekly weight
    def set_weekly_weight(self, weekly_weight):
        self.weekly_weight = weekly_weight

    # TODO: Method to update the amount of weekly feed consumed
    def set_feed_consumed(self, feed_consumed):
        self.feed_consumed = feed_consumed

    # TODO: Method to update the weekly amount of milk collected
    def set_weekly_milk_collected(self, milk_amount):
        self.weekly_milk_collected = milk_amount

