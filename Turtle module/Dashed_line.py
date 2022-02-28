import turtle as t

#Object
timmy = t.Turtle()
#change the shape see documentation , I can put more different thing or type
timmy.shape( "turtle" )
# change the color
timmy.color( "chocolate" )

for i in range(15):
    timmy.forward( 15 )
    timmy.penup()
    timmy.forward( 5 )
    timmy.pendown()
