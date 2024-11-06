import turtle
import time

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("#300030")

t = turtle.Turtle()
t.hideturtle()
t.speed(3)

def draw_heart(x, y, size, color, thickness):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.pensize(thickness)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(size)
    
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.009)
    
    t.left(120)
    
    for _ in range(200):
        t.right(1)
        t.forward(size * 0.009)
    
    t.forward(size)
    t.end_fill()
    t.setheading(0)

hearts = [
    (0, -150, 300, "#480048", 5),
    (0, -135, 270, "#601848", 5),
    (0, -120, 240, "#c04848", 5),
    (0, -105, 210, "#f07241", 5),
    (0, -90, 180, "#eb613b", 5),
    (0, -75, 150, "#f2cc67", 5),
    (0, -50, 100, "#fbea80", 5)
]

for heart in hearts:
    draw_heart(*heart)
    time.sleep(0.5)

screen.mainloop()
