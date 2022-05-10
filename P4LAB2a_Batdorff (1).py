import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(4)
t.pencolor("green")
t.shape("turtle")

for i in (1,2,3,4):
    t.forward(100)
    t.left(90)

t.penup()
t.forward(200)
t.pendown()

for i in (1,2,3):
    t.forward(100)
    t.left(120)

win.mainloop()
