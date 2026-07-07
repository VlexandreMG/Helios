import tkinter as tk
from tkinter import ttk
from src.ui.components.form import Form

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Helios")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f7")
        
        # C'est ici qu'on viendra greffer nos futurs composants (formulaire, tableau)
        self.Formulaire = Form(self.root)