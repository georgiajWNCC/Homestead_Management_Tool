"""
    Name: homestead_gui.py
    Author: Jonathan Georgiades
    Created: 24 October 2024
    Purpose: Python gui class module for user interation with main program.
"""


# Import rich library
import rich
from rich.console import Console
from rich.panel import Panel

# --------------------------------- HOMESTEAD GUI CLASS --------------------------- #
class HomesteadGUI:
    def __init__(self):
        # Initialize the homestead management system
        self.homestead = Homestead()

    def run(self):
        # Menu loop for the program
        while True:
            # Display menu title using Rich panel for formatting
            console.print(
                Panel.fit(
                    "\nGEORGIADES HOMESTEAD MANAGEMENT MENU",
                    style="bold blue"
                )
            )

            # Display menu options
            print("\nMENU OPTIONS")
            console.print(Panel.fit("1. Add Animal", style="bold green"))
            console.print(Panel.fit("2. Remove Animal", style="bold red"))
            console.print(Panel.fit("3. Total Feed Consumed", style="bold cyan"))
            console.print(Panel.fit("4. Generate Report", style="bold yellow"))
            console.print(Panel.fit("5. Exit Program", style="bold magenta"))

            # Prompt user for menu option
            option = input("\nChoose an Option from the Menu: ")

            if option == '1':
                self.add_animal()  # Call method to add an animal
            elif option == '2':
                self.remove_animal()  # Call method to remove an animal
            elif option == '3':
                self.display_total_feed()  # Call method to display total feed consumed
            elif option == '4':
                self.display_report()  # Call method to display the report
            elif option == '5':
                print("Thank you for using the Homestead Management Program!")
                break  # Exit the program
            else:
                print("Invalid option. Please try again.")  # Handle invalid input
