import turtle as tr
import time as t
delay = 2

# desiner un carree
c = 200 
for i in range(4):
    print(f"forward {c}") 
    tr.forward(c)

    t.sleep(delay)
    print(f"left 90")
    tr.left(90)

    t.sleep(delay)

tr.exitonclick()

# tsy atao itsony action left() @ farany
