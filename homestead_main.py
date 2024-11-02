"""
    Name: homestead_main.py
    Author: Jonathan Georgiades
    Created: 26 September 2024
    Edited: 24 October 2024
    Edited: 30 October 2024
    Purpose: Python main homestead program that imports
    chicken, cow, goat, pig, and rabbit classes.  Imports 
    HomesteadGUI to run GUI.
"""
# Import tkinter library for GUI
# Import messagebox for alerts
# and simpledialog for dialog inputs
import tkinter as tk  
from tkinter import messagebox, simpledialog  

# Import animal classes for management program
from animal import Animal  # Base class for animals
from cow import Cow
from sheep import Sheep
from goat import Goat
from chicken import Chicken
from pig import Pig
from rabbit import Rabbit

# Import Homestead and the HomesteadGUI classes from modules
from homestead import Homestead
from homestead_gui import HomesteadGUI

# Main entry point of the application
# Initialize the Homestead Management Tool application
def main():
    homestead = Homestead()  # Create an instance of the Homestead class
    root = tk.Tk()  # Create the main application window
    gui = HomesteadGUI(root, homestead)  # Pass the homestead instance to the GUI
    root.mainloop()  # Start the Tkinter event loop to keep the application running

# Call the main function
if __name__ == "__main__":
    main()
