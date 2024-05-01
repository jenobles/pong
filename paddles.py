from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle:
    starting_positions = [(0, 0), (0, -20), (0, -40)]
    
    def __init__(self):
        self.create_paddle()
        self.paddle = []
        self.head = self.paddle[0]
        
    def create_paddle(self):
        for x in starting_positions:
            self.paddle_segment(x)
           
    def move(self):
        for index in range(len(self.paddle)-1, 0, -1):
            new_x = self.paddle[index - 1].xcor()
            new_y = self.paddle[index - 1].ycor()
            self.paddle[index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def paddle_segment(self, x):
        piece = Turtle(shape = 'square')
        piece.setheading(90)
        piece.penup()
        piece.color('white')
        piece.goto(x)
        self.paddle.append(piece)

    def up(self):
        self.head.setheading(90)
        
        
    def down(self):
        self.head.setheading(270)

        


