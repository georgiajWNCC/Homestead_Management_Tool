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

# Import animal classes for management program
from cow import Cow
from sheep import Sheep
from goat import Goat
from chicken import Chicken
from pig import Pig
from rabbit import Rabbit

# Initialize Rich Console for formatting
console = Console()

#TODO: Create Homestead class to manage animals
class Homestead:
    def __init__(self):
        # Initialize a dictionary to hold lists of the different animal types
        self.animals = {
            "cows": [],
            "sheep": [],
            "goats": [],
            "chickens": [],
            "pigs": [],
            "rabbits": []
        }

    # TODO: Create method to add animal to corresponding type list
    def add_animal(self, animal_type, animal):
        if animal_type in self.animals:
            self.animals[animal_type].append(animal)

    # TODO: Create method to remove animal from a specific type list by the animal's ID number
    def remove_animal(self, animal_type, id_number):
        if animal_type in self.animals:
            self.animals[animal_type] = [
                animal for animal in self.animals[animal_type] 
                if animal.get_id_number() != id_number  # Keep animals that don't match the ID
            ]

    # TODO: Create method to calculate the total feed consumed 
    def total_feed_consumed(self):
        total_feed = 0
        for animal_list in self.animals.values():
            # Sum feed consumed by each animal for each list
            total_feed += sum(animal.get_feed_consumed() for animal in animal_list)
        return total_feed

    # TODO: Create method to generate a report to summarize the count of each animal type
    def generate_report(self):
        report = {}
        for animal_type, animal_list in self.animals.items():
            report[animal_type] = len(animal_list)  # Count number of animals of each type
        return report

# TODO: Create homestead GUI class to handle user interactions
class HomesteadGUI:
    def __init__(self, homestead):
        # Initialize the console and link to the homestead instance
        self.console = Console()
        self.homestead = homestead

    # TODO: Create method to run menu loop 
    def run(self):
        while True:
            # Display the menu title with rich formatting
            self.console.print(
                Panel.fit(
                    "\nGEORGIADES HOMESTEAD MANAGEMENT MENU",
                    style="bold blue"  # Set the title style
                )
            )

            # Display menu options
            self.console.print(Panel.fit("1. Add Animal", style="bold green"))
            self.console.print(Panel.fit("2. Remove Animal", style="bold red"))
            self.console.print(Panel.fit("3. Total Feed Consumed", style="bold cyan"))
            self.console.print(Panel.fit("4. Generate Report", style="bold yellow"))
            self.console.print(Panel.fit("5. Exit Program", style="bold magenta"))

            # Prompt user to select a menu option
            option = input("\nPlease choose an Option from the Menu: ")

            # Option '1', adding a new animal
            if option == '1':
                # Get animal details from the user
                animal_type = input("Enter animal type (cow, sheep, goat, chicken, pig, rabbit): ").lower()
                id_num = int(input("Enter animal ID number: "))
                breed = input("Enter breed: ")
                age = int(input("Enter age (in years): "))
                health_issues = input("Enter health issues (parasites, flu, anemia, none, etc): ")
                weekly_weight = int(input("Enter weekly weight (in pounds): "))
                feed_consumed = float(input("Enter total feed consumed (in pounds): "))
                
                # Create animal object based on type
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
                    continue  # continue the loop if the type is invalid
                
                # Add animal object to the homestead
                self.homestead.add_animal(animal_type, animal)
                print(f"{animal_type.capitalize()} added to the homestead!")  # Confirmation message

            # Option '2', removing an animal
            elif option == '2':
                animal_type = input("Enter animal type to remove (cow, sheep, goat, chicken, pig, rabbit): ").lower()
                id_num = int(input("Enter ID number of the animal to remove: "))
                self.homestead.remove_animal(animal_type, id_num)
                print(f"{animal_type.capitalize()} removed from the homestead.")

            # Option '3', display total feed amount consumed by animal
            elif option == '3':
                total_feed = self.homestead.total_feed_consumed()
                print(f"Total Feed Consumed: {total_feed} pounds")  # Display total feed

            # Option '4', generate and display a report for animals
            elif option == '4':
                report = self.homestead.generate_report()
                print("Homestead Animal Report:")
                for animal_type, count in report.items():
                    print(f"{animal_type.capitalize()}: {count}")  # Show count for each animal type

            # Option '5', exit program
            elif option == '5':
                print("Thank you for using the Homestead Management Program!")
                break  

            # Handle any invalid inputs by th user
            else:
                print("Sorry, that input is invalid. Please try again.")  

# TODO: Create main program entry point
def main():
    homestead = Homestead()  # Create an instance of the Homestead class
    gui = HomesteadGUI(homestead)  # Create an instance of the GUI, passing the homestead instance
    gui.run()  # Run the GUI menu

# Call the main function
if __name__ == "__main__":
    main() 
