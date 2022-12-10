# datetime package
from datetime import datetime
# tkinter and customtkinter to display the actual time
import tkinter as tk
import customtkinter as ctk

# Functions
# Gets time


def time_function():
    # Current time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
# Updates the tk label to current time


def update():
    l.config(text=time_function())
    app.after(1000, update)


# Window modes
ctk.set_appearance_mode("System")
# create CTk window like you do with the Tk window
app = ctk.CTk()
# Screen width
screen_width = app.winfo_screenwidth()
# Makes app fullscreen
app.attributes('-fullscreen', True)
# Title of window
app.title("Clock App")
# Makes a label with current time
l = tk.Label(text=time_function(), font=(
    # Chooses font and label size
    f'Times {int(screen_width/5)} bold'))
# labels background color
l.configure(fg="green", background="#242424")
# Places the label in the correct area in the window
l.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# Calls update that updates the app after 1 second
app.after(1000, update)
app.mainloop()
