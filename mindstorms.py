#Elliott Hawks
#Nov 25, 2016
import turtle


def drawPicture():

    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()
    brad.speed(5)

    for x in range(0, 36):
        drawSquare(brad)
        brad.right(10)



    #drawCircle()
    #drawTriangle()

    window.exitonclick()

def drawSquare(myTurtle):
    
    for x in range(0, 4):
        myTurtle.forward(100)
        myTurtle.right(90)

def drawCircle():
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("red")
    angie.circle(50)

def drawTriangle():
    tim = turtle.Turtle()
    tim.shape("triangle")
    tim.right(120)
    tim.forward(50)
    tim.right(120)
    tim.forward(50)
    tim.right(120)
    tim.forward(50)


drawPicture()

