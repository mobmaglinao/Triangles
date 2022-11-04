import turtle

display = turtle.Screen()

turtle.color('green', 'green')

# set pen width, speed, shape
turtle.width(3)
turtle.shape('turtle')
turtle.speed(4)

def triangle(edge=100):
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.right(120)
    turtle.forward(edge)
    turtle.left(300)

triangle()
triangle()
triangle()
triangle()
triangle()
triangle()

display.mainloop()