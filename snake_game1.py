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
def go_up():
    head.direction == "up"

def go_down():
    head.direction == "down"

def go_right():
    head.direction == "right"

def go_left():
    head.direction == "left"



head = tr.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.goto(0,0)
head.direction = "stop"

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

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")

# Main game loop
while True:
    wn.update()

    move()

    t.sleep(delay)

wn.mainloop()