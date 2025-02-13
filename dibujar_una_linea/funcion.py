import turtle

def draw_line(x1, y1, paso=20):
    turtle.penup()
    turtle.goto(x1, y1)

    for i in range(paso + 1):
        x = x1 * (i / paso)
        y = y1
        turtle.goto(x, y)
        turtle.dot(3, "black")  

draw_line(100, 100)

input('')