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
        # Initialize the homestead management program
        self.homestead = Homestead()

    # TODO: Method to run gui
    def run(self):
        # Create while loop for menu program loop 
        while True:
            # Display menu title using rich panel for formatting
            console.print(
                Panel.fit(
                    "\nGEORGIADES HOMESTEAD MANAGEMENT MENU",
                    style="bold blue"
                )
            )

            # Display menu options to user to select from
            print("\nMENU OPTIONS")
            console.print(Panel.fit("1. Add Animal", style="bold green"))
            console.print(Panel.fit("2. Remove Animal", style="bold red"))
            console.print(Panel.fit("3. Total Feed Consumed", style="bold cyan"))
            console.print(Panel.fit("4. Generate Report", style="bold yellow"))
            console.print(Panel.fit("5. Exit Program", style="bold magenta"))

            # Prompt user to select a menu option
            # Use if-else statement for menu options
            option = input("\nChoose an Option from the Menu: ")

            # Call method to add animal
            if option == '1':
                self.add_animal()  
            # Call method to remove an animal
            elif option == '2':
                self.remove_animal()  
            # Call method to display the amount of feed consumed
            elif option == '3':
                self.display_total_feed() 
            # Call method to display a report for the animal
            elif option == '4':
                self.display_report()  
            # Exit the program and display message to user
            # break
            elif option == '5':
                print("Thank you for using the Homestead Management Program!")
                print("Goodbye!")
                break  
            # Else, handle any invalid input from the user
            else:
                print("Invalid option. Please try again.") 
