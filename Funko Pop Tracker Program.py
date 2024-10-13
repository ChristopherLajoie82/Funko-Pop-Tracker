# Funko Pop Tracker Program with GUI
import json
import os
import tkinter as tk
from tkinter import messagebox

# File path to save the collection
data_file = "funko_collection.json"

# Initialize an empty list to store Funko Pop details
funko_collection = []

# Function to load the Funko Pop collection from the file
def load_collection():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Function to save the Funko Pop collection to the file
def save_collection():
    with open(data_file, "w") as file:
        json.dump(funko_collection, file)

# Function to add a Funko Pop to the collection
def add_funko_pop():
    dialog = tk.Toplevel()
    dialog.title("Add Funko Pop")
    dialog.geometry("400x300")

    tk.Label(dialog, text="Enter Funko Pop name:").pack(pady=5)
    name_entry = tk.Entry(dialog, width=30)
    name_entry.pack(pady=5)

    tk.Label(dialog, text="Enter Funko Pop collection:").pack(pady=5)
    collection_entry = tk.Entry(dialog, width=30)
    collection_entry.pack(pady=5)

    tk.Label(dialog, text="Enter Funko Pop price:").pack(pady=5)
    price_entry = tk.Entry(dialog, width=30)
    price_entry.pack(pady=5)

    def submit():
        name = name_entry.get()
        collection = collection_entry.get()
        try:
            price = float(price_entry.get())
            if name and collection:
                funko_collection.append({
                    "name": name,
                    "collection": collection,
                    "price": price
                })
                messagebox.showinfo("Success", f"{name} has been added to the collection.")
                save_collection()
            else:
                messagebox.showerror("Error", "Name and collection cannot be empty.")
            dialog.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid price. Please enter a numeric value.")

    submit_button = tk.Button(dialog, text="Add", command=submit)
    submit_button.pack(pady=10)

# Function to display collection information
def collection_information():
    if funko_collection:
        sorted_collection = sorted(funko_collection, key=lambda x: x['name'].lower())
        collection_info = "Your Funko Pop Collection:\n"
        for index, funko in enumerate(sorted_collection, start=1):
            collection_info += f"{index}. Name: {funko['name']}, Collection: {funko['collection']}, Price: ${funko['price']:.2f}\n"
        total_value = sum(funko['price'] for funko in funko_collection)
        collection_info += f"\nTotal Funko Pops Owned: {len(funko_collection)}\n"
        collection_info += f"The total value of your Funko Pop collection is: ${total_value:.2f}"
        return collection_info
    else:
        return "Your collection is empty."

# Function to remove a Funko Pop from the collection
def remove_funko_pop():
    if funko_collection:
        dialog = tk.Toplevel()
        dialog.title("Remove Funko Pop")
        dialog.geometry("500x400")

        collection_info = collection_information()
        tk.Label(dialog, text=collection_info, justify="left").pack(pady=5)

        tk.Label(dialog, text="Enter the number of the Funko Pop to remove:").pack(pady=5)
        index_entry = tk.Entry(dialog, width=10)
        index_entry.pack(pady=5)

        def submit():
            try:
                index = int(index_entry.get()) - 1
                if 0 <= index < len(funko_collection):
                    removed_funko = funko_collection.pop(index)
                    messagebox.showinfo("Success", f"{removed_funko['name']} has been removed from the collection.")
                    save_collection()
                    dialog.destroy()
                else:
                    messagebox.showerror("Error", "Invalid selection. Please enter a valid number.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

        submit_button = tk.Button(dialog, text="Remove", command=submit)
        submit_button.pack(pady=10)
    else:
        messagebox.showinfo("Remove Funko Pop", "Your collection is empty.")

# Main program loop with GUI
def main():
    global funko_collection
    funko_collection = load_collection()

    # Create the main window
    root = tk.Tk()
    root.title("Funko Pop Tracker Program")

    # Add welcome text
    welcome_label = tk.Label(root, text="Welcome to Funko Pop Tracker", font=("Helvetica", 16))
    welcome_label.pack(pady=10)

    # Add buttons for each action
    add_button = tk.Button(root, text="Add Funko Pop", command=add_funko_pop)
    add_button.pack(pady=5)

    info_button = tk.Button(root, text="Collection Information", command=lambda: messagebox.showinfo("Collection Information", collection_information()))
    info_button.pack(pady=5)

    remove_button = tk.Button(root, text="Remove Funko Pop", command=remove_funko_pop)
    remove_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=5)

    # Start the main event loop
    root.mainloop()

# Run the program
if __name__ == "__main__":
    main()