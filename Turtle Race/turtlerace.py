import time
import turtle
import random

WIDTH = 1000
HEIGHT = 1000
COLORS = ['red', 'blue', 'brown', 'green', 'yellow', 'pink', 'orange', 'purple', 'cyan', 'gold']

def amount_of_turtles():
    while True:
        racers = int(input("Enter how many turtles you want to race (2 - 10): "))
        if 2 <= racers <= 10:
            return racers
        else:
            print("Your choice has to be between 2 - 10!!!")
            time.sleep(2)
            print("Try again......\n")
            time.sleep(2)

def create_new_turtles(colors):
    turtles = []
    spaceY = HEIGHT / (len(colors) + 1)
    for x, color in enumerate(colors):
        racer = turtle.Turtle() 
        racer.color(color)
        racer.shape('turtle')
        racer.penup()
        racer.setpos(-WIDTH // 2 + 30, -HEIGHT // 2 + (x + 1) * spaceY)
        racer.speed(3)
        turtles.append(racer)
        time.sleep(0.5)
    return turtles

def race(turtles):
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if x >= (WIDTH / 2) - 30: 
                return turtles.index(racer)
            
def draw_line(x_position, line_color="black"):
    line_turtle = turtle.Turtle()
    line_turtle.hideturtle()
    line_turtle.color(line_color)
    line_turtle.pensize(20)
    line_turtle.penup()
    line_turtle.goto(x_position, -HEIGHT // 2) 
    line_turtle.pendown() 
    line_turtle.goto(x_position, HEIGHT // 2)
    line_turtle.penup()


racers = amount_of_turtles()


screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)
screen.title("Mohammed's Racers")
draw_line(-WIDTH // 2 + 30, line_color="white")
draw_line(WIDTH // 2 - 30, line_color="#ff000d")

random.shuffle(COLORS)
colors = COLORS[:racers]
turtles = create_new_turtles(colors)
t = turtle.Turtle()
t.hideturtle()
t.color("white")
t.write("Are you ready??" , align="center", font=("Arial", 30, "normal"))
time.sleep(1)
t.clear()
t.write("On Your Marks!", align="center", font=("Arial", 30, "normal"))
time.sleep(1)
t.clear()
t.write("Get Set!", align="center", font=("Arial", 30, "normal"))
time.sleep(1)
t.clear()
t.write("GO ---->", align="center", font=("Arial", 30, "normal"))
time.sleep(1)
t.clear()
winner_index = race(turtles)

winner = colors[winner_index]

screen.clear() 
screen.bgcolor("black")
screen.title("Race WINNER")


t.hideturtle()
t.penup()
t.goto(0, 50)
t.write(f"The winner of this race is {winner}!", align="center", font=("Arial", 30, "normal"))
t.goto(0,0)
t.write(f"Congratulations!!!" ,  align="center", font=("Arial", 30, "normal"))
time.sleep(5)
screen.bye()
