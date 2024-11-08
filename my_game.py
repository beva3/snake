import turtle as _tr
import random as _rnd
import time as _t

#Configuration de la Fenêtre de Jeu
class JeuSnake:
    def __init__(self):
        self.win = _tr.Screen() # Crée une fenêtre pour le jeu
        self.win.title("Jeu Snake") # Définit le titre de la fenêtre
        self.win.bgcolor("black")   #  Couleur de fond du fenetre
        self.win.setup(width=600, height=600)   # size fenetre
        self.win.tracer(0)  # Desactive le tracer pour le rendu instantané
        self.win.listen()   # Active lecoute des events


def main():
    jeu = JeuSnake()

if __name__ == "__main__":
    main()