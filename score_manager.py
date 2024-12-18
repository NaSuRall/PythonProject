import json
import os
import tkinter as tk

SCORE_FILE = "scores.json"

def save_score(name, difficulty, time_taken):
    """Enregistre le score d'un joueur dans un fichier JSON."""
    score_data = {
        "nom": name,
        "difficulté": difficulty,
        "temps": time_taken
    }
    # Lecture des scores existants
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as file:
            scores = json.load(file)
    else:
        scores = []

    # Ajout du nouveau score
    scores.append(score_data)

    # Écriture dans le fichier
    with open(SCORE_FILE, "w") as file:
        json.dump(scores, file, indent=4)
    print(f"Score enregistré : {name} - {difficulty} - {time_taken} secondes")

def display_scores_tkinter():
    """Affiche les scores dans une fenêtre tkinter."""
    # Lecture des scores
    if not os.path.exists(SCORE_FILE):
        scores = []
    else:
        with open(SCORE_FILE, "r") as file:
            scores = json.load(file)

    # Création de la fenêtre tkinter
    scores_window = tk.Toplevel()
    scores_window.title("Tableau des Scores")
    scores_window.geometry("400x300")
    scores_window.configure(bg="#2c3e50")

    # Titre
    title = tk.Label(scores_window, text="Tableau des Scores",
                     font=("Helvetica", 14, "bold"), bg="#2c3e50", fg="white")
    title.pack(pady=10)

    # Contenu des scores
    if not scores:
        no_scores_label = tk.Label(scores_window, text="Aucun score enregistré.",
                                   font=("Helvetica", 12), bg="#2c3e50", fg="white")
        no_scores_label.pack()
    else:
        for idx, score in enumerate(scores, start=1):
            score_text = f"{idx}. {score['nom']} - {score['difficulté']} - {score['temps']}s"
            score_label = tk.Label(scores_window, text=score_text,
                                   font=("Helvetica", 10), bg="#34495e", fg="white")
            score_label.pack(pady=2)


# Exemple d'utilisation avec tkinter
def main_menu():
    """Menu principal avec tkinter."""
    root = tk.Tk()
    root.title("Démineur")
    root.geometry("300x200")
    root.configure(bg="#2c3e50")

    # Boutons
    tk.Button(root, text="Voir les Scores", command=display_scores_tkinter,
              width=20, bg="#2980b9", fg="white").pack(pady=20)
    tk.Button(root, text="Quitter", command=root.quit,
              width=20, bg="#c0392b", fg="white").pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_menu()



