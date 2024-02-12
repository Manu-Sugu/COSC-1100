# Name: Manu Sugunakumar
# App name: Temperature Conversion
# Date: December 16, 2022
# Description: App that converts temperature from celius to ferenheit to kelvins

from tkinter import * # Import the tkinter module
from tkinter.ttk import * # Replace the W95 look with a modern one

# Constants
TEMPERATURE_NAMES = ("Celsius", "Fahrenheit", "Kelvin")

# Defining Functions
def celsius(value:float):
    """
    Converts the given temperature to Celsius
    """
    if   temperature_selection.get() == TEMPERATURE_NAMES[0]:
        return value
    elif temperature_selection.get() == TEMPERATURE_NAMES[1]:
        # Conversion from Fahrenheit to Celsius
        converted_value = round((value - 32)* (5/9), 1)
        return converted_value # Return value if conversion selection is same as values unit
    elif temperature_selection.get() == TEMPERATURE_NAMES[2]:
        # Conversion from Kelvin to Celsius
        converted_value = round(value - 273.15, 1)
        return converted_value 

def fahrenheit(value:float):
    """
    Converts the given temperature to Fahrenheit
    """
    if   temperature_selection.get() == TEMPERATURE_NAMES[0]:
        # Conversion from Celsius to Fahrenheit
        converted_value = round((value * (9/5)) + 32, 1)
        return converted_value
    elif temperature_selection.get() == TEMPERATURE_NAMES[1]:
        return value # Return value if conversion selection is same as values unit
    elif temperature_selection.get() == TEMPERATURE_NAMES[2]:
        # Conversion from Kelvin to Fahrenheit
        converted_value = round(1.8*(value-273.15)+32, 1)
        return converted_value 

def kelvin(value:float):
    """
    Converts the given temperature to Kelvin
    """
    if   temperature_selection.get() == TEMPERATURE_NAMES[0]:
        # Conversion from Celsius to Kelvin
        converted_value = round(value + 273.15, 1)
        return converted_value
    elif temperature_selection.get() == TEMPERATURE_NAMES[1]:
        # Conversion from Fahrenheit to Kelvin
        converted_value = round((value-32)*(5/9)+273.15, 1)
        return converted_value
    elif temperature_selection.get() == TEMPERATURE_NAMES[2]:
        return value # Return value if conversion selection is same as values unit

def convert_click():
    """
    Executed when [Convert] Button is clicked
    * Checks for valid input
    * Converts the value according to user selection
    """
    # Gets the user's temperature and stores in the value variable
    value = input_text.get()
    try:
        value = float(value) # Checks if it can conver the value into a float
    except:
        output_text.set("Error value is not numeric!") # sets the output text to an error statment if not numeric value
        return # Exits the function
    # Checks which conversion and calls the appropriate function
    if   temperature_convert.get() == TEMPERATURE_NAMES[0]:
        output_text.set(f"{celsius(value)} °C")
    elif temperature_convert.get() == TEMPERATURE_NAMES[1]:
        output_text.set(f"{fahrenheit(value)} °F")
    elif temperature_convert.get() == TEMPERATURE_NAMES[2]:
        output_text.set(f"{kelvin(value)} K")

def clear_click():
    """
    Executed when [Clear] Button is clicked
    * Resets the app to defualt parameters
    """
    input_text.set("70")
    output_text.set("21.1 °C")
    temperature_selection.set(TEMPERATURE_NAMES[1])
    temperature_convert.set(TEMPERATURE_NAMES[0])

def key_handler(event:Event):
    """Handles key presses"""
    if event.keysym == "Return":   # Enter key
        convert_click()
    elif event.keysym == "Escape": # Escape key
        clear_click()

# Setup the window
window = Tk()                                     # Create a window
window.title("Temperature Conversion - Manu Sugunakumar") # Change the title
window.iconbitmap("Temperature.ico")
window.bind("<Key>", key_handler) # K is uppercase
window.resizable(width=False,height=False)        # Not resizable

# Frame = holds all the other widgets
input_frame       = Frame()
output_frame      = Frame()
radiobutton_frame = Frame()

# Labels
input_label       = Label(input_frame,width = 70, text="Enter your temperature")
output_label      = Label(output_frame,width=70, text="Converted Temperature")
radiobutton_label = Label(radiobutton_frame, text="Convert To")

# Entry Variables
input_text  = Variable()
output_text = Variable()

# Set Default Values
input_text.set("70")
output_text.set("21.1 °C")

# Entry Labels
input_entry  = Entry(input_frame,  width = 56, textvariable=input_text)
output_entry = Entry(output_frame, width = 70, textvariable=output_text, state="readonly", cursor="no")

# Combo Box
temperature_selection = Variable()
temperature_selection.set(TEMPERATURE_NAMES[1]) # Set default value
selections_combobox   = Combobox(input_frame, width=10, values=TEMPERATURE_NAMES, textvariable=temperature_selection, state="readonly")

# Radio Buttons
temperature_convert    = Variable()
temperature_convert.set(TEMPERATURE_NAMES[0]) # Set default value
celsius_radiobutton    = Radiobutton(radiobutton_frame, text="Celsius",    variable=temperature_convert, value=TEMPERATURE_NAMES[0])
fahrenheit_radiobutton = Radiobutton(radiobutton_frame, text="Fahrenheit", variable=temperature_convert, value=TEMPERATURE_NAMES[1])
kelvin_radiobutton     = Radiobutton(radiobutton_frame, text="Kelvin",     variable=temperature_convert, value=TEMPERATURE_NAMES[2])

# Buttons
convert_button = Button(output_frame, text="Convert", command=convert_click)
clear_button   = Button(output_frame, text="Clear",   command=clear_click)

# Place widgets in the window
# Input Frame
input_frame.pack(padx=10,pady=(10,0), anchor="w")
input_label.pack(anchor="w")
input_entry.pack(anchor="w", side="left")
selections_combobox.pack(side="left", anchor="w")
#--------------------------------------------------
# Radio Button Frame
radiobutton_frame.pack(padx=10, pady=2, anchor="w")
radiobutton_label.pack(anchor="w")
celsius_radiobutton.pack(side="left")
fahrenheit_radiobutton.pack(side="left")
kelvin_radiobutton.pack(side="left")
#---------------------------------------------------
# Output Frame
output_frame.pack(padx=10,pady=(0,10))
output_label.pack(anchor="w")
output_entry.pack(anchor="w")
convert_button.pack(pady=(5,0), side="right")
clear_button.pack(pady=(5,0), side="left")

# Show the window
window.mainloop()