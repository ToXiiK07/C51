"""
Extended Tkinter Example
This script demonstrates the basic structure of a Tkinter application in Python.
Each section is accompanied by a description of what it does.
"""

import tkinter as tk  # Import the Tkinter library

# Create the main window (root)
root = tk.Tk()  # Initialize the Tkinter window
root.title("Extended Tkinter Window")  # Set the window title
root.geometry("500x400")  # Set the size of the window (width x height)

# Description: This label is just a simple text displayed on the window.
label = tk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))  # Create a label widget
label.pack(pady=20)  # Add the label to the window with padding on the Y-axis

# Description: This button closes the application when clicked.
def on_button_click():
    root.quit()  # Close the application

button = tk.Button(root, text="Close", command=on_button_click)  # Create a button widget
button.pack(pady=10)  # Add the button below the label with padding

# Description: Entry allows users to type text in the window.
entry = tk.Entry(root, width=30)  # Create an entry widget
entry.pack(pady=5)  # Add the entry to the window with a small padding

# Description: This button displays the text from the entry when clicked.
def show_text():
    input_text = entry.get()  # Get the text from the entry widget
    label.config(text=f"Input: {input_text}")  # Update the label with the input text

submit_button = tk.Button(root, text="Show Text", command=show_text)  # Create a button to show text
submit_button.pack(pady=10)  # Add this button below the entry widget

# Description: Create a dropdown menu to select items.
OPTIONS = ["Option 1", "Option 2", "Option 3"]
selected_option = tk.StringVar()
selected_option.set(OPTIONS[0])  # Set the default option

def show_option():
    label.config(text=f"Selected: {selected_option.get()}")

dropdown = tk.OptionMenu(root, selected_option, *OPTIONS)  # Create a dropdown menu
dropdown.pack(pady=10)  # Add the dropdown menu to the window

option_button = tk.Button(root, text="Show Selected Option", command=show_option)  # Button to show selected option
option_button.pack(pady=10)

# Description: Add a checkbutton (checkbox) widget.
check_var = tk.IntVar()  # Variable to store checkbox state (0 for unchecked, 1 for checked)

def toggle_check():
    status = "Checked" if check_var.get() == 1 else "Unchecked"
    label.config(text=f"Checkbox is {status}")

checkbox = tk.Checkbutton(root, text="Check me!", variable=check_var, command=toggle_check)  # Create a checkbox
checkbox.pack(pady=10)  # Add the checkbox to the window

# Start the Tkinter event loop (this keeps the window open)
root.mainloop()
