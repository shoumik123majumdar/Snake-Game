from turtle import Turtle

snakes = []
moveDistance = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.snakes = []
        self.createSnake(3)
        self.head = self.snakes[0]

    def createSnake(self, numSquares):
        global snakes,screen
        for int in range(numSquares):
            timmy = Turtle()
            timmy.penup()
            timmy.shape("square")
            timmy.color("white")
            timmy.setpos(0 - (int * 20), 0)
            self.snakes.append(timmy)


    def move(self):
        for int in range(len(self.snakes)-1,0,-1):
            snake = self.snakes[int]
            futureSnake = self.snakes[int-1]
            snake.setpos(futureSnake.xcor(),futureSnake.ycor())
        self.snakes[0].forward(moveDistance)

    def addSnake(self):
        timothy = Turtle()
        timothy.penup()
        timothy.shape("square")
        timothy.color("white")
        endSnake = self.snakes[len(self.snakes) - 1]
        timothy.setpos(endSnake.xcor() - 20, endSnake.ycor())
        self.snakes.append(timothy)

    def getHeadPos(self):
        return self.snakes[0].pos()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
