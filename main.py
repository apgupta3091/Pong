from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#SET UP THE SCREEN
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

#INITALIZE THE CLASS INSTANCES
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

#GET SCREEN TO LISTEN TO KEY PRESSES 
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#START OF GAME
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #DETECT COLLISION W WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #DETECT COLLISION W PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bouce_x()
        
    #DETECT BALL OUT OF BOUNDS RIGHT
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    #DETECT BALL OUT OF BOUNDS LEFT
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

#END OF GAME
screen.exitonclick()