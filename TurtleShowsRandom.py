from random import randint, choice
from turtle import Turtle, Screen

randintNumText = Turtle()
randchoiceText = Turtle()
randintNumText.penup()
randchoiceText.penup()
randintNumText.hideturtle()
randchoiceText.hideturtle()
randintNumText.goto(0, 100)
randchoiceText.goto(0, -100)

randintNum = randint(0, 9999)
randChoice = choice(['This', 'is', 'randomized'])

randintNumText.write(str(randintNum), align="center", font=('Arial', 24, 'bold'))
randchoiceText.write(randChoice, align="center", font=('Arial', 24, 'bold'))

screen = Screen()
screen.mainloop()