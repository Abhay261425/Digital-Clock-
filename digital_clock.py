import tkinter as tk
import time

def update_time():
  """Updates the clock label with the current time."""
  current_time = time.strftime("%I:%M:%S %P") # Get time in 12-hour format
  time_label.config(text= current_time) # Update the label with the new time
  time_label.after(1000,update_time) # Schedule the function to run again in 1 second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150") # Set the window size
root.configure(bg="black") # Set the background color


time_label. = tk.Labek(root, font=("Arial",40,"bold"),bg="black",fg="white")
time_label.pack(pady=20) # Add some padding around the label

# Start the clock
update_time() # Call the update_time function initially
root.mainloop() # Run the Tkinter event loop
