import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from config import EDMAM_APPLICATION_ID, EDMAM_APPLICATION_KEY

class GetRecipe:
    def __init__(self, root):
        self.root = root
        self.root.title("Gourmet Guide")
        self.root.geometry("900x675")
        self.root.resizable(False, False)


    def dropdown_menus(self):

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

if __name__ == "__main__":
    root = tk.Tk()
    app = GetRecipe(root)
    root.mainloop()