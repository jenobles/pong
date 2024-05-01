from turtle import Turtle, Screen
from paddles import Paddle
import time

t = Turtle()
start_one = Paddle().starting_positions([(-380, 0), (-380, -20), (-380, -40)])
paddle_one = Paddle(start_one)
start_two = Paddle().starting_positions([(380, 0), (380, -20), (380, -40)])
paddle_two = Paddle(start_two)

game_is_on = True

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

t.goto(0, 300)
t.setheading(270)
for _ in range(50):
    t.forward(10)
    t.color('white')
    t.forward(10)
    t.color('black')

screen.listen()
screen.onkey(paddle_one.up, 'w')
screen.onkey(paddle_one.down, 's')

screen.onkey(paddle_two.up, 'Up')
screen.onkey(paddle_two.down, 'Down')


while game_is_on:
    screen.update()
    time.sleep(0.1)

    paddle_one.move()
    paddle_two.move()



screen.exitonclick()
