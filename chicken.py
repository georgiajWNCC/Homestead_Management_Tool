"""
    Name: chicken_manager.py
    Author: Jonathan Georgiades
    Created: 01 September 2024
    Purpose: Create a python homesteading chicken management program that tracks
    the breed, age, health, weekly egg production, and feed amount consumed
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
# AI copilot prompt utilized to create chicken class with id, breed, age, 
# health issues, egg count, and feed consumption functions template. 
# Create chicken class
class Chicken:
    def __init__(self, id_number, breed, age, health_issues, weekly_egg_count, feed_consumed):
        self.id_number = id_number
        self.breed = breed
        self.age = age
        self.health_issues = health_issues
        self.weekly_egg_count = weekly_egg_count
        self.feed_consumed = feed_consumed

    # Create getters and setters for chicken class
    # Get id number of chicken
    def get_id_number(self):
        return self.id_number

    # Get chicken breed
    def get_breed(self):
        return self.breed

    # Get age of chicken
    def get_age(self):
        return self.age

    # Get health issues of chicken
    def get_health_issues(self):
        return self.health_issues

    # Get weekly egg count
    def get_weekly_egg_count(self):
        return self.weekly_egg_count

    # Get total feed consumption
    def get_feed_consumed(self):
        return self.feed_consumed

    # Set health issues
    def set_health_issues(self, health_issues):
        self.health_issues = health_issues

    # Set weekly egg count
    def set_weekly_egg_count(self, weekly_egg_count):
        self.weekly_egg_count = weekly_egg_count

    # Set total feed consumed
    def set_feed_consumed(self, feed_consumed):
        self.feed_consumed = feed_consumed

# ----------------------------------- HOMESTEAD CLASS --------------------------------------- #
"""AI copilot prompt utilized to create homestead class in order to allow user to add or remove
 chickens to management system, create a total for eggs collected, create a health report,
 track total feed consumption, update health issues, add feed, and generate a report for 
 review of a specific chickens status."""
class Homestead:
    # Initialize
    def __init__(self):
        self.chickens = []

    # Add chicken by new id number
    def add_chicken(self, chicken):
        self.chickens.append(chicken)

    # Removes ckicken via its individual id number
    def remove_chicken(self, id_number):
        self.chickens = [chicken for chicken in self.chickens if chicken.get_id_number() != id_number]

    # Calculate total egg collection for the week
    def total_egg_collection(self):
        return sum(chicken.get_weekly_egg_count() for chicken in self.chickens)

    # Generate a health report that lists any health issues
    def create_health_report(self):
        report = {}
        for chicken in self.chickens:
            report[chicken.get_id_number()] = chicken.get_health_issues()
        return report
    
    # Calculate a sum total for feed consumed
    def total_feed_consumed(self):
        return sum(chicken.get_feed_consumed() for chicken in self.chickens)

    # Update health issues of chicken
    def update_health_issues(self, id_number, health_issues):
        for chicken in self.chickens:
            if chicken.get_id_number() == id_number:
                chicken.set_health_issues(health_issues)

    # Give additional feed to chicken
    def add_feed(self, id_number, feed_amount):
        for chicken in self.chickens:
            if chicken.get_id_number() == id_number:
                chicken.set_feed_consumed(chicken.get_feed_consumed() + feed_amount)

    # Generate a complete report on the chicken's id, breed, age, health, egg count, and amount of feed consumed.  
    def generate_report(self, id_number):
        for chicken in self.chickens:
            if chicken.get_id_number() == id_number:
                return {
                    "ID Number": chicken.get_id_number(),
                    "Breed": chicken.get_breed(),
                    "Age": chicken.get_age(),
                    "Health Issues": chicken.get_health_issues(),
                    "Weekly Egg Count": chicken.get_weekly_egg_count(),
                    "Feed Consumed": chicken.get_feed_consumed()
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
        console.print(Panel.fit("1. Add Chicken",
        style="bold green",))
        console.print(Panel.fit("2. Remove Chicken",
        style="bold red",))
        print("3. Gather Weekly Eggs")
        print("4. Update Health Issues")
        print("5. Add To Feed Total")
        console.print(Panel.fit("6. Generate Chicken Status Report",
        style="bold cyan"))
        console.print(Panel.fit("7. Exit Program",
        style="bold yellow"))

        # Prompt user to select from menu options
        option = input("\nChoose Menu Option: ")

        if option == '1':
            id_num = int(input("Enter Chicken ID number: "))
            breed = input("Enter Breed: ")
            age = int(input("Enter Chicken Age (in years ): "))
            health_issues = input("Enter Known Health Issues (e.g. bumblefoot, anemia, flu, none, etc): ")
            weekly_egg_count = int(input("Enter Weekly Egg Count: "))
            feed_consumed = float(input("Enter Total Feed Consumed (in pounds): "))
            chicken = Chicken(id_num, breed, age, health_issues, weekly_egg_count, feed_consumed)
            homestead.add_chicken(chicken)
            print("Chicken Added to Homestead Flock :) .")

        elif option == '2':
            id_num = int(input("Enter chicken ID number to remove: "))
            homestead.remove_chicken(id_num)
            print("Chicken Removed from Homestead Flock :/ !")
            print("Time to Breed/Buy more Chickens!!!")

        elif option == '3':
            print(f"Total Eggs Collected: {homestead.total_egg_collection()} eggs")

        elif option == '4':
            id_num = int(input("Enter chicken ID number to update health issues: "))
            health_issues = input("Enter new health issues: ")
            homestead.update_health_issues(id_num, health_issues)
            print("Health issues updated!")

        elif option == '5':
            id_num = int(input("Enter chicken ID number to add feed: "))
            feed_amount = float(input("Enter feed amount given (in pounds): "))
            homestead.add_feed(id_num, feed_amount)
            print("Update to feed given complete!")

        elif option == '6':
            id_num = int(input("Enter chicken ID number to generate a complete report: "))
            report = homestead.generate_report(id_num)
            if report:
                print("\nChicken Report")
                for key, value in report.items():
                    print(f"{key}: {value}")
            else:
                print("Unfortunatley that Chicken cannot be found!")
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
