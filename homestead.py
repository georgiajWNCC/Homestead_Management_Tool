"""
    Name: homestead.py
    Author: Jonathan Georgiades
    Created: 12 September 2024
    Edited: 24 October 2024
    Purpose: Python homesteading homestead class module that tracks
    the breed, age, health, weekly milk production, and feed amount consumed.
    Imports Animal class from animal.py module.
"""

# import datetime, to track date/time of health issues, egg production
# and feed consumption. 
import datetime

from animal import Animal

class Homestead:
    def __init__(self):
        """Initialize a new Homestead with an empty list of animals."""
        self.animals = []

    def add_animal(self, id_number, species, breed, age, health_issues, weekly_weight, feed_consumed, weekly_product_collected=0):
        """Add a new animal to the homestead's herd."""
        animal = Animal(id_number, species, breed, age, health_issues, weekly_weight, feed_consumed, weekly_product_collected)
        self.animals.append(animal)

    def remove_animal(self, id_number):
        """Remove an animal from the homestead by its ID number."""
        self.animals = [animal for animal in self.animals if animal.get_id_number() != id_number]

    def total_weekly_weight(self):
        """Calculate and return the total weekly weight of all animals."""
        return sum(animal.get_weekly_weight() for animal in self.animals)

    def total_weekly_product(self):
        """Calculate and return the total weekly product collected from all animals."""
        return sum(animal.get_weekly_product_collected() for animal in self.animals)

    def create_health_report(self):
        """Generate a health report of all animals, returning a dictionary of ID numbers and health issues."""
        report = {}
        for animal in self.animals:
            report[animal.get_id_number()] = animal.get_health_issues()
        return report
    
    def total_feed_consumed(self):
        """Calculate and return the total feed consumed by all animals."""
        return sum(animal.get_feed_consumed() for animal in self.animals)

    def update_health_issues(self, id_number, health_issues):
        """Update the health issues of a specific animal by its ID number."""
        for animal in self.animals:
            if animal.get_id_number() == id_number:
                animal.set_health_issues(health_issues)

    def add_feed(self, id_number, feed_amount):
        """Add feed amount to a specific animal's total feed consumed by its ID number."""
        for animal in self.animals:
            if animal.get_id_number() == id_number:
                animal.set_feed_consumed(animal.get_feed_consumed() + feed_amount)

    def generate_report(self, id_number):
        """Generate a detailed report for a specific animal by its ID number."""
        for animal in self.animals:
            if animal.get_id_number() == id_number:
                return {
                    "ID Number": animal.get_id_number(),
                    "Species": animal.get_species(),
                    "Breed": animal.get_breed(),
                    "Age": animal.get_age(),
                    "Health Issues": animal.get_health_issues(),
                    "Weekly Weight (lbs)": animal.get_weekly_weight(),
                    "Feed Consumed": animal.get_feed_consumed(),
                    "Weekly Product Collected": animal.get_weekly_product_collected()
                }
        return None  # Return None if the animal with the specified ID is not found

    def list_animals(self):
        """Return a list of all animals in the homestead."""
        return [{"ID": animal.get_id_number(), "Species": animal.get_species(), "Breed": animal.get_breed(), "Age": animal.get_age()} for animal in self.animals]
