import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Helios")
        self.root.geometry("800x600")
        self.root.configure(bg="#f5f5f7")
        
        # C'est ici qu'on viendra greffer nos futurs composants (formulaire, tableau)
        self.creer_widgets()

    def creer_widgets(self):
        # Un titre temporaire pour tester
        titre = tk.Label(
            self.root, 
            text="HELIOS - Fenêtre Principale", 
            font=("Helvetica", 14, "bold"),
            bg="#f5f5f7"
        )
        titre.pack(pady=20)