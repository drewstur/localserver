import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.speed(10)
    brad.forward(100)
    brad.right(90)
    brad.forward(20)
    brad.right(90)
    brad.forward(80)
    brad.left(90)
    brad.forward(80)
    brad.left(90)
    brad.forward(60)
    brad.left(90)
    brad.forward(30)
    brad.left(90)
    brad.forward(40)
    brad.right(90)
    brad.forward(20)
    brad.right(90)
    brad.forward(60)
    brad.right(90)
    brad.forward(70)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(120)
    brad.right(90)

    angie = turtle.Turtle()
    angie.speed(10)
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
    window.exitonclick()
draw_square()
