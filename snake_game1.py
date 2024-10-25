import turtle as tr # tortu

#setup the screen
wn = tr.Screen()
wn.title("Snake game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #desactiver la mise a jour automatique de l'ecran

#Snake head
head = tr.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.goto(0,0)
head.direction = "stop"

# Main game loop
while True:
    wn.update()

wn.mainloop()