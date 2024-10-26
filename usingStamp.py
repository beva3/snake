import turtle as tr
import time as t

# delay
delay = 3

# forward the turtle by 100
tr.forward(100)

# stamp the turtle shape
tr.stamp()  # turtlr : head of pen

# set the position by using setpos()
tr.up()             # pen UP
tr.setpos(-50,50)
tr.down()           # pen DOWN

# forward turtle by 100
t.sleep(delay)
tr.forward(100)

# exit on click
tr.exitonclick()
