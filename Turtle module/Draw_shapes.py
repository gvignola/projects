import turtle as t
import random

timmy = t.Turtle()

colors = ["medium aquamarine", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]



# draw a square
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

for shape_side_n in range(3,11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)


 # '''for triangle in range(3):
 #    timmy.forward(100)
 #    timmy.right(120)
 #for square in range(4):
 #    timmy.forward( 100 )
 #    timmy.right(90)
 #for pentagon in range(5):
 #    timmy.forward(100)
 #    timmy.right(72)
 #for hexagon in range(6):
 #    timmy.forward(100)
 #    timmy.right(60)
 #for heptagon in range(7):
 #    timmy.forward(100)
 #    timmy.right(51)
 #for octagon in range(8):
 #    timmy.forward(100)
 #    timmy.right(45)
 #for nonago in range(9):
 #    timmy.forward(100)
 #    timmy.right(40)
 #for decagon in range(10):
 #    timmy.forward(100)
 #    timmy.right(36)'''