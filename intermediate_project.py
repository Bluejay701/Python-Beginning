#Jackson Pollock:

import turtle
import random
colors = ["navy", "yellow", "green", "blue", "orange", "violet"]
shapes = ["square", "arrow", "classic", "circle", "triangle", "turtle"]

t = turtle.Turtle()
screen = turtle.Screen()

def change_color():
    t.color(random.choice(colors))

def change_shape(chosen_shape):
    t.shape(chosen_shape)

def draw_square():
  	t.setheading(random.randint(0, 360))
  	t.forward(random.randint(0, 200))
  	t.begin_fill()
  	length = random.randint(0, 50)
  	for i in range(4):
  	  	t.forward(length)
  	  	t.right(90)
  	t.end_fill()
    
def draw_triangle():
  t.setheading(random.randint(0, 360))
  t.forward(random.randint(0, 250))
  length = random.randint(0, 200)
  for x in range(2):
    t.forward(length)
    t.left(120)

def draw_star():
  t.setheading(random.randint(0,360))
  t.penup()
  t.forward(random.randint(0, 250))
  t.pendown()
  x = random.randint(10, 100)
  t.begin_fill()
  for i in range(5):
    t.forward(x)
    t.right(144)

while True:
    init_x = random.randrange(-50,50)
    init_y = random.randrange(-50,50)
    t.goto(init_x, init_y)

    t.speed(random.randint(0,75))
    change_color()
    screen.bgcolor(random.choice(colors))
    t.pensize(random.randint(1,50))
    s = random.randint(0, 5)
    change_shape(shapes[s]) 

    if s == 0:
        draw_square()
    elif s == 1 or s == 2:
        t.right(90)
        t.forward(random.randrange(10, 250))
    elif s == 3:
      t.forward(random.randrange(10, 250))
      t.circle(random.randint(1, 50))
    elif s == 4:
        draw_triangle()
    elif s == 5:
        draw_star()
