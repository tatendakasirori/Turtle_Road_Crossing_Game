from turtle import Turtle 


class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.sety(-160)
        self.shape("turtle")
        self.setheading(90)


    def move(self):
        self.fd(2)
        


       
        