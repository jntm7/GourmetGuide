import tkinter as tk

def create_menu(root, save_recipes_command):
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    
    file_menu.add_command(label="Save", command=save_recipes_command)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)