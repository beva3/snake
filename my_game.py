import turtle as _tr
import random as _rnd
import time as _t

#Configuration de la Fenêtre de Jeu
class JeuSnake:
    def __init__(self):
        self.window = _tr.Screen()
        self.window.title("Jeu Snake")
        self.window.bgcolor("black")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)
        self.serpent = Serpent()
        self.nourriture = Nouriture()
        self.window.listen()
        # Associe les touches du clavier au mouvement
        self.window.onkey(self.monter, "Up")
        self.window.onkey(self.descendre, "Down")
        self.window.onkey(self.aller_gauche, "Left")
        self.window.onkey(self.aller_droite, "Right")

    def jouer(self):
        while not self.serpent.game_over:
            self.window.update()
            self.serpent.deplacer_serpent()
            if self.serpent.collision_murs():
                self.serpent.afficher_game_over(self.window)
                break
            if self.serpent.serpent[0].distance(self.nourriture) < 20:
                self.nourriture.deplacer()
                self.serpent.ajouter_segment()
            _t.sleep(0.1)

        self.window.update()
        self.window.mainloop()

    def monter(self):
        if self.serpent.serpent[0].heading() != 270:
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

class Serpent:
    def __init__(self):
        self.serpent = []           # Liste de seg du serpent
        self.taille_serpent = 1     # taille du serpent
        self.game_over = 0          # Game over
        self.creer_serpent()
    def creer_serpent(self):
        # Ajout un segment de depart
        for i in range(self.taille_serpent):
            segment = Segment(-20 * i, 0)
            self.serpent.append(segment)
    
    def deplacer_serpent(self):
        # Deplacent de segment du corps
        if self.game_over:
            return  # Arreter le mvt si game over
        for i in range(len(self.serpent) -1 , 0, -1):
            x = self.serpent[i -1].xcor()
            y = self.serpent[i -1].ycor()
            self.serpent[i].goto(x, y)
        self.serpent[0].forward(20)
    
    def ajouter_segment(self):
        # Ajout un segment a la fin du serprnt
        segment = Segment(self.serpent[-1].xcor(), self.serpent[-1].ycor())
        self.serpent.append(segment)
    
    def collision_murs(self):
        # Vérifie si le serpent touche un mur
        X = self.serpent[0].xcor()
        Y = self.serpent[0].ycor()
        if X > 290 or X < -290 or Y > 290 or Y < -290:
            self.game_over = True  # Game Over
            return True
        return False
    
    def afficher_game_over(self, window):
        # Affiche le message Game Over à l'écran
        texte = _tr.Turtle()
        texte.hideturtle()
        texte.color("white")
        texte.penup()
        texte.goto(0, 0)
        texte.write("Game Over!", align="center", font=("Courier", 24, "normal"))
        window.update()

def main():
    jeu = JeuSnake()  # Crée le jeu
    jeu.jouer()  # Lance la boucle de jeu

if __name__ == "__main__":
    main()
