import random
import turtle as t

tim = t.Turtle()
t.colormode(255)

t.bgcolor("black")
t.pensize(2)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

t.speed("fastest")
#detect when stop drawing
def draw_spirograph(size_of_gap):
    for _ in range (int(360 / size_of_gap)): #360 degrees full circle / different offset
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)



screen = t.Screen()
screen.exitonclick()