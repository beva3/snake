import turtle as tr
import time as tm

delay = 3

# Créer une fenêtre
fenetre = tr.Screen()

# Créer une tortue
tortue = tr.Turtle()

# Dessiner un carré
for _ in range(4):
    print(f"wait {delay}")
    tm.sleep(delay)
    print("forward 100 px")
    tortue.forward(100) # avancee de 100 px    
    print("turn to right ")
    tortue.right(90)    #tourner droit de 90 deg

fenetre.exitonclick()


"""
Turtle : 
    #   outil de programmation
        simple et amusant
        tortue vistuelle 

        tu peux lui donner des ordre pour qu'elle se deplace

        leve son stylo
        baisse son stylo
    
    #   a quoi ca sert
        dessiner
            forme geometique
            dessin plus complex
            animation simple

        pour apprendre la programmation
            comprendre la concepte 
                de boucle
                condition
                fontion
                ...
        
        visualiser le code
    
    #   comment ca marche

        basique :
            forward(x)  : avancer de x pixel
            right(x)    : tourner de x deg
            penup()     : leve son stylo (elle ne designe pas)
                pen Up
            pendown()   : baisse son stylo (elle desine)

                


"""