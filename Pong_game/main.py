from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
from PIL import Image
from turtle import Screen

# Convert PNG to GIF
img = Image.open("bck.png")
img.save("bck.gif", format="GIF")

# Set up the screen with background image
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgpic("bck.gif")  # <- include the full filename with .gif
screen.tracer(0)


r_paddle = Paddle((350, 0))   # Right paddle on the right
l_paddle = Paddle((-350, 0)) # Left paddle on the left
ball = Ball()
score = Score()

# Controls
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_pos()
        score.l_point()


    if ball.xcor()<-380:
        ball.reset_pos()
        score.r_point()


