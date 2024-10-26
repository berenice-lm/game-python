import webbrowser
import tkinter as tk
from tkinter import messagebox

# Define the function to open the HTML file in the default browser
def open_map():
    try:
        # Provide the correct path to your carte.html file
        webbrowser.open('carte.html')
    except Exception as e:
        messagebox.showerror("Error", f"Could not open the map: {str(e)}")

# Create the main window using tkinter
window = tk.Tk()
window.title("Open Map")

# Create a button that will call the open_map function
open_map_button = tk.Button(window, text="Open Map", command=open_map)
open_map_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()