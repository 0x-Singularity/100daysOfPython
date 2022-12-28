from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()


timmy_the_turtle.color("light blue")

number_of_sides = 3

colors = ["light blue","light steel blue","cornflower blue","royal blue", "blue", "medium blue",
          "navy", "dark blue", "midnight blue","indigo"]

direction = ["right", "left"]

def random_choice(input):
    if input == 0:
        timmy_the_turtle.left(90)
    else:
        timmy_the_turtle.right(90)

def random_walk():
        randomNumber = random.randint(0,1)
        timmy_the_turtle.forward(20)
        random_choice(randomNumber)     


def draw_shape(number_of_sides):
    for i in range(number_of_sides):
        angle = 360 / number_of_sides
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)


for i in range(0,1000):
    timmy_the_turtle.pensize(5)
    random_walk()
    timmy_the_turtle.color(random.choice(colors))
    


 









screen = Screen()
screen.exitonclick()

