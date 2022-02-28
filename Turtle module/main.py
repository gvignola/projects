from turtle  import Turtle, Screen
#import turtle as t

#timmy_the_turtle = t.Turtle()
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("red")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.backward(200)
#timmy_the_turtle.right(90)
#timmy_the_turtle.left(180)
#timmy_the_turtle.setheading(0)

#Object
timmy = Turtle()
#change the shape see documentation , I can put more different thing or type
timmy.shape( "turtle" )
# change the color
timmy.color( "chocolate" )


## move forward(100) of paces or backward
#timmy.forward( 100 )
##Turn right 90 degrees
#timmy.right( 90 )


# draw a square

for square in range(4):
    timmy.forward( 100 )
    timmy.right(90)


'''import heroes
print(heroes.gen())'''











#stay the screen and exit when we clik (we want)
screen = Screen()
screen.exitonclick()