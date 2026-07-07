import tkinter as tk 
from tkinter import ttk

class Form:
    def __init__(self,parent):
        self.parent = parent

        self.cadre = tk.LabelFrame(self.parent, text=" Nouvel Appareil ", padx=10, pady=10)
        self.cadre.pack(padx=15, pady=10)

        self.creer_form()

    def creer_form(self):
        nomApp = tk.Label(self.cadre, text="Nom de l'appareil")
        nomApp.pack(side="left", padx=5)

        self.entry_nom = tk.Entry(self.cadre, width=20)
        self.entry_nom.pack(side="left", padx=5)

        puissance = tk.Label(self.cadre, text="Puissance")
        puissance.pack(side="left", padx=5)

        self.entry_puissance = tk.Entry(self.cadre, width=20)
        self.entry_puissance.pack(side="left", padx=5)

        tranche = tk.Label(self.cadre, text="Tranche")
        tranche.pack(side="left", padx=5)

        self.combo_tranche = ttk.Combobox(self.cadre, values=["T1", "T2", "T3"], state="readonly", width=8)
        self.combo_tranche.current(0) 
        self.combo_tranche.pack(side="left", padx=5, pady=(20, 0))

        heureDebut = tk.Label(self.cadre, text="Heure debut")
        heureDebut.pack(side="left", padx=5)

        self.entry_hdebut = tk.Entry(self.cadre, width=20)
        self.entry_hdebut.pack(side="left", padx=5)

        heureFin = tk.Label(self.cadre, text="Heure fin")
        heureFin.pack(side="left", padx=5)

        self.entry_hfin = tk.Entry(self.cadre, width=20)
        self.entry_hfin.pack(side="left", padx=5)