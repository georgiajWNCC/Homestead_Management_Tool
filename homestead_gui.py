"""
    Name: homestead_gui.py
    Author: Jonathan Georgiades
    Created: 31 October 2024
    First Revision: 12 November 2024
    Second Revision: 28 November 2024
    Purpose: Python gui class module for user interation with main program.
"""


# Import tkinter library for GUI
# Import messagebox for alerts and simpledialog for dialog inputs
import tkinter as tk  
from tkinter import messagebox, simpledialog  
# Import the get_weather function from weather_api.py
from weather_api import get_weather
# Import the Homestead class from the appropriate module
from homestead import Homestead
from cow import Cow
from sheep import Sheep
from goat import Goat
from chicken import Chicken
from pig import Pig
from rabbit import Rabbit

#--------------------------------- HOMESTEAD GUI CLASS -------------------------------------- #

# Create homestead gui class
# Use homestead instance
class HomesteadGUI:
    def __init__(self, root, homestead):
        self.homestead = homestead  

        # Set up main application window
        # Set the window title
        self.root = root
        self.root.title("Homestead Management Tool")

        # Set the window icon 
        self.root.iconbitmap("Barn.ico")  
  

        # Create label to display program title
        self.title_label = tk.Label(root, text="Homestead Management Tool", fg="blue", font=("Helvetica", 22, "bold"))
        self.title_label.pack(pady=10)  

        
        # Create buttons for functionalities
        # Define button styles
        button_style = {"width": 20, "height": 2, "font": ("Arial", 12), "bd": 2}

        # Create buttons for functionalities
        # add animal button
        # reomve animal button
        # total feed consumed by animal button
        # generate report button
        # exit program button
        # Create spacing for buttons, pady = 5
        self.add_button = tk.Button(root, text="Add Animal", command=self.add_animal, fg="blue",**button_style)
        self.add_button.pack(pady=5)  

        self.remove_button = tk.Button(root, text="Remove Animal", command=self.remove_animal, fg="red",**button_style)
        self.remove_button.pack(pady=5)

        self.feed_button = tk.Button(root, text="Total Feed Consumed", command=self.display_total_feed, fg="green",**button_style)
        self.feed_button.pack(pady=5)

        self.report_button = tk.Button(root, text="Generate Report", command=self.display_report, fg="orange", **button_style)
        self.report_button.pack(pady=5)

        # Add a weather button for get weather function
        self.weather_button = tk.Button(root, text="Get Weather Update", command=self.display_weather, fg="purple", **button_style)
        self.weather_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit Program", command=self.exit_program, fg="red",**button_style)
        self.exit_button.pack(pady=5)

    # Create method to display weather info by calling the get_weather function from weather_api.py
    def display_weather(self):
        location = simpledialog.askstring("Weather Data:", "Enter a Location (Example: Scottsbluff, NE, US):")
        if location:
            weather_data = get_weather(location)  # Call the function from weather_api.py
            if isinstance(weather_data, dict):  # Check if the response is successful
                # Extract the relevant weather data you want to display
                weather_description = weather_data['weather'][0]['description']
                temperature = weather_data['main']['temp']
                humidity = weather_data['main']['humidity']
                report = f"Weather in {location}:\n" \
                         f"Description: {weather_description}\n" \
                         f"Temperature: {temperature}°F\n" \
                         f"Humidity: {humidity}%"
                messagebox.showinfo("Weather Report", report)
            else:
                messagebox.showerror("Error", weather_data)  # Display an error message if the API request fails
        else:
            messagebox.showwarning("No Location", "Please enter a valid location.") # Display an error message if the location is invalid

    
    # Create method to prompt user to add an animal
    def add_animal(self):
        # Get animal type, ID, breed, etc., through dialogs
        animal_type = simpledialog.askstring("Add Animal", "Enter Animal Type (cow, sheep, goat, chicken, pig, rabbit):")
        
        if animal_type:
            # Create try-except block to handle user input
            try:
                id_num = int(simpledialog.askstring("Add Animal", "Enter animal ID number:"))
                breed = simpledialog.askstring("Add Animal", "Enter breed:")
                age = int(simpledialog.askstring("Add Animal", "Enter age (in years):"))
                health_issues = simpledialog.askstring("Add Animal", "Enter health issues:")
                weekly_weight = int(simpledialog.askstring("Add Animal", "Enter weekly weight (in pounds):"))
                feed_consumed = float(simpledialog.askstring("Add Animal", "Enter total feed consumed (in pounds):"))

                # Create animal based on the animal type
                if animal_type.lower() == 'cow':
                    weekly_milk_collected = float(simpledialog.askstring("Add Animal", "Enter weekly milk collected (in gallons):"))
                    animal = Cow(id_num, breed, age, health_issues, weekly_weight, feed_consumed, weekly_milk_collected)
                elif animal_type.lower() == 'sheep':
                    animal = Sheep(id_num, breed, age, health_issues, weekly_weight, feed_consumed)
                elif animal_type.lower() == 'goat':
                    animal = Goat(id_num, breed, age, health_issues, weekly_weight, feed_consumed)
                elif animal_type.lower() == 'chicken':
                    weekly_egg_collected = float(simpledialog.askstring("Add Animal", "Enter weekly egg collected (in number of eggs):"))
                    animal = Chicken(id_num, breed, age, health_issues, weekly_weight, feed_consumed, weekly_egg_collected)
                elif animal_type.lower() == 'pig':
                    animal = Pig(id_num, breed, age, health_issues, weekly_weight, feed_consumed)
                elif animal_type.lower() == 'rabbit':
                    animal = Rabbit(id_num, breed, age, health_issues, weekly_weight, feed_consumed)
                else:
                    # If an invalid animal type is entered, show an error
                    messagebox.showerror("Invalid Animal Type", f"{animal_type} is not a valid animal type.")
                    return  # Exit the method if invalid type is entered

                # Add the animal to the homestead
                self.homestead.add_animal(animal)
                messagebox.showinfo("Success", f"{animal_type.capitalize()} has been added.")
            
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid numeric values.")


    # Create method to prompt the user to remove an animal
    def remove_animal(self):
        animal_id = simpledialog.askstring("Remove Animal", "Enter the animal ID to remove:")
        if animal_id:
            try:
                if self.homestead.remove_animal(animal_id):
                    messagebox.showinfo("Success", f"Animal ID {animal_id} has been removed.")
                else:
                    messagebox.showwarning("Not Found", f"Animal ID {animal_id} not found in the homestead.")
            # Handle any invalid user input, except ValueError
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid ID number.")

    # Create method to display the total amount of feed consumed
    def display_total_feed(self):
        total_feed = self.homestead.total_feed_consumed()
        messagebox.showinfo("Total Feed Consumed", f"Total feed consumed: {total_feed} pounds")

    
    # Create method to generate and display a report of all animals to the user
    def display_report(self):
        # Prompt user for ID number if they want a specific animal's report
        id_number = simpledialog.askstring("Generate Report", "Enter animal ID for a specific report (or leave blank for all animals):")
        
        # If the user enters an ID number, generate a report for that specific animal
        if id_number:
            try:
                id_number = int(id_number)  # Convert to integer
                report = self.homestead.generate_report(id_number)
                if report:
                    report_text = "\n".join([f"{key}: {value}" for key, value in report.items()])
                    messagebox.showinfo("Animal Report", report_text)
                else:
                    messagebox.showwarning("Not Found", f"Animal ID {id_number} not found.")
            except ValueError:
                messagebox.showerror("Input Error", "Please enter a valid numeric ID number.")
        else:
            # If no ID number is entered, generate a report for all animals
            report = self.homestead.generate_report()
            report_text = "\n\n".join([f"Animal {i+1}:\n" + "\n".join([f"{key}: {value}" for key, value in animal_report.items()])
                                    for i, animal_report in enumerate(report)])
            messagebox.showinfo("Animal Report", report_text)

    # Create method to exit the program, prompting the user for confirmation
    def exit_program(self):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.root.destroy()  # Close the application window

# Main entry point of the application
# Create main app window
# Instantiate GUI class with homestead instance
# Start tkinter event loop to keep application running
if __name__ == "__main__":
    root = tk.Tk()  
    homestead = Homestead()  
    gui = HomesteadGUI(root, homestead)  
    root.mainloop()  
