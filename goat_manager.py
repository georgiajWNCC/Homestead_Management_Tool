"""
    Name: goat_manager.py
    Author: Jonathan Georgiades
    Created: 12 September 2024
    Purpose: Python homesteading goat management program that tracks
    the breed, age, health, weekly milk production, and feed amount consumed
    using assistance from AI (MS Copilot)
"""

# import datetime, to track date/time of health issues, egg production
# and feed consumption. 
import datetime
# pip install rich
import rich 
# Import Console for console printing
from rich.console import Console
# Import Panel for title displays
from rich.panel import Panel
# Initialize rich.console
console = Console()


# ----------------------------------- CHICKEN CLASS --------------------------------------- #
# AI copilot prompt utilized to create chicken class, copied for goat class, with id, breed, age, 
# health issues, egg count, and feed consumption functions template. 
# Create chicken class
class Goat:
    def __init__(self, id_number, breed, age, health_issues, weekly_milk_count, feed_consumed):
        self.id_number = id_number
        self.breed = breed
        self.age = age
        self.health_issues = health_issues
        self.weekly_milk_count = weekly_milk_count
        self.feed_consumed = feed_consumed

    # Create getters and setters for goat class
    # Get id number of goat
    def get_id_number(self):
        return self.id_number

    # Get goat breed
    def get_breed(self):
        return self.breed

    # Get age of goat
    def get_age(self):
        return self.age

    # Get health issues of goat
    def get_health_issues(self):
        return self.health_issues

    # Get weekly milk production
    def get_weekly_milk_count(self):
        return self.weekly_milk_count

    # Get total feed consumption
    def get_feed_consumed(self):
        return self.feed_consumed

    # Set health issues
    def set_health_issues(self, health_issues):
        self.health_issues = health_issues

    # Set weekly milk production
    def set_weekly_milk_count(self, weekly_milk_count):
        self.weekly_milk_count = weekly_milk_count

    # Set total feed consumed
    def set_feed_consumed(self, feed_consumed):
        self.feed_consumed = feed_consumed

# ----------------------------------- HOMESTEAD CLASS --------------------------------------- #
"""AI copilot prompt utilized to create homestead class in order to allow user to add or remove
 goats to management system, create a total for milk collected, create a health report,
 track total feed consumption, update health issues, add feed, and generate a report for 
 review of a specific goat's status."""
class Homestead:
    # Initialize
    def __init__(self):
        self.goats = []

    # Add chicken by new id number
    def add_goat(self, goat):
        self.goats.append(goat)

    # Removes goat via its individual id number
    def remove_goat(self, id_number):
        self.goats = [goat for goat in self.goats if goat.get_id_number() != id_number]

    # Calculate total milk collection for the week
    def total_milk_collection(self):
        return sum(goat.get_weekly_milk_count() for goat in self.goats)

    # Generate a health report that lists any health issues
    def create_health_report(self):
        report = {}
        for goat in self.goats:
            report[goat.get_id_number()] = goat.get_health_issues()
        return report
    
    # Calculate a sum total for feed consumed
    def total_feed_consumed(self):
        return sum(goat.get_feed_consumed() for goat in self.goats)

    # Update health issues of goat
    def update_health_issues(self, id_number, health_issues):
        for goat in self.goats:
            if goat.get_id_number() == id_number:
                goat.set_health_issues(health_issues)

    # Give additional feed to goat
    def add_feed(self, id_number, feed_amount):
        for goat in self.goats:
            if goat.get_id_number() == id_number:
                goat.set_feed_consumed(goat.get_feed_consumed() + feed_amount)

    # Generate a complete report on the goats's id, breed, age, health, milk production, and amount of feed consumed.  
    def generate_report(self, id_number):
        for goat in self.goats:
            if chicken.get_id_number() == id_number:
                return {
                    "ID Number": goat.get_id_number(),
                    "Breed": goat.get_breed(),
                    "Age": goat.get_age(),
                    "Health Issues": goat.get_health_issues(),
                    "Weekly Milk Count (GAL)": goat.get_weekly_milk_count(),
                    "Feed Consumed": goat.get_feed_consumed()
                }
        return None

    
# ----------------------------------- MAIN PROGRAM  --------------------------------------- #
def main():
    homestead = Homestead()
# Create while loop menu to prompt user input.
# While True, continue to run program.  
    while True:

# TODO: Print a nice title for the program using rich.
        console.print(
        Panel.fit(
        "\nGEORGIADES" "\nHOMESTEAD"
        "\nMANAGEMENT" "\nMENU",
        style="bold blue",))
        print()
        print("")
        # Use rich to highlight menu options.
        print("\nMENU OPTIONS ")
        print()
        console.print(Panel.fit("1. Add Goat",
        style="bold green",))
        console.print(Panel.fit("2. Remove Goat",
        style="bold red",))
        print("3. Collect Daily Milk")
        print("4. Update Health Issues")
        print("5. Add To Feed Total")
        console.print(Panel.fit("6. Generate Goat Status Report",
        style="bold cyan"))
        console.print(Panel.fit("7. Exit Program",
        style="bold yellow"))

        # Prompt user to select from menu options
        option = input("\nChoose Menu Option: ")

        if option == '1':
            id_num = int(input("Enter Goat ID number: "))
            breed = input("Enter Breed: ")
            age = int(input("Enter Goat Age (in years ): "))
            health_issues = input("Enter Known Health Issues (e.g. parasites, anemia, flu, none, etc): ")
            weekly_milk_count = int(input("Enter Weekly Milk Count (in gallons): "))
            feed_consumed = float(input("Enter Total Feed Consumed (in pounds): "))
            goat = Goat(id_num, breed, age, health_issues, weekly_milk_count, feed_consumed)
            homestead.add_goat(goat)
            print("Goat Added to Homestead Goat Herd :) .")

        elif option == '2':
            id_num = int(input("Enter Goat ID number to remove: "))
            homestead.remove_goat(id_num)
            print("Goat Removed from Homestead Goat Herd :/ !")
            print("Time to Breed/Buy more Goats!!!")

        elif option == '3':
            print(f"Total Milk Collected: {homestead.total_milk_collection()} gallons of milk")

        elif option == '4':
            id_num = int(input("Enter goat ID number to update health issues: "))
            health_issues = input("Enter new health issues: ")
            homestead.update_health_issues(id_num, health_issues)
            print("Health issues updated!")

        elif option == '5':
            id_num = int(input("Enter goat ID number to add feed: "))
            feed_amount = float(input("Enter feed amount given (in pounds): "))
            homestead.add_feed(id_num, feed_amount)
            print("Update to feed given complete!")

        elif option == '6':
            id_num = int(input("Enter goat ID number to generate a complete report: "))
            report = homestead.generate_report(id_num)
            if report:
                print("\nGoat Report")
                for key, value in report.items():
                    print(f"{key}: {value}")
            else:
                print("Unfortunatley that Goat cannot be found!")
                print("Please double check your hand written records for verification.")

        elif option == '7':
            print("Thank you for utilizing the Homestead Management Program!")
            print("Keep up the hard work!")
            print("Bye for now!")
            break

        else:
            print("I'm sorry.  That isn't a menu option. Please try again.")
            print("Remember to select from options 1 to 7.")

if __name__ == "__main__":
    main()