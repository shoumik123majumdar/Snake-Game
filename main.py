from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width= 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

#Deals with snake movement
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down ")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if(snake.head.distance(food) <15):
        food.refresh()
        snake.addSnake()
        scoreboard.addScore()
    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor()<-300 or snake.head.ycor() <-300:
        scoreboard.gameOver()
        gameIsOn = False
    for snape in snake.snakes[1:]:
        if snake.head.distance(snape)<10:
            scoreboard.gameOver()
            gameIsOn = False


screen.exitonclick()