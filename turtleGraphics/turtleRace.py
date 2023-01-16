from turtle import Turtle, Screen
import random

turtleOne = Turtle(shape="turtle", visible = False)
turtleOne.penup()
turtleOne.color("Red")
turtleTwo = Turtle(shape="turtle", visible = False)
turtleTwo.penup()
turtleTwo.color("Orange")
turtleThree = Turtle(shape="turtle", visible = False)
turtleThree.penup()
turtleThree.color("Yellow")
turtleFour = Turtle(shape="turtle", visible = False)
turtleFour.penup()
turtleFour.color("Green")
turtleFive = Turtle(shape="turtle", visible = False)
turtleFive.penup()
turtleFive.color("Blue")
screen = Screen()

screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title="Make your bet", prompt= "Which turtle will win the race? Enter a color:")

turtleOne.goto(x=-230, y = 0)
turtleTwo.goto(x=-230, y = 80)
turtleThree.goto(x=-230, y = 160)
turtleFour.goto(x=-230, y = -80)
turtleFive.goto(x=-230, y = -160)

turtleOne.showturtle()
turtleTwo.showturtle()
turtleThree.showturtle()
turtleFour.showturtle()
turtleFive.showturtle()

def move_forward():
    spaceForward = random.randint(0,10)
    return spaceForward

for i in range(0,100):
    turtleOne.forward(move_forward())
    turtleTwo.forward(move_forward())
    turtleThree.forward(move_forward())
    turtleFour.forward(move_forward())
    turtleFive.forward(move_forward())




screen.exitonclick()