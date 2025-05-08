from turtle import Screen
from cars import Car
from lines import Lines
from crosser import Crosser
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width = 600, height = 600)
screen.tracer(0)

lines = Lines()
lines.create_top_line()
lines.create_bottom_line()
crosser = Crosser()
cars = []
for car in range(20):
    car = Car()
    cars.append(car)



game_on = True 
screen.tracer(1)
screen.listen()
screen.onkeypress(crosser.move,"Up")
init_time = 0.005

while game_on:
        time.sleep(init_time)
     for car in cars:
       if car.xcor() <= -280:
           car.hideturtle()
           car.resert_car()
           car.showturtle()
       car.setx(car.xcor() - 5)

 












screen.exitonclick()