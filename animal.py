"""
    Name: animal.py
    Author: Jonathan Georgiades
    Created: 24 October 2024
    Purpose: Create a python animal class module that tracks
    the breed, age, health, weekly egg production, and feed amount consumed.
"""
# ------------------------------ ANIMAL CLASS -------------------------------------- #
class Animal:
    # Initialize animal object with parameters given
    def __init__(self, id_number, breed, age, health_issues, weekly_weight, feed_consumed):
        self.id_number = id_number  # ID number for the animal
        self.breed = breed          # Breed of animal
        self.age = age              # Age of the animal (years)
        self.health_issues = health_issues  # Any health issues 
        self.weekly_weight = weekly_weight  # Weekly animal weight
        self.feed_consumed = feed_consumed  # Weekly total feed consumed 

    # TODO: Create getters
    # TODO: Method to get/return ID number
    def get_id_number(self):
        # Return animal ID number
        return self.id_number

    # TODO: Method to get/return animal breed
    def get_breed(self):
        # Return animal breed
        return self.breed

    # TODO: Method to get/return the age of the animal
    def get_age(self):
        # Return age of the animal
        return self.age

    # TODO: Method to get/return any animal health issues
    def get_health_issues(self):
        # Return any health issues
        return self.health_issues

    # TODO: Method to get/return weekly animal weight
    def get_weekly_weight(self):
        # Return weekly animal weight
        return self.weekly_weight

    # TODO: Method to get/return weekly feed amount consumed
    def get_feed_consumed(self):
        # Return weekly feed amount consumed
        return self.feed_consumed

    # TODO: Create setters
    # TODO: Method to update health issues
    def set_health_issues(self, health_issues):
        self.health_issues = health_issues

    # TODO: Method to update weekly animal weight
    def set_weekly_weight(self, weekly_weight):
        self.weekly_weight = weekly_weight

    # TODO: Method to update weekly feed amount consumed
    def set_feed_consumed(self, feed_consumed):
        self.feed_consumed = feed_consumed
