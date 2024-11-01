"""
    Name: rabbit.py
    Author: Jonathan Georgiades
    Created: 26 September 2024
    Purpose: Python homesteading rabbit management program that tracks
    the breed, age, health, monthly weight, and feed amount consumed
"""

import datetime

# ------------------------------------------ RABBIT CLASS ------------------------------------------- #

class Rabbit:
    # Initialize goat object with parameters given
    def __init__(self, id_number, breed, age, health_issues, weekly_weight, feed_consumed, weekly_fur_yield=0):
        self.id_number = id_number  # Unique identifier for the rabbit
        self.breed = breed          # Breed of the rabbit
        self.age = age              # Age of the rabbit in years
        self.health_issues = health_issues  # Known health issues (if any)
        self.weekly_weight = weekly_weight  # Weight of the rabbit for the week
        self.feed_consumed = feed_consumed  # Total feed consumed by the rabbit
        self.weekly_fur_yield = weekly_fur_yield  # Amount of fur collected weekly

    # TODO: Create getters
    def get_id_number(self):
        """Return the unique ID number of the rabbit."""
        return self.id_number

    def get_breed(self):
        """Return the breed of the rabbit."""
        return self.breed

    def get_age(self):
        """Return the age of the rabbit."""
        return self.age

    def get_health_issues(self):
        """Return the known health issues of the rabbit."""
        return self.health_issues

    def get_weekly_weight(self):
        """Return the weekly weight of the rabbit."""
        return self.weekly_weight

    def get_feed_consumed(self):
        """Return the total feed consumed by the rabbit."""
        return self.feed_consumed

    def get_weekly_fur_yield(self):
        """Return the weekly fur yield of the rabbit."""
        return self.weekly_fur_yield

    # TODO: Create setters
    def set_health_issues(self, health_issues):
        """Update the health issues of the rabbit."""
        self.health_issues = health_issues

    def set_weekly_weight(self, weekly_weight):
        """Update the weekly weight of the rabbit."""
        self.weekly_weight = weekly_weight

    def set_feed_consumed(self, feed_consumed):
        """Update the total feed consumed by the rabbit."""
        self.feed_consumed = feed_consumed

    def set_weekly_fur_yield(self, fur_amount):
        """Update the weekly fur yield of the rabbit."""
        self.weekly_fur_yield = fur_amount
