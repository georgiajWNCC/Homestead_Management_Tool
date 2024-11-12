"""
    Name: homestead.py
    Author: Jonathan Georgiades
    Created: 12 September 2024
    1st Revision: 24 October 2024
    2nd Revision: 12 November 2024
    Purpose: Python homesteading homestead class module that tracks
    the breed, age, health, weekly milk production, and feed amount consumed.
    Imports Animal class from animal.py module.
"""

# import datetime, to track date/time of health issues, egg production
# and feed consumption. 
import datetime
from animal import Animal
from cow import Cow
from sheep import Sheep
from goat import Goat
from chicken import Chicken
from pig import Pig
from rabbit import Rabbit

class Homestead:
    def __init__(self):
        """Initialize a new Homestead with an empty list of animals."""
        self.animals = []

    def add_animal(self, animal):
        """Adds an animal object to the homestead."""
        self.animals.append(animal)
        print(f"Added {animal.get_id_number()} to the homestead.")

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

    def generate_report(self, id_number=None):
        """Generate a report for a specific animal by ID, or for all animals if no ID is given."""
        if id_number:
            # Generate report for a specific animal
            for animal in self.animals:
                if animal.get_id_number() == id_number:
                    animal_report = {
                        "ID Number": animal.get_id_number(),
                        "Species": animal.get_species(),
                        "Breed": animal.get_breed(),
                        "Age": animal.get_age(),
                        "Health Issues": animal.get_health_issues(),
                        "Weekly Weight (lbs)": animal.get_weekly_weight(),
                        "Feed Consumed": animal.get_feed_consumed(),
                    }
                    # If-elif-else statement for
                    # checking for specific product that is collected based on the animal's species
                    # Example: Sheep, weekly wool collected
                    if isinstance(animal, Cow):
                        animal_report["Weekly Product Collected"] = animal.get_weekly_milk_collected()
                    elif isinstance(animal, Chicken):
                        animal_report["Weekly Product Collected"] = animal.get_weekly_egg_collected()
                    elif isinstance(animal, Sheep):
                        animal_report["Weekly Product Collected"] = animal.get_weekly_wool_collected() 
                    elif isinstance(animal, Goat):
                        animal_report["Weekly Product Collected"] = animal.get_weekly_milk_collected() 
                    elif isinstance(animal, Pig):
                        animal_report["Weekly Product Collected"] = animal.get_weekly_meat_collected() 
                    elif isinstance(animal, Rabbit):
                        animal_report["Weekly Product Collected"] = animal.get_weekly_fur_collected() 
                    else:
                        animal_report["Weekly Product Collected"] = "N/A"  # If no product is collected for other animals

                    return animal_report

            return None  # Animal not found for the provided ID number
        else:
            # Generate report for all animals
            report = []
            for animal in self.animals:
                animal_report = {
                    "ID Number": animal.get_id_number(),
                    "Species": animal.get_species(),
                    "Breed": animal.get_breed(),
                    "Age": animal.get_age(),
                    "Health Issues": animal.get_health_issues(),
                    "Weekly Weight (lbs)": animal.get_weekly_weight(),
                    "Feed Consumed": animal.get_feed_consumed(),
                }

                # Check for product collected based on species
                if isinstance(animal, Cow):
                    animal_report["Weekly Product Collected"] = animal.get_weekly_milk_collected()
                elif isinstance(animal, Chicken):
                    animal_report["Weekly Product Collected"] = animal.get_weekly_egg_collected()
                elif isinstance(animal, Sheep):
                    animal_report["Weekly Product Collected"] = animal.get_weekly_wool_collected()
                elif isinstance(animal, Goat):
                    animal_report["Weekly Product Collected"] = animal.get_weekly_milk_collected()
                elif isinstance(animal, Pig):
                    animal_report["Weekly Product Collected"] = animal.get_weekly_meat_collected()
                elif isinstance(animal, Rabbit):
                    animal_report["Weekly Product Collected"] = animal.get_weekly_fur_collected()
                else:
                    animal_report["Weekly Product Collected"] = "N/A"  # If no product is collected for other animals

                report.append(animal_report)

            return report

    def list_animals(self):
        """Return a list of all animals in the homestead."""
        return [{"ID": animal.get_id_number(), "Species": animal.get_species(), "Breed": animal.get_breed(), "Age": animal.get_age()} for animal in self.animals]
