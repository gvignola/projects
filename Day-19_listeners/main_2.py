import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
#similarly
user_bet = screen.textinput(title= "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle( shape="turtle" )
    new_turtle.color( colors[turtle_index ] )
    new_turtle.penup()
    #start of the line at very left edge of my screen
    new_turtle.goto( x=-230, y= y_positions[turtle_index ] )
    all_turtle.append(new_turtle)#multiple turtle

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            #the end is 250 , turtle's width is 40 --> 40/2 (250-30)
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        # (0,10) #random movement from 0 to 10
        random_distance = random.randint(0, 10) #random int is inclusive
        turtle.forward(random_distance)




screen.exitonclick()