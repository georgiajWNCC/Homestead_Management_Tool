"""
    Name: homestead_main.py
    Author: Jonathan Georgiades
    Created: 26 September 2024
    Edited: 24 October 2024
    Purpose: Python main homestead program that imports
    chicken, cow, goat, pig, and rabbit classes.
"""

# Import rich library
import rich
from rich.console import Console
from rich.panel import Panel
# Import cow, sheep, goat, chicken, pig, and rabbit classes
from cow import Cow
from sheep import Sheep
from goat import Goat
from chicken import Chicken
from pig import Pig
from rabbit import Rabbit

# Initialize Rich Console 
console = Console()

# Create a homestead class for main program
class Homestead:
    def __init__(self):
        # Initialize a dictionary to hold lists of animal types
        self.animals = {
            "cows": [],
            "sheep": [],
            "goats": [],
            "chickens": [],
            "pigs": [],
            "rabbits": []
        }
    # Create add_animal function to add a specific animal type
    def add_animal(self, animal_type, animal):
        # Add animal to animal type list
        if animal_type in self.animals:
            self.animals[animal_type].append(animal)

    # Create remove_animal function to remove a specific animal type
    def remove_animal(self, animal_type, id_number):
        # Remove animal from type list by ID number
        if animal_type in self.animals:
            self.animals[animal_type] = [
                animal for animal in self.animals[animal_type] 
                if animal.get_id_number() != id_number
            ]
    # Create total_feed_consumed function to track total feed consumed
    def total_feed_consumed(self):
        # Calculate the total feed consumed by all animals
        total_feed = 0
        for animal_list in self.animals.values():
            total_feed += sum(animal.get_feed_consumed() for animal in animal_list)
        return total_feed

    # Create generate_report 
    def generate_report(self):
        # Generate report summarizing the number of each animal type
        report = {}
        for animal_type, animal_list in self.animals.items():
            report[animal_type] = len(animal_list)  # Count of each animal type
        return report
# Main program start
def main():
    homestead = Homestead()
    
    # Create menu loop for program
    while True:
        # Display menu title using Rich panel for formatting
        console.print(
            Panel.fit(
                "\nGEORGIADES HOMESTEAD MANAGEMENT MENU",
                style="bold blue"
            )
        )
        
        print("\nMENU OPTIONS")
        console.print(Panel.fit("1. Add Animal", style="bold green"))
        console.print(Panel.fit("2. Remove Animal", style="bold red"))
        console.print(Panel.fit("3. Total Feed Consumed", style="bold cyan"))
        console.print(Panel.fit("4. Generate Report", style="bold yellow"))
        console.print(Panel.fit("5. Exit Program", style="bold magenta"))

        # Prompt user for menu option
        option = input("\nChoose an Option from the Menu: ")

        if option == '1':
            # Add animal
            animal_type = input("Enter animal type (cow, sheep, goat, chicken, pig, rabbit): ").lower()
            id_num = int(input("Enter animal ID number: "))
            breed = input("Enter breed: ")
            age = int(input("Enter age (in years): "))
            health_issues = input("Enter health issues (parasites, flu, annemia, none, etc): ")
            weekly_weight = int(input("Enter weekly weight (in pounds): "))
            feed_consumed = float(input("Enter total feed consumed (in pounds): "))
            
            # Create animal object based on animal type
            # if, elif, else statements
            if animal_type == 'cow':
                weekly_milk_collected = float(input("Enter weekly milk collected (in gallons): "))
                animal = Cow(id_num, breed, age, health_issues, weekly_weight, feed_consumed, weekly_milk_collected)
            elif animal_type == 'sheep':
                animal = Sheep(id_num, breed, age, health_issues, weekly_weight, feed_consumed)
            elif animal_type == 'goat':
                animal = Goat(id_num, breed, age, health_issues, weekly_weight, feed_consumed)
            elif animal_type == 'chicken':
                egg_production = int(input("Enter weekly egg production: "))
                animal = Chicken(id_num, breed, age, health_issues, egg_production, feed_consumed)
            elif animal_type == 'pig':
                animal = Pig(id_num, breed, age, health_issues, weekly_weight, feed_consumed)
            elif animal_type == 'rabbit':
                animal = Rabbit(id_num, breed, age, health_issues, weekly_weight, feed_consumed)
            else:
                print("Invalid animal type. Please choose a valid animal type.")
                continue
            
            # Add the created animal object to the homestead
            homestead.add_animal(animal_type, animal)
            print(f"{animal_type.capitalize()} added to the homestead!")

        elif option == '2':
            # Remove animal
            animal_type = input("Enter animal type to remove (cow, sheep, goat, chicken, pig, rabbit): ").lower()
            id_num = int(input("Enter ID number of the animal to remove: "))
            homestead.remove_animal(animal_type, id_num)
            print(f"{animal_type.capitalize()} removed from the homestead.")

        elif option == '3':
            # Display total feed consumed
            total_feed = homestead.total_feed_consumed()
            print(f"Total Feed Consumed: {total_feed} pounds")

        elif option == '4':
            # Generate and display report
            report = homestead.generate_report()
            print("Homestead Animal Report:")
            for animal_type, count in report.items():
                print(f"{animal_type.capitalize()}: {count}")

        elif option == '5':
            # Exit the program
            print("Thank you for using the Homestead Management Program!")
            break

        else:
            # Invalid option
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
