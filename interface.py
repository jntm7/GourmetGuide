import tkinter as tk
from tkinter import ttk, messagebox

class GourmetGuideUI:
    def __init__(self, root):
        self.root = root
        self.create_preferences()

    def create_preferences(self):

        # Cuisine Type
        self.cuisine_label = tk.Label(self.root, text="Select Cuisine Type:")
        self.cuisine_label.pack()
        self.cuisine_var = tk.StringVar()
        self.cuisine_dropdown = ttk.Combobox(self.root, textvariable=self.cuisine_var)
        self.cuisine_dropdown['values'] = (
            "American",
            "British",
            "Carribean",
            "Chinese",
            "French",
            "Greek",
            "Indian",
            "Italian",
            "Japanese",
            "Korean",
            "Mediterranean",
            "Mexican",
            "Middle Eastern",
            "South American",
            "South East Asian",
        )
        self.cuisine_dropdown.pack()

        # Meal Type
        self.meal_label = tk.Label(self.root, text="Select Meal Type:")
        self.meal_label.pack()
        self.meal_var = tk.StringVar()
        self.meal_dropdown = ttk.Combobox(self.root, textvariable=self.meal_var)
        self.meal_dropdown['values'] = (
            "Breakfast",
            "Lunch",
            "Dinner",
            "Snack",
        )
        self.meal_dropdown.pack()

        # Search Button
        self.search_button = tk.Button(self.root, text="Search", command=self.search_recipes)
        self.search_button.pack()

        # Display results
        self.results_text = tk.Text(self.root, height=20, width=100)
        self.results_text.pack()