import turtle

def flower():
    window = turtle.Screen()
    window.bgcolor("white")

    
    flower = turtle.Turtle()
    flower.speed(100)
    i = 0
    while (i < 20):
        flower.forward(100)
        flower.right(150)
        flower.right(5)
        i += 1



    
    
    window.exitonclick()
flower()
