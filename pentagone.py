import turtle as tr

# desine pentagon
c = 100
for i in range(5):
    tr.forward(c)
    if i!=4:
        tr.left(72)
    else: pass

tr.exitonclick()
