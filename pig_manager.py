"""
    Name: pig_manager.py
    Author: Jonathan Georgiades
    Created: 26 September 2024
    Purpose: Python homesteading pig management program that tracks
    the breed, age, health, monthly weight, and feed amount consumed
"""

import datetime
import rich
from rich.console import Console
from rich.panel import Panel

console = Console()

# ----------------------------------- PIG CLASS --------------------------------------- #
class Pig:
    def __init__(self, id_number, breed, age, health_issues, weekly_weight, feed_consumed):
        self.id_number = id_number
        self.breed = breed
        self.age = age
        self.health_issues = health_issues
        self.weekly_weight = weekly_weight
        self.feed_consumed = feed_consumed

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

    # Setters
    def set_health_issues(self, health_issues):
        self.health_issues = health_issues

    def set_weekly_weight(self, weekly_weight):
        self.weekly_weight = weekly_weight

    def set_feed_consumed(self, feed_consumed):
        self.feed_consumed = feed_consumed

# ----------------------------------- HOMESTEAD CLASS --------------------------------------- #
class Homestead:
    def __init__(self):
        self.pigs = []

    def add_pig(self, pig):
        self.pigs.append(pig)

    def remove_pig(self, id_number):
        self.pigs = [pig for pig in self.pigs if pig.get_id_number() != id_number]

    def total_weekly_weight(self):
        return sum(pig.get_weekly_weight() for pig in self.pigs)

    def create_health_report(self):
        report = {}
        for pig in self.pigs:
            report[pig.get_id_number()] = pig.get_health_issues()
        return report
    
    def total_feed_consumed(self):
        return sum(pig.get_feed_consumed() for pig in self.pigs)

    def update_health_issues(self, id_number, health_issues):
        for pig in self.pigs:
            if pig.get_id_number() == id_number:
                pig.set_health_issues(health_issues)

    def add_feed(self, id_number, feed_amount):
        for pig in self.pigs:
            if pig.get_id_number() == id_number:
                pig.set_feed_consumed(pig.get_feed_consumed() + feed_amount)

    def generate_report(self, id_number):
        for pig in self.pigs:
            if pig.get_id_number() == id_number:
                return {
                    "ID Number": pig.get_id_number(),
                    "Breed": pig.get_breed(),
                    "Age": pig.get_age(),
                    "Health Issues": pig.get_health_issues(),
                    "Weekly Weight (lbs)": pig.get_weekly_weight(),
                    "Feed Consumed": pig.get_feed_consumed()
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
        console.print(Panel.fit("1. Add Pig", style="bold green"))
        console.print(Panel.fit("2. Remove Pig", style="bold red"))
        print("3. Weekly Weight")
        print("4. Update Health Issues")
        print("5. Add To Feed Total")
        console.print(Panel.fit("6. Generate Pig Status Report", style="bold cyan"))
        console.print(Panel.fit("7. Exit Program", style="bold yellow"))

        option = input("\nChoose Menu Option: ")

        if option == '1':
            id_num = int(input("Enter Pig ID number: "))
            breed = input("Enter Breed: ")
            age = int(input("Enter Pig Age (in years): "))
            health_issues = input("Enter Known Health Issues (e.g., parasites, anemia, flu, none, etc): ")
            weekly_weight = int(input("Enter Weekly Weight (in pounds): "))
            feed_consumed = float(input("Enter Total Feed Consumed (in pounds): "))
            pig = Pig(id_num, breed, age, health_issues, weekly_weight, feed_consumed)
            homestead.add_pig(pig)
            print("Pig Added to Homestead Pig Herd :)")

        elif option == '2':
            id_num = int(input("Enter Pig ID number to remove: "))
            homestead.remove_pig(id_num)
            print("Pig Removed from Homestead Pig Herd :/")

        elif option == '3':
            print(f"Total Weekly Weight: {homestead.total_weekly_weight()} pounds")

        elif option == '4':
            id_num = int(input("Enter Pig ID number to update health issues: "))
            health_issues = input("Enter new health issues: ")
            homestead.update_health_issues(id_num, health_issues)
            print("Health issues updated!")

        elif option == '5':
            id_num = int(input("Enter Pig ID number to add feed: "))
            feed_amount = float(input("Enter feed amount given (in pounds): "))
            homestead.add_feed(id_num, feed_amount)
            print("Update to feed given complete!")

        elif option == '6':
            id_num = int(input("Enter Pig ID number to generate a complete report: "))
            report = homestead.generate_report(id_num)
            if report:
                print("\nPig Report")
                for key, value in report.items():
                    print(f"{key}: {value}")
            else:
                print("Unfortunately, that Pig cannot be found!")
                print("Please double-check your records.")

        elif option == '7':
            print("Thank you for utilizing the Homestead Management Program!")
            print("Keep up the hard work!")
            print("Bye for now!")
            break

        else:
            print("I'm sorry. That isn't a menu option. Please try again.")
            print("Remember to select from options 1 to 7.")

if __name__ == "__main__":
    main()
