import turtle as tr

# methode to draw patern of circle with rad radius
def draw(rad):
    # draw circle
    tr.circle(rad)

    tr.up()
    tr.setpos(0,-rad)
    tr.down()

# loop for patern
for i in range(5):
    draw(20 + 20*i)

# exit on click
tr.exitonclick()