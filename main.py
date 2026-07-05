import tkinter as tk
from src.ui.main_window import MainWindow

def main():
    # 1. Création de la fenêtre de base Tkinter
    root = tk.Tk()
    
    # 2. Initialisation de ton interface modulaire
    app = MainWindow(root)
    
    # 3. Lancement de l'application
    root.mainloop()

if __name__ == "__main__":
    main()