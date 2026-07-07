import tkinter as tk 
from tkinter import ttk

class Form:
    def __init__(self,parent):
        self.parent = parent

        self.cadre = tk.LabelFrame(self.parent, text=" Nouvel Appareil ", padx=10, pady=10)
        self.cadre.pack(fill="x", padx=15, pady=10)

        self.creer_form()

    def creer_form(self):
        nomApp = tk.Label(self.cadre, text="Nom de l'appareil")
        nomApp.pack(side="left", padx=5)
