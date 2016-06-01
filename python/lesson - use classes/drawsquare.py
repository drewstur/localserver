import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")


    
    def draw_square():
        brad = turtle.Turtle()
        brad.speed(10)
        i = 0
        while (i < 4):
            brad.forward(100)
            brad.right(90)
            i += 1

    def draw_circle():
        angie = turtle.Turtle()
        angie.shape("arrow")
        angie.color("blue")
        angie.circle(100)

    def draw_triangle():
        mark = turtle.Turtle()
        mark.penup()
        mark.goto(100,100)
        mark.pendown()
        triangleSize = 100
        for i in range(0, 3):
            mark.forward(triangleSize)
            mark.right(120)

    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()
draw_shapes()
