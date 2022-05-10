import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(3)
t.pencolor("maroon")
t.shape("turtle")

t.right(90)
t.forward(100)
t.right(45)
t.forward(15)
t.right(45)
t.forward(50)
t.right(45)
t.forward(15)

t.penup()
t.right(180)
t.forward(15)
t.left(45)
t.forward(75)
t.left(90)

t.pendown()
t.forward(110)
t.right(90)

for i in range(2):
    t.forward(50)
    t.right(45)
    t.forward(15)
    t.right(45)
    t.forward(35)
    t.right(45)
    t.forward(15)
    t.right(45)
    t.forward(50)
    t.right(180)


win.mainloop()
