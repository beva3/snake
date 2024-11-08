import turtle
import time
import random

# Configuration de la fenêtre de jeu
class JeuSnake:
    def __init__(self):
        # Créer la fenêtre
        self.window = turtle.Screen()
        self.window.title("Jeu Snake")
        self.window.bgcolor("black")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)

        # Attributs du serpent
        self.serpent = []
        self.taille_serpent = 1
        self.serpent_vitesse = 0.1

        # Initialisation des objets
        self.creer_serpent()
        self.nourriture = Nourriture()

        # Écoute des commandes utilisateur
        self.window.listen()
        self.window.onkey(self.monter, "Up")
        self.window.onkey(self.descendre, "Down")
        self.window.onkey(self.aller_gauche, "Left")
        self.window.onkey(self.aller_droite, "Right")

        # Lancer le jeu
        self.jouer()

    def creer_serpent(self):
        """Crée le serpent initial avec un seul segment."""
        for i in range(self.taille_serpent):
            segment = Segment(-20 * i, 0)
            self.serpent.append(segment)

    def deplacer_serpent(self):
        """Déplace le serpent."""
        for i in range(len(self.serpent) - 1, 0, -1):
            x = self.serpent[i - 1].xcor()
            y = self.serpent[i - 1].ycor()
            self.serpent[i].goto(x, y)
        if len(self.serpent) > 0:
            self.serpent[0].avance()

    def ajouter_segment(self):
        """Ajoute un segment au serpent lorsqu'il mange de la nourriture."""
        segment = Segment(self.serpent[-1].xcor(), self.serpent[-1].ycor())
        self.serpent.append(segment)

    def manger_nourriture(self):
        """Vérifie si le serpent mange la nourriture."""
        if self.serpent[0].distance(self.nourriture) < 20:
            self.nourriture.deplacer()
            self.ajouter_segment()
            self.taille_serpent += 1

    def monter(self):
        """Change la direction du serpent vers le haut."""
        self.serpent[0].setheading(90)

    def descendre(self):
        """Change la direction du serpent vers le bas."""
        self.serpent[0].setheading(270)

    def aller_gauche(self):
        """Change la direction du serpent vers la gauche."""
        self.serpent[0].setheading(180)

    def aller_droite(self):
        """Change la direction du serpent vers la droite."""
        self.serpent[0].setheading(0)

    def jouer(self):
        """Boucle principale du jeu."""
        while True:
            self.window.update()  # Mettre à jour la fenêtre
            self.deplacer_serpent()  # Déplacer le serpent
            self.manger_nourriture()  # Vérifier si le serpent mange de la nourriture

            # Vérification des collisions avec les murs
            if self.serpent[0].xcor() > 290 or self.serpent[0].xcor() < -290 or self.serpent[0].ycor() > 290 or self.serpent[0].ycor() < -290:
                print("Game Over!")
                break

            # Vérification des collisions avec le corps du serpent
            for segment in self.serpent[1:]:
                if self.serpent[0].distance(segment) < 20:
                    print("Game Over!")
                    break

            time.sleep(self.serpent_vitesse)  # Contrôler la vitesse du serpent

        self.window.bye()  # Fermer la fenêtre

class Segment(turtle.Turtle):
    def __init__(self, x, y):
        """Initialisation d'un segment du serpent."""
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(x, y)

    def avance(self):
        """Déplace le segment en avant."""
        self.forward(20)

class Nourriture(turtle.Turtle):
    def __init__(self):
        """Initialisation de la nourriture."""
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.deplacer()

    def deplacer(self):
        """Déplace la nourriture à une nouvelle position aléatoire."""
        self.goto(random.randint(-290, 290), random.randint(-290, 290))

# Lancer le jeu
if __name__ == "__main__":
    JeuSnake()
