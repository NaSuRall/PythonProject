import tkinter as tk
from tkinter import messagebox, simpledialog
from Grille import Grille



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
    messagebox.showinfo("Démineur", f"La partie va commencer en mode {difficulté}. Bonne chance !")

    # Générer la grille
    grille = Grille(rows, cols)

    # Effacer l'interface actuelle
    for widget in root.winfo_children():
        widget.destroy()

    # Afficher la grille dans l'interface
    frame_grille = tk.Frame(root)
    frame_grille.pack()

    for i in range(grille.largeur):
        for j in range(grille.longueur):
            bouton = tk.Button(frame_grille, text=" ", width=3, height=1)
            bouton.grid(row=i, column=j)

    # Bouton pour revenir au menu principal
    tk.Button(root, text="Revenir au menu", font=("Arial", 14), command=menu_principal).pack(pady=20)



def quitter_application_demineur():
    root.destroy()


def on_victory():
    """Félicite le joueur et enregistre son nom."""
    nom = simpledialog.askstring("Félicitations !", "Vous avez gagné ! Entrez votre nom :")
    if nom:
        messagebox.showinfo("Victoire !", f"Bravo {nom}, vous avez gagné !")





def menu_principal():

    # Efface les widgets existants
    for widget in root.winfo_children():
        widget.destroy()

    # Ajout label )
    label_titre_principal = tk.Label(root, text="Bienvenue dans le jeu Démineur", font=("Arial", 20), pady=20)
    label_titre_principal.pack()

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
    bouton_quitter_application = tk.Button(root, text="Quitter l'application", font=("Arial", 14),command=quitter_application_demineur)
    bouton_quitter_application.pack(pady=20)


# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu Démineur")
root.geometry("1920x1080")

# Afficher le menu principal
menu_principal()


# Boucle principale pour afficher la fenêtre
root.mainloop()



# on a definie une fenetre qui montrera les scores du demineur
root_2=tk.Tk()

root_2.title("Score")  # Titre de la fenêtre appellé score
root_2.geometry("600x500")  # fenetre taille 600x500

partie_terminer_message=messagebox.showinfo("partie terminer", "félicitation la partie est terminée")
nom_titre= tk.Label(root_2, text="Nom", font=("Arial", 20), pady=10) #Nom du champ appelé nom
nom_titre.pack()
nom_utilisateur=tk.Entry(root_2)#creation d'un champ qu'on assosie a la fenetre du module tk
nom_utilisateur.pack()


root_2.mainloop()