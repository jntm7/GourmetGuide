import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
import json
from config import EDMAM_APPLICATION_ID, EDMAM_APPLICATION_KEY
from ctypes import windll

from interface import GourmetGuideUI
from menu import create_menu
from search import search_recipes


windll.shcore.SetProcessDpiAwareness(1)

class GourmetGuideApp:
    def __init__(self, root):
        self.root = root
        self.ui = GourmetGuideUI(root)
        self.ui.bind_search_command(self.search_recipes)
        create_menu(root, self.ui.save_recipes)

    def search_recipes(self):
        cuisine_type = self.ui.cuisine_var.get()
        meal_type = self.ui.meal_var.get()

        if not cuisine_type or not meal_type:
            messagebox.showinfo("Info", "Please select both Cuisine and Meal types.")
            return

        recipes = search_recipes(cuisine_type, meal_type)
        
        if recipes:
            self.ui.display_recipes(recipes)
        
        else:
            messagebox.showinfo("Error", "Failed to retrieve recipes.")


    # Save Recipes
    def save_recipes(self, recipes):
        if not hasattr(self, 'recipes') or not self.recipes:
            messagebox.showinfo("Info", "No recipes to save.")
            return
        
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if save_path:
            with open(save_path, 'w') as f:
                for recipe in self.recipes:
                    recipe_data = recipe['recipe']
                    recipe_name = recipe_data['label']
                    ingredients = ', '.join(recipe_data['ingredientLines'])
                    calories = recipe_data['calories']
                    f.write(f"Recipe: {recipe_name}\nIngredients: {ingredients}\nCalories: {calories}\n\n")
            messagebox.showinfo("Info", "Recipes saved successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GourmetGuideApp(root)
    root.mainloop()