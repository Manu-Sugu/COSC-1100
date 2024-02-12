# Name: Manu Suguankumar
# Date: October 11, 2022
# App Name: PizzaPi
# Description: To calculate the number of slices to calculate on a pizza given the diameter of the pizza.

# Import system(), math
from os import system
import math

# Change the title
system("title Pizza Pi - Manu Sugunakumar")

# Constants - no magic numbers! 🪄
MIN, MAX = 8, 24

diameter = input(f"Please enter the diameter of your pizza: ")

# Try to convert from string to int
try:
    diameter = int(diameter)
    valid = True
except:
    valid = False

# Error when not numeric
if valid == False:
    print("Error - Diameter must be numeric!")
# Error when not between 8" and 24"
elif diameter < MIN or diameter > MAX:
    print(f"Error - Pizza must have a diameter in the range of {MIN}\" to {MAX}\" inclusive!")
# Otherwise start the calculations
else:
    # Checks for how much slices the pizza has
    if diameter < 12:
        number_of_slices = 6
    elif diameter >= 12 and diameter < 14:
        number_of_slices = 8
    elif diameter >= 14 and diameter < 16:
        number_of_slices = 10
    elif diameter >= 16 and diameter < 20:
        number_of_slices = 12
    elif diameter >= 20:
        number_of_slices = 16
    
    # Calculate radius of pizza
    r = float(diameter/2)

    # Calculate area of pizza
    area_of_pizza = float(math.pi*r**2)

    # Calculate area of each slice
    area_of_slice = float(area_of_pizza/number_of_slices)

    # Calculate the angle of each slice
    angle_of_slice = int(360/number_of_slices)

    # Round down the answers to 2 decimal places
    area_of_pizza = round(area_of_pizza, 2)
    area_of_slice = round(area_of_slice, 2)

    # Outputs result
    print(f"A {diameter}\" pizza has an area of {area_of_pizza} square inches and will yield {number_of_slices} slices.\nEach slice will be cut at {angle_of_slice} degrees and have an area of {area_of_slice} square inches.")

# Exit prompt
input("Press [enter] to exit: ")