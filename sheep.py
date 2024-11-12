"""
    Name: sheep.py
    Author: Jonathan Georgiades
    Created: 24 October 2024
    Revised: 12 November 2024
    Purpose: Python homesteading sheep management program that tracks
    the breed, age, health, weekly weight, weekly milk production, and feed amount consumed
"""

import datetime
from animal import Animal
# ------------------------------------------ SHEEP CLASS -------------------------------------------- #

class Sheep(Animal):
    # Initialize goat object with parameters given
    def __init__(self, id_number, breed, age, health_issues, weekly_weight, feed_consumed, weekly_wool_collected=0):
        self.id_number = id_number  # Unique identifier for the sheep
        self.breed = breed          # Breed of the sheep
        self.age = age              # Age of the sheep in years
        self.health_issues = health_issues  # Known health issues (if any)
        self.weekly_weight = weekly_weight  # Weight of the sheep for the week
        self.feed_consumed = feed_consumed  # Total feed consumed by the sheep
        self.weekly_wool_collected = weekly_wool_collected  # Amount of wool collected weekly

    def get_species(self):
        return "Sheep"
    
    # TODO: Create getters
    def get_id_number(self):
        """Return the unique ID number of the sheep."""
        return self.id_number

    def get_breed(self):
        """Return the breed of the sheep."""
        return self.breed

    def get_age(self):
        """Return the age of the sheep."""
        return self.age

    def get_health_issues(self):
        """Return the known health issues of the sheep."""
        return self.health_issues

    def get_weekly_weight(self):
        """Return the weekly weight of the sheep."""
        return self.weekly_weight

    def get_feed_consumed(self):
        """Return the total feed consumed by the sheep."""
        return self.feed_consumed

    def get_weekly_wool_collected(self):
        """Return the weekly wool yield of the sheep."""
        return self.weekly_wool_collected

    # TODO: Create setters
    def set_health_issues(self, health_issues):
        """Update the health issues of the sheep."""
        self.health_issues = health_issues

    def set_weekly_weight(self, weekly_weight):
        """Update the weekly weight of the sheep."""
        self.weekly_weight = weekly_weight

    def set_feed_consumed(self, feed_consumed):
        """Update the total feed consumed by the sheep."""
        self.feed_consumed = feed_consumed

    def set_weekly_wool_collected(self, wool_amount):
        """Update the weekly wool yield of the sheep."""
        self.weekly_wool_collected = wool_amount
