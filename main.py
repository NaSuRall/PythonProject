# importer le module tkinter
import tkinter as tk
from tkinter import StringVar, OptionMenu

# définir une fenêtre
game = tk.Tk()

# définir ses caractéristiques
game.title("Demineur")
game.geometry("600x600")

# définir une fonction qui ferme la fenêtre
def exit():
    game.destroy()

# définir une fonction qui affiche une liste déroulante
def click():
    options = [
        "Facile 9 x 9",
        "Moyen 16 x 16",
        "Difficile 30 x 16"
    ]
    clicked = StringVar()
    clicked.set("Choisir la Difficulté")
    drop = OptionMenu(game, clicked ,*options)
    drop.pack()

# définir des boutons avec des actions
stop = tk.Button(game, text="Arrêter le Jeu", command=exit)
stop.grid(column=1, row=0)
play = tk.Button(game, text="Jouer", command=click)
play.grid(column=1, row=1)

#ouvrir la fenêtre
game.mainloop()