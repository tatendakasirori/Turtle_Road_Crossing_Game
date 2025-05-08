import turtle as t
import random as r
t.colormode(hex)
hex_colors = [
    "#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#8E44AD",
    "#2ECC71", "#E74C3C", "#3498DB", "#1ABC9C", "#9B59B6",
    "#34495E", "#16A085", "#27AE60", "#2980B9", "#D35400",
    "#C0392B", "#BDC3C7", "#7F8C8D", "#F39C12", "#E67E22"
]


class Car(t.Turtle):
    def __init__(self,colors = hex_colors):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.2, stretch_len=0.9)
        self.setx(r.randint(-280,280))
        self.sety(r.randint(-150,150))
        self.color(r.choice(hex_colors))
        

    def resert_car(self):
        self.setx(280)
        self.sety(r.randint(-150,150))
