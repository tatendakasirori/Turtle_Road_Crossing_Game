from turtle import Turtle

class Level(Turtle):
    def __init__(self, level):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,200)
        self.level = level
        self.write(f"Level: {self.level}", align = "center", font = ("Times New Roman", 20, "normal"))

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align = "center", font = ("Times New Roman", 20, "normal"))