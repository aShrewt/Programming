import turtle

s = turtle.getscreen()

t = turtle.Turtle()
t.color("green","yellow")

def picture():
    t.backward(500)
    for i in range(100):
        t.forward(1000)
        t.left(90)
        t.forward(1)
        t.left(85)


picture()

turtle.Screen().exitonclick()