import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(25)
t.pencolor("cyan")
t.shape("turtle")

for i in range(6):
    t.left(60)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(120)

for i in range(6):
    t.left(60)
    t.forward(175)
    t.left(60)
    t.forward(75)
    t.backward(75)
    t.right(120)
    t.forward(75)
    t.backward(75)
    t.left(60)
    t.forward(75)
    t.backward(250)  

win.mainloop()
