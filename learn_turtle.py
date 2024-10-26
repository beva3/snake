import turtle as tr

# show the siz of screen
def print_sizeScreen(wn):
    w = wn.window_width()
    h = wn.window_height()
    print(f"{wn}\n\
          w = {w}\n\
          h = {h}")
    
#configurer la fenetre Turtle
window = tr.Screen()

# run 
print_sizeScreen(window)

tr.exitonclick()