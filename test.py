import turtle

# Define the turtle window and set the background color
turtle.setup(width=600, height=600)
turtle.bgcolor("black")

# Define the turtle shape and set the turtle color
turtle.shape("turtle")
turtle.color("white")

# Draw the heart shape
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.pensize(10)
turtle.pencolor("white")
turtle.left(45)
turtle.forward(150)
turtle.circle(75, 180)
turtle.right(90)
turtle.circle(75, 180)
turtle.forward(150)
turtle.end_fill()

# Draw the arrow
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.pensize(5)
turtle.pencolor("white")
turtle.right(135)
turtle.forward(100)
turtle.right(180)
turtle.forward(100)
turtle.right(135)
turtle.forward(50)

turtle.done()
