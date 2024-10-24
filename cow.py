"""
    Name: cow_manager.py
    Author: Jonathan Georgiades
    Created: 26 September 2024
    Purpose: Python homesteading cow management program that tracks
    the breed, age, health, weekly weight, weekly milk production, and feed amount consumed
"""

import datetime
import rich
from rich.console import Console
from rich.panel import Panel

console = Console()

# ----------------------------------- COW CLASS --------------------------------------- #
class Cow:
    def __init__(self, id_number, breed, age, health_issues, weekly_weight, feed_consumed, weekly_milk_collected=0):
        self.id_number = id_number
        self.breed = breed
        self.age = age
        self.health_issues = health_issues
        self.weekly_weight = weekly_weight
        self.feed_consumed = feed_consumed
        self.weekly_milk_collected = weekly_milk_collected

    # Getters
    def get_id_number(self):
        return self.id_number

    def get_breed(self):
        return self.breed

    def get_age(self):
        return self.age

    def get_health_issues(self):
        return self.health_issues

    def get_weekly_weight(self):
        return self.weekly_weight

    def get_feed_consumed(self):
        return self.feed_consumed

    def get_weekly_milk_collected(self):
        return self.weekly_milk_collected

    # Setters
    def set_health_issues(self, health_issues):
        self.health_issues = health_issues

    def set_weekly_weight(self, weekly_weight):
        self.weekly_weight = weekly_weight

    def set_feed_consumed(self, feed_consumed):
        self.feed_consumed = feed_consumed

    def set_weekly_milk_collected(self, milk_amount):
        self.weekly_milk_collected = milk_amount

# ----------------------------------- HOMESTEAD CLASS --------------------------------------- #
class Homestead:
    def __init__(self):
        self.cows = []

    def add_cow(self, cow):
        self.cows.append(cow)

    def remove_cow(self, id_number):
        self.cows = [cow for cow in self.cows if cow.get_id_number() != id_number]

    def total_weekly_weight(self):
        return sum(cow.get_weekly_weight() for cow in self.cows)

    def total_weekly_milk(self):
        return sum(cow.get_weekly_milk_collected() for cow in self.cows)

    def create_health_report(self):
        report = {}
        for cow in self.cows:
            report[cow.get_id_number()] = cow.get_health_issues()
        return report
    
    def total_feed_consumed(self):
        return sum(cow.get_feed_consumed() for cow in self.cows)

    def update_health_issues(self, id_number, health_issues):
        for cow in self.cows:
            if cow.get_id_number() == id_number:
                cow.set_health_issues(health_issues)

    def add_feed(self, id_number, feed_amount):
        for cow in self.cows:
            if cow.get_id_number() == id_number:
                cow.set_feed_consumed(cow.get_feed_consumed() + feed_amount)

    def generate_report(self, id_number):
        for cow in self.cows:
            if cow.get_id_number() == id_number:
                return {
                    "ID Number": cow.get_id_number(),
                    "Breed": cow.get_breed(),
                    "Age": cow.get_age(),
                    "Health Issues": cow.get_health_issues(),
                    "Weekly Weight (lbs)": cow.get_weekly_weight(),
                    "Feed Consumed": cow.get_feed_consumed(),
                    "Weekly Milk Collected (gallons)": cow.get_weekly_milk_collected()
                }
        return None

# ----------------------------------- MAIN PROGRAM --------------------------------------- #
def main():
    homestead = Homestead()
    
    while True:
        console.print(
            Panel.fit(
                "\nGEORGIADES" "\nHOMESTEAD"
                "\nMANAGEMENT" "\nMENU",
                style="bold blue",))
        
        print("\nMENU OPTIONS ")
        console.print(Panel.fit("1. Add Cow", style="bold green"))
        console.print(Panel.fit("2. Remove Cow", style="bold red"))
        print("3. Weekly Weight")
        print("4. Weekly Milk Collected")
        print("5. Update Health Issues")
        print("6. Add To Feed Total")
        console.print(Panel.fit("7. Generate Cow Status Report", style="bold cyan"))
        console.print(Panel.fit("8. Exit Program", style="bold yellow"))

        option = input("\nChoose Menu Option: ")

        if option == '1':
            id_num = int(input("Enter Cow ID number: "))
            breed = input("Enter Breed: ")
            age = int(input("Enter Cow Age (in years): "))
            health_issues = input("Enter Known Health Issues (e.g., parasites, anemia, flu, none, etc): ")
            weekly_weight = int(input("Enter Weekly Weight (in pounds): "))
            feed_consumed = float(input("Enter Total Feed Consumed (in pounds): "))
            weekly_milk_collected = float(input("Enter Weekly Milk Collected (in gallons): "))
            cow = Cow(id_num, breed, age, health_issues, weekly_weight, feed_consumed, weekly_milk_collected)
            homestead.add_cow(cow)
            print("Cow Added to Homestead Cow Herd :)")

        elif option == '2':
            id_num = int(input("Enter Cow ID number to remove: "))
            homestead.remove_cow(id_num)
            print("Cow Removed from Homestead Cow Herd :/")

        elif option == '3':
            print(f"Total Weekly Weight: {homestead.total_weekly_weight()} pounds")

        elif option == '4':
            print(f"Total Weekly Milk Collected: {homestead.total_weekly_milk()} gallons")

        elif option == '5':
            id_num = int(input("Enter Cow ID number to update health issues: "))
            health_issues = input("Enter new health issues: ")
            homestead.update_health_issues(id_num, health_issues)
            print("Health issues updated!")

        elif option == '6':
            id_num = int(input("Enter Cow ID number to add feed: "))
            feed_amount = float(input("Enter feed amount given (in pounds): "))
            homestead.add_feed(id_num, feed_amount)
            print("Update to feed given complete!")

        elif option == '7':
            id_num = int(input("Enter Cow ID number to generate a complete report: "))
            report = homestead.generate_report(id_num)
            if report:
                print("\nCow Report")
                for key, value in report.items():
                    print(f"{key}: {value}")
            else:
                print("Unfortunately, that Cow cannot be found!")
                print("Please double-check your records.")

        elif option == '8':
            print("Thank you for utilizing the Homestead Management Program!")
            print("Keep up the hard work!")
            print("Bye for now!")
            break

        else:
            print("I'm sorry. That isn't a menu option. Please try again.")
            print("Remember to select from options 1 to 8.")

if __name__ == "__main__":
    main()
