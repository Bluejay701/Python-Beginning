import turtle
import random

colors = ["navy", "yellow", "green", "blue", "orange", "violet"]
shapes = ["square", "arrow", "classic", "circle", "triangle", "turtle"]

turtles = []
for i in range(3):
  turtles.append(turtle.Turtle())
screen = turtle.Screen()

def step(x):
  x.color(random.choice(colors))
  x.setheading(random.randint(-180, 180))
  x.forward(random.randint(1, 50))

def square(x):
  len = random.randint(5, 50)
  for i in range(4):
    x.forward(len)
    x.left(90)


while True:
  for t in turtles:
    step(t)
    num = random.random()
    if num < 0.1:
      square(t)
