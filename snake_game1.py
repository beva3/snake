# import turtle
# import random
# import time

# class Segment(turtle.Turtle):
#     def __init__(self, x, y):
#         super().__init__()
#         self.speed(0)
#         self.shape("square")
#         self.color("green")
#         self.penup()
#         self.goto(x, y)

# class Nourriture(turtle.Turtle):
#     def __init__(self):
#         super().__init__()
#         self.speed(0)
#         self.shape("circle")
#         self.color("red")
#         self.penup()
#         self.deplacer()

#     def deplacer(self):
#         """Position aléatoire sur la fenêtre."""
#         self.goto(random.randint(-290, 290), random.randint(-290, 290))

# class Serpent:
#     def __init__(self):
#         self.serpent = []
#         self.taille_serpent = 1
#         self.creer_serpent()

#     def creer_serpent(self):
#         for i in range(self.taille_serpent):
#             segment = Segment(-20 * i, 0)
#             self.serpent.append(segment)

#     def deplacer(self):
#         """Déplace chaque segment."""
#         for i in range(len(self.serpent) - 1, 0, -1):
#             x = self.serpent[i - 1].xcor()
#             y = self.serpent[i - 1].ycor()
#             self.serpent[i].goto(x, y)
#         self.serpent[0].forward(20)
    
#     def ajouter_segment(self):
#         """Ajoute un segment après avoir mangé."""
#         segment = Segment(self.serpent[-1].xcor(), self.serpent[-1].ycor())
#         self.serpent.append(segment)

# class JeuSnake:
#     def __init__(self):
#         self.window = turtle.Screen()
#         self.window.title("Jeu Snake")
#         self.window.bgcolor("black")
#         self.window.setup(width=600, height=600)
#         self.window.tracer(0)

#         self.serpent = Serpent()
#         self.nourriture = Nourriture()

#         self.window.listen()
#         self.window.onkey(self.monter, "Up")
#         self.window.onkey(self.descendre, "Down")
#         self.window.onkey(self.aller_gauche, "Left")
#         self.window.onkey(self.aller_droite, "Right")

#     def jouer(self):
#         """Boucle principale pour faire fonctionner le jeu."""
#         while True:
#             self.window.update()
#             self.serpent.deplacer()
#             self.verifier_collisions()
#             time.sleep(0.1)

#     def verifier_collisions(self):
#         if self.serpent.serpent[0].distance(self.nourriture) < 20:
#             self.nourriture.deplacer()
#             self.serpent.ajouter_segment()

#     def monter(self):
#         self.serpent.serpent[0].setheading(90)

#     def descendre(self):
#         self.serpent.serpent[0].setheading(270)

#     def aller_gauche(self):
#         self.serpent.serpent[0].setheading(180)

#     def aller_droite(self):
#         self.serpent.serpent[0].setheading(0)

# def main():
#     jeu = JeuSnake()
#     jeu.jouer()

# if __name__ == "__main__":
#     main()

import turtle
import time
import random

# Classe Segment
class Segment(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(x, y)

# Classe Nourriture
class Nourriture(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.deplacer()

    def deplacer(self):
        self.goto(random.randint(-290, 290), random.randint(-290, 290))

# Classe Serpent
class Serpent:
    def __init__(self):
        self.serpent = []
        self.taille_serpent = 1
        self.creer_serpent()
        self.game_over = False  # Flag pour stopper le jeu en cas de collision

    def creer_serpent(self):
        for i in range(self.taille_serpent):
            segment = Segment(-20 * i, 0)
            self.serpent.append(segment)

    def deplacer(self):
        """Déplace le serpent. Si le jeu est terminé, il ne bouge plus."""
        if self.game_over:
            return  # Ne rien faire si Game Over

        # Déplacer les segments du corps
        for i in range(len(self.serpent) - 1, 0, -1):
            x = self.serpent[i - 1].xcor()
            y = self.serpent[i - 1].ycor()
            self.serpent[i].goto(x, y)
        
        # Déplacer la tête du serpent
        self.serpent[0].forward(20)

    def ajouter_segment(self):
        segment = Segment(self.serpent[-1].xcor(), self.serpent[-1].ycor())
        self.serpent.append(segment)

    def collision_murs(self):
        """Vérifie si la tête du serpent entre en collision avec les bords."""
        x = self.serpent[0].xcor()
        y = self.serpent[0].ycor()
        if x > 290 or x < -290 or y > 290 or y < -290:
            self.game_over = True  # Active le flag Game Over
            return True
        return False

    def afficher_game_over(self, window):
        """Affiche le message Game Over à l'écran."""
        texte = turtle.Turtle()
        texte.hideturtle()
        texte.color("white")
        texte.penup()
        texte.goto(0, 0)
        texte.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
        window.update()

# Classe principale JeuSnake
class JeuSnake:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Jeu Snake")
        self.window.bgcolor("black")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)

        self.serpent = Serpent()
        self.nourriture = Nourriture()

        self.window.listen()
        self.window.onkey(self.monter, "Up")
        self.window.onkey(self.descendre, "Down")
        self.window.onkey(self.aller_gauche, "Left")
        self.window.onkey(self.aller_droite, "Right")

    def jouer(self):
        """Boucle principale du jeu."""
        try:
            while not self.serpent.game_over:
                self.window.update()
                self.serpent.deplacer()

                # Vérification de collision avec les murs
                if self.serpent.collision_murs():
                    self.serpent.afficher_game_over(self.window)
                    break

                # Vérifier si le serpent mange la nourriture
                if self.serpent.serpent[0].distance(self.nourriture) < 20:
                    self.nourriture.deplacer()
                    self.serpent.ajouter_segment()

                time.sleep(0.1)

            # Laisser la fenêtre ouverte après Game Over
            self.window.update()
            self.window.mainloop()  # Permet à l'utilisateur de fermer proprement

        except turtle.Terminator:
            print("Le jeu a été fermé.")

    def monter(self):
        if self.serpent.serpent[0].heading() != 270:  # Eviter de faire demi-tour sur soi-même
            self.serpent.serpent[0].setheading(90)

    def descendre(self):
        if self.serpent.serpent[0].heading() != 90:
            self.serpent.serpent[0].setheading(270)

    def aller_gauche(self):
        if self.serpent.serpent[0].heading() != 0:
            self.serpent.serpent[0].setheading(180)

    def aller_droite(self):
        if self.serpent.serpent[0].heading() != 180:
            self.serpent.serpent[0].setheading(0)

# Fonction main
def main():
    jeu = JeuSnake()
    jeu.jouer()

if __name__ == "__main__":
    main()
