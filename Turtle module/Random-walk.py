import turtle as t
import random

colors = ["medium aquamarine", "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat",
          "SlateGray", "SeaGreen"]
degrees = [90, 180, 0, 270]

timmy = t.Turtle()
t.colormode(255) #0 to 255

def random_color():
    r = random.randint(0,255) #red
    g = random.randint(0, 255) #green
    b = random.randint(0, 255) #blue
    random_color = (r, g, b) #tuple
    return random_color


for _ in range(200):
    #direction = [timmy.right, timmy.left]
    #set_direction = random.choice(direction)
    #set_direction(random.choice(degrees))
    timmy.setheading(random.choice(degrees))
    timmy.color(random_color())
    timmy.pensize(5)
    timmy.speed(10)
    timmy.forward(30)

screen = t.Screen()
screen.exitonclick()

