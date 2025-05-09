from turtle import Screen
from cars import Car
from lines import Lines
from crosser import Crosser
from Level import Level
import time

# create screan object and set up its desired properties 
screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Road Crossing Game")
screen.setup(width = 600, height = 600)
screen.tracer(0)

# show level dispay 
level = Level(0)

# show the two end of the road 
lines = Lines()
lines.create_top_line()
lines.create_bottom_line()
# start of with 30 cars 
cars = []
for _ in range(20):
    car = Car()
    cars.append(car)
# increases num of cars after each level pass
def increase_difficulty(cars):
    screen.tracer(0)
    for _ in range(3):
      cars.append(Car())
    screen.tracer(1)
    print(len(cars))
# resets to 20 cars after level fail
def level_1(cars):
   level.reset_level()
   cars = cars[:20]
   return cars


game_on = True 
screen.listen()
# create the crosser object(turtle)
crosser = Crosser()
screen.tracer(1)
screen.onkeypress(crosser.move,"Up")
# detect collision and send car back to start if true
def check_collison(cars):
   for car in cars:
        if crosser.distance(car) <= 18:
           crosser.back_2_start()
           cars = level_1(cars)
           print(len(cars))
      
while game_on:
    check_collison(cars)
    for car in cars:
       check_collison(cars) 


        #check if car is off the screen
       if car.xcor() <= -280:
           car.hideturtle()
           car.resert_car()
           car.showturtle()
       car.forward(car.move_speed)
       time.sleep(level.sleep_time)    

    # check if crosser has reached the top of the screen
    # if so, increase the level and reset the crosser
       if crosser.ycor() >= 160:
        increase_difficulty(cars)
        level.increase_level()
        crosser.back_2_start()



screen.exitonclick()