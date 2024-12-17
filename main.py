# importer le module tkinter
import tkinter as tk
from tkinter.constants import ANCHOR, CENTER

# définir une fenêtre
game = tk.Tk()

# définir ses caractéristiques
game.title("Demineur")
game.geometry("600x600")

def exit():
    game.destroy()

lbl = tk.Label(game, text="Demineur", fg="white", bg="black")
lbl.pack()

btn = tk.Button(game, text="Close Game", command=exit)
btn.grid(column=1, row=0)

#ouvrir la fenêtre
game.mainloop()