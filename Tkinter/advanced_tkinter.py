"""
Advanced Tkinter Example
This script demonstrates a more advanced structure of a Tkinter application in Python.
Each section is accompanied by a description of what it does.
"""

import tkinter as tk  # Import the Tkinter library

# Create the main window (root)
root = tk.Tk()  # Initialize the Tkinter window
root.title("Advanced Tkinter Window")  # Set the window title
root.geometry("600x500")  # Set the size of the window (width x height)

# ----------------------------- Widgets ----------------------------- #

# Description: This label is just a simple text displayed on the window.
label = tk.Label(root, text="Welcome to Advanced Tkinter!", font=("Helvetica", 16))  # Create a label widget
label.pack(pady=20)  # Add the label to the window with padding on the Y-axis

# ----------------------------- Frame ----------------------------- #
# Description: Frames are used to organize widgets within a window.
frame = tk.Frame(root, relief=tk.RAISED, borderwidth=2)  # Create a frame widget
frame.pack(pady=10)  # Add the frame to the window

frame_label = tk.Label(frame, text="This is inside a frame")  # Create a label inside the frame
frame_label.pack()

# ----------------------------- Radio Buttons ----------------------------- #
# Description: Radio buttons allow users to select one option from multiple choices.
radio_var = tk.StringVar()  # Variable to store the selected radio button value
radio_var.set("Option 1")  # Set a default value

def show_radio_choice():
    label.config(text=f"Selected Radio: {radio_var.get()}")

radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=show_radio_choice)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=show_radio_choice)
radio2.pack()

radio3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value="Option 3", command=show_radio_choice)
radio3.pack()

# ----------------------------- Slider (Scale) ----------------------------- #
# Description: Sliders allow users to select a value by sliding a knob along a bar.
def update_slider(val):
    label.config(text=f"Slider at: {val}")

slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=update_slider)  # Create a horizontal slider
slider.pack(pady=20)

# ----------------------------- Canvas ----------------------------- #
# Description: A canvas widget is used for drawing shapes and graphics.
canvas = tk.Canvas(root, width=200, height=150, bg="lightblue")  # Create a canvas
canvas.pack(pady=20)

# Drawing shapes on the canvas
canvas.create_line(0, 0, 200, 150, fill="black", width=2)  # Draw a diagonal line
canvas.create_rectangle(50, 50, 150, 100, fill="red")  # Draw a red rectangle

# ----------------------------- Spinbox ----------------------------- #
# Description: A Spinbox allows users to select a number by clicking the up/down arrows.
def update_spinbox():
    label.config(text=f"Spinbox Value: {spinbox.get()}")

spinbox = tk.Spinbox(root, from_=1, to=10, command=update_spinbox)  # Create a spinbox
spinbox.pack(pady=10)

# ----------------------------- Messagebox ----------------------------- #
# Description: Messageboxes are pop-up dialogs used to show alerts, confirm actions, etc.
from tkinter import messagebox

def show_messagebox():
    messagebox.showinfo("Message", "This is a Tkinter MessageBox!")  # Show an information message box

message_button = tk.Button(root, text="Show Message Box", command=show_messagebox)  # Button to trigger the message box
message_button.pack(pady=10)

# Start the Tkinter event loop (this keeps the window open)
root.mainloop()
