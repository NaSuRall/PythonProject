import tkinter as tk
from tkinter import messagebox
from Grille import Grille


longueur = 9
largeur = 9


grille = Grille(longueur, largeur)
grille.afficherGrille()


def démarrer_partie_de_demineur(difficulté):
    """
    Fonction appelée lorsque l'utilisateur sélectionne une difficulté.
    """
    if difficulté == "Facile":
        rows, cols, mines = 9, 9, 10
    elif difficulté == "Moyen":
        rows, cols, mines = 16, 16, 40
    elif difficulté == "Difficile":
        rows, cols, mines = 30, 16, 99
    else:
        return

    # Afficher un message de démarrage avec la difficulté
    messagebox.showinfo("Démineur",f"La partie va commencer en mode {difficulté} . Bonne chance !")
    # Ici, tu pourras appeler la fonction pour initialiser et afficher le plateau de jeu.
    # Exemple : `start_game(rows, cols, mines)`


def quitter_application_demineur():
    """ Fonction appelée lorsque l'utilisateur clique sur "Quitter". """
    root.destroy()  # Ferme la fenêtre principale


# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu Démineur")  # Titre de la fenêtre

# Configuration de la taille de la fenêtre
root.geometry("600x500")  # Largeur x Hauteur

# Ajout d'un label (texte d'accueil)
label_titre_principal = tk.Label(root, text="Bienvenue dans le jeu Démineur", font=("Arial", 20), pady=20)
label_titre_principal.pack()  # Place le label dans la fenêtre

# Sous-titre pour choisir la difficulté
label_difficulte = tk.Label(root, text="Choisissez une difficulté :", font=("Arial", 16), pady=10)
label_difficulte.pack()

# Boutons pour choisir la difficulté et démarrer une partie
bouton_facile = tk.Button(root, text="Facile (9x9, 10 mines)", font=("Arial", 14),command=lambda: démarrer_partie_de_demineur("Facile"))
bouton_facile.pack(pady=5)

bouton_moyen = tk.Button(root, text="Moyen (16x16, 40 mines)", font=("Arial", 14),command=lambda: démarrer_partie_de_demineur("Moyen"))
bouton_moyen.pack(pady=5)

bouton_difficile = tk.Button(root, text="Difficile (30x16, 99 mines)", font=("Arial", 14),command=lambda: démarrer_partie_de_demineur("Difficile"))
bouton_difficile.pack(pady=5)

# Bouton pour quitter l'application
bouton_quitter_application = tk.Button(root, text="Quitter l'application", font=("Arial", 14), command=quitter_application_demineur)
bouton_quitter_application.pack(pady=20)

# Boucle principale pour afficher la fenêtre
root.mainloop()
