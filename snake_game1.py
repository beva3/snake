import turtle as tr # tortu
import time as t

delay = 0.1

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
head.direction = "right"

# function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.sety(x - 20)

# Main game loop
while True:
    wn.update()

    move()

    t.sleep(delay)

wn.mainloop()