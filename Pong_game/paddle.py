from turtle import Turtle

class Paddle(Turtle):  # Inherit from Turtle directly
    def __init__(self, position):
        super().__init__()  # Corrected: call super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)  # Use the position passed to the constructor

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20  # Fixed: was incorrectly using xcor()
        self.goto(self.xcor(), new_y)
