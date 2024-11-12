"""
    Name: homestead_gui.py
    Author: Jonathan Georgiades
    Created: 31 October 2024
    Purpose: Python gui class module for user interation with main program.
"""

# Import tkinter library for GUI
# Import messagebox for alerts and simpledialog for dialog inputs
import tkinter as tk  
from tkinter import messagebox, simpledialog  

# Import the Homestead class from the appropriate module
from homestead import Homestead

#--------------------------------- HOMESTEAD GUI CLASS -------------------------------------- #

class HomesteadGUI:
    def __init__(self, root, homestead):
        self.homestead = homestead  # Use the passed homestead instance

        # Set up the main application window
        self.root = root
        self.root.title("Homestead Management Tool")  # Title of the window

        # Create label to display program title
        self.title_label = tk.Label(root, text="Georgiades Homestead Management", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)  

        # Create buttons for different functionalities
        self.add_button = tk.Button(root, text="Add Animal", command=self.add_animal)
        self.add_button.pack(pady=5)  

        self.remove_button = tk.Button(root, text="Remove Animal", command=self.remove_animal)
        self.remove_button.pack(pady=5)

        self.feed_button = tk.Button(root, text="Total Feed Consumed", command=self.display_total_feed)
        self.feed_button.pack(pady=5)

        self.report_button = tk.Button(root, text="Generate Report", command=self.display_report)
        self.report_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit Program", command=self.exit_program)
        self.exit_button.pack(pady=5)

    # Method to prompt the user to add an animal
    def add_animal(self):
        # Get animal type, ID, breed, etc., through dialogs
        animal_type = simpledialog.askstring("Add Animal", "Enter animal type (cow, sheep, goat, chicken, pig, rabbit):")
        if animal_type:
            try:
                id_num = int(simpledialog.askstring("Add Animal", "Enter animal ID number:"))
                breed = simpledialog.askstring("Add Animal", "Enter breed:")
                age = int(simpledialog.askstring("Add Animal", "Enter age (in years):"))
                health_issues = simpledialog.askstring("Add Animal", "Enter health issues:")
                weekly_weight = int(simpledialog.askstring("Add Animal", "Enter weekly weight (in pounds):"))
                feed_consumed = float(simpledialog.askstring("Add Animal", "Enter total feed consumed (in pounds):"))

                # Create the animal based on type
                if animal_type.lower() == 'cow':
                    weekly_milk_collected = float(simpledialog.askstring("Add Animal", "Enter weekly milk collected (in gallons):"))
                    animal = Cow(id_num, breed, age, health_issues, weekly_weight, feed_consumed, weekly_milk_collected)
                # Repeat for other animal types...
                else:
                    # Example for sheep
                    if animal_type.lower() == 'sheep':
                        animal = Sheep(id_num, breed, age, health_issues, weekly_weight, feed_consumed)
                    # Add other animal types similarly...

                self.homestead.add_animal(animal)  # Add the animal to the homestead
                messagebox.showinfo("Success", f"{animal_type.capitalize()} has been added.")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numeric values.")

    # Method to prompt the user to remove an animal
    def remove_animal(self):
        animal_id = simpledialog.askstring("Remove Animal", "Enter the animal ID to remove:")
        if animal_id:
            try:
                if self.homestead.remove_animal(animal_id):
                    messagebox.showinfo("Success", f"Animal ID {animal_id} has been removed.")
                else:
                    messagebox.showwarning("Not Found", f"Animal ID {animal_id} not found in the homestead.")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid ID number.")

    # Method to display the total feed consumed
    def display_total_feed(self):
        total_feed = self.homestead.total_feed_consumed()
        messagebox.showinfo("Total Feed Consumed", f"Total feed consumed: {total_feed} pounds")

    # Method to generate and display a report of all animals
    def display_report(self):
        report = self.homestead.generate_report()
        report_text = "\n".join([f"{animal_type.capitalize()}: {count}" for animal_type, count in report.items()])
        messagebox.showinfo("Animal Report", report_text)

    # Method to exit the program, prompting the user for confirmation
    def exit_program(self):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.root.destroy()  # Close the application window

# Main entry point of the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    homestead = Homestead()  # Create an instance of the Homestead class
    gui = HomesteadGUI(root, homestead)  # Instantiate the GUI class with the homestead instance
    root.mainloop()  # Start the Tkinter event loop to keep the application running
