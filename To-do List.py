import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the to-do list
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


# Function to update/edit the selected task
def update_task():
    try:
        index = listbox.curselection()
        updated_task = entry.get()
        if updated_task:
            listbox.delete(index)
            listbox.insert(index, updated_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an updated task.")
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Function to delete a selected task from the to-do list
def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Main window
window = tk.Tk()
window.title("To-Do List")


# To-do list
listbox = tk.Listbox(window, width=50, height=10, font=("Arial", 12))
listbox.pack(pady=20)

# Scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Scrollbar to the to-do list
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Task entry field
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=10)

# Buttons to add, update and delete tasks
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=10)
update_button = tk.Button(window, text="Update Task", command=update_task)
update_button.pack(pady=10)
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=10)

# GUI main loop
window.mainloop()