# Import tkinter, json and random
import tkinter as tk
import json as js
import random as rd

# Create the window
window = tk.Tk()
# Set window title
window.title("Quick Quotes")

# Open the quotes.json file and read and store the data within it
with open("quotes.json", "r") as quotes_data:
    quotes = js.load(quotes_data)

# Create a label with text randomly selected from the quotes data
word = tk.Label(text=rd.choice(quotes["quotes"])["text"],
                height=7,
                bg="#5c9aff").pack()

# Begin main loop
window.mainloop()