# Name: Manu Sugunakumar
# App Name: Prime Numbers!
# Date: October 31, 2022👻
# Description: App that takes a user input and calculates all the prime numebrs up to that number and displays them.

# Import the system function
from os import system

# CONSTANTS
MIN, MAX = 2, 100

# DOC String for title
INTRODUCTION = """
===================
== Prime Numbers ==
===================
"""

# Set the title
system("title Prime Numbers - Manu Sugunakumar")

restart = "r" # Needs to run atleast once

while restart == "r":
    system("cls") # Clears the screen

    # Print Intro
    print(INTRODUCTION)

    valid = False # Need to run atleast once

    while not valid:

        # Ask for a number
        number = input(f"Enter a number between {MIN} and {MAX}: ")

        # Try to convert from string to int
        try:
            number = int(number)
            numeric = True
        except:
            numeric = False
        # Error when not numeric
        if numeric == False:
            print("Error - Input must be whole number.")
        
        # Error when not in the valid range
        elif number < MIN or number > MAX:
            print(f"Error - Number must be between {MIN} and {MAX}!")
        # Valid input
        else:
            valid = True

    # Doc string for subtitle
    SUBTITLE = f"""
============================
== Prime Numbers up to {number} ==
============================
    """

    system("cls") # Clears the screen
    print(SUBTITLE) # Prints the subtitle

    # Variables
    number_of_primes = 0 # Must be declared outside the loop

    for count1 in range(MIN,number+1): # This loop counts from 2 up until the number given
        is_prime = True # declaring the is_prime variable
        for count2 in range(MIN,count1):# This loop counts from 2 up until the current number that needs to be checked
            if count1 % count2 == 0:# Checks if theres are remainder if there is none then the number is not a prime and will break the loop
                is_prime = False
                break # Breaks the loop
        if is_prime == True:# Checks if the number is prime
            for hastag in range(0,count1):# Loop for the amount of hastags to output
                print("#",end="")
            print(f" {count1}")# Outputs the number that is a prime
            number_of_primes += 1# Counting the number of prime numbers
    
    # Output Statement
    print(f"\nThere are {number_of_primes} prime numbers from {MIN} up to {number}\n")

    # Exit if anything except r
    restart = input("Enter 'r' to restart: ").lower()