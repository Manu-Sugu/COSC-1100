# Name: Manu Sugunakumar
# App name: Caesar Cipher
# Date: December 5, 2022
# Description: App that takes a users message and encrypts or decrypts it.

from tkinter import *          # Import the tkinter module
from tkinter.ttk import *      # Replace the W95 look with a modern one
from tkinter import messagebox # Pop-up message

# Constants
ENCRYPTION_KEY = 200
ENCRYPT_ANSWER = "encrypt"
DECRYPT_ANSWER = "decrypt"

# Defining functions
def encrypt(message:str):
    """
    Encrypts the data in the message parameter
    """
    # blank variable to start creating the encrypted message
    encrypted_message = ""
    for letter in message:
        # Encrypt the letter by getting its numeric value and adding the ENCRYPTION_KEY
        encrypted_message += chr(ord(letter) + ENCRYPTION_KEY)
    # returns the encrypted message
    return encrypted_message

def decrypt(message:str):
    """
    Decrypts the data in the message parameter
    """
    # blank variable to start creating the decrypted message
    decrypted_message = ""
    for letter in message:
        # Decrypt the letter by getting its numeric value and subtracting the ENCRYPTION_KEY
        decrypted_message += chr(ord(letter) - ENCRYPTION_KEY)
    # returns the decrypted nessage
    return decrypted_message

def convert_click():
    """
    Executed when [Convert] button is clicked
    * Finds out if user wants to encrypt or decrypt
    * Calls either encrypt or decrypt function based on user selection
    * Outputs an error message box if no selection was made
    * Sets the output as the result
    """
    # Takes the user's message and stores it in a variable
    message = input_text.get()
    # Checks if the user wants to encrypt or decrypt then uses the respective function to do so
    if encrypt_decrypt_answer.get() == ENCRYPT_ANSWER:
        result = encrypt(message)
    elif encrypt_decrypt_answer.get() == DECRYPT_ANSWER:
        result = decrypt(message)
    else:
        messagebox.showwarning(title="Warning!", message="You must select either encrypt or decrypt!")
    # Sets the output text as the resulting decryption/encryption
    output_text.set(result)

def clear_click():
    """
    Executed when [Clear] button is clicked
    *Resets the app to default parameters
    """
    # Set default values
    input_text.set("")
    output_text.set("")
    encrypt_decrypt_answer.set("")

# Setup the window
window = Tk()                                    # Create a window
window.title("Caesar Cipher - Manu Sugunakumar") # Change the title
window.iconbitmap("Cipher.ico")                  # Sets the app icon
window.resizable(width=False,height=False)       # Not resizable

# Frames = holds all the other widgets
input_frame  = Frame()
output_frame = Frame()

# Create labels
input_label  = Label(input_frame,  text="Enter your message")
output_label = Label(output_frame, text="Encrypted/Decrypted Message")

# Variables for entry box
input_text  = Variable()
output_text = Variable()

# Sets default values
input_text.set("")
output_text.set("")

# Create Entries
input_entry  = Entry(input_frame, width=60, textvariable=input_text)
output_entry = Entry(output_frame, state="readonly", cursor="no", width=60, textvariable=output_text)

# Variables for Buttons
encrypt_decrypt_answer = Variable()

# Radio Buttons
encrypt_radiobutton = Radiobutton(input_frame, text="Encrypt", variable=encrypt_decrypt_answer, value=ENCRYPT_ANSWER)
decrypt_radiobutton = Radiobutton(input_frame, text="Decrypt", variable=encrypt_decrypt_answer, value=DECRYPT_ANSWER)

# Buttons
clear_button   = Button(output_frame, text="Clear", command=clear_click)
convert_button = Button(output_frame, text="Convert", command=convert_click)

# Place widgets in the window
# Input Frame widgets
input_frame.pack(padx = 10, pady = 10, side="top")
input_label.pack(anchor="w")
input_entry.pack(anchor="w")
encrypt_radiobutton.pack(anchor="w", side="left")
decrypt_radiobutton.pack(anchor="w", side="left")
#-----------------------------------------------------------
# Output Frame widgets
output_frame.pack(padx = 10, pady = (0,10), side="bottom")
output_label.pack(anchor="w")
output_entry.pack(anchor="w")
clear_button.pack(side="left", pady=(5,0))
convert_button.pack(side="right", pady=(5,0))

# Show the window
window.mainloop()