import random


class Grille:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.tab = self.generationGrille()

    def generationGrille(self):
        # Créer un tableau vide de dimensions 'largeur' x 'longueur' avec des zéros et des bordures
        tab = []
        for i in range(self.largeur):
            ligne = []
            for j in range(self.longueur):
                if i == 0 or i == self.largeur - 1 or j == 0 or j == self.longueur - 1:
                    ligne.append("/")  # Bordure
                else:
                    ligne.append(0)  # Intérieur de la grille
            tab.append(ligne)

        # Placer des "1" à l'intérieur de la grille de manière aléatoire
        placements = self.getPlacements()
        while placements > 0:
            i = random.randint(1, self.largeur - 2)  # Pas sur les bords
            j = random.randint(1, self.longueur - 2)  # Pas sur les bords

            if tab[i][j] == 0:
                tab[i][j] = "x"
                placements -= 1
        return tab

    def getPlacements(self):
        if self.largeur == 9 :
            return 10
        elif self.largeur == 16:
            return 40
        elif self.largeur == 30 and self.longueur == 16:
            return 99
        return 0

    def afficherGrille(self):
        for ligne in self.tab:
            print(" ".join(str(cell) for cell in ligne))

    def incrementerAutour(self, x, y):
        # Incrémenter les cases autour de la position (x, y)
        # Vérifier les cases autour de la position (en haut, en bas, gauche, droite, diagonales)
        for i in range(x - 1, x + 2):  # Parcours des lignes autour de la case (x)
            for j in range(y - 1, y + 2):  # Parcours des colonnes autour de la case (y)
                if 0 <= i < self.largeur and 0 <= j < self.longueur:  # Vérifier si la case est dans les limites
                    if self.tab[i][j] != "X":  # On ne veut pas incrémenter la case contenant déjà un X
                        self.tab[i][j] += 1
