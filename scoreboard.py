from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,280)
        self.color("white")
        self.ht()
        self.write(f"Score: {self.score}",False, "center",("Arial",20,"bold"))

    def addScore(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 20, "bold"))

    def gameOver(self):
        gameOverScreen = Turtle()
        gameOverScreen.ht()
        gameOverScreen.color("white")
        gameOverScreen.goto(0,0)
        gameOverScreen.write("Game Over",False, "center",("Arial",20,"normal"))


