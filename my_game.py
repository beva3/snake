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


class Segment(_tr.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.speed(0)   # pas d'animatoin
        self.shape("square")    # Forme de chaque segment
        self.color("green")     # Couleur des segments su segment
        self.penup()            # Pas de trace des segments
        self.goto(x,y)          # Placer le segment a une positoin donnee

class Nouriture(_tr.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)           # pas d'animation
        self.shape("circle")    # Forme de la nouriture
        self.color("red")       # Couleur de la nouriture
        self.penup()            # Pas de trace de la nouriture
        self.deplacer()         # Déplacer la nouriture a une nouvelle position aléatoire

    def deplacer(self):
        # placer la nouriture a une position aleatoir dans la fenetre
        self.goto(_rnd.randint(-290, 290), _rnd.randint(-290, 290))

def main():
    jeu = JeuSnake()

if __name__ == "__main__":
    main()