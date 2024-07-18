import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from config import EDMAM_API_ID, EDMAM_API_KEY

class GetRecipe:
    def __init__(self, root):
        self.root = root
        self.root.title("Gourmet Guide")


if __name__ == "__main__":
    root = tk.Tk()
    app = GetRecipe(root)
    root.mainloop()