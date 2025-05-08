from turtle import Turtle 

class Lines(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        

    def create_top_line(self):
        self.penup()
        self.sety(160)
        self.setx(-300)
        self.pendown()
        self.fd(600)
    
    def create_bottom_line(self):
        self.penup()
        self.sety(-160)
        self.setx(-300)
        self.pendown()
        self.fd(600)
    
