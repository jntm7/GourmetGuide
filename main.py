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


    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        
        file_menu.add_command(label="Save", command=self.save_recipes)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)


    def search_recipes(self):
        cuisine_type = self.cuisine_var.get()
        meal_type = self.meal_var.get()

        if not cuisine_type or not meal_type:
            messagebox.showerror("Error", "Please select both cuisine and meal type")
            return

        url = f'https://api.edamam.com/search?q={meal_type}&app_id={EDMAM_APPLICATION_ID}&app_key={EDMAM_APPLICATION_KEY}&cuisineType={cuisine_type}'

        response = requests.get(url)

        if response.status_code == 200:
            recipes = response.json().get('hits', [])
            self.display_recipes(recipes)

        else:
            messagebox.showerror("Error: failed to fetch recipes.")

    def display_recipes(self, recipes):
        self.results_text.delete(1.0, tk.END)

        for recipe in recipes:
            recipe_data = recipe['recipe']
            recipe_name = recipe_data['label']
            ingredients = ', '.join(recipe_data['ingredientLines'])
            calories = recipe_data['calories']

            self.results_text.insert(tk.END, f"Recipe: {recipe_name}\nIngredients: {ingredients}\nCalories: {calories}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = GetRecipe(root)
    root.mainloop()