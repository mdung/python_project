import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle for the character
character = turtle.Turtle()
character.shape("circle")  # Set the shape to a circle

# Draw the head
character.penup()
character.goto(0, -200)  # Set the starting position
character.pendown()
character.color("yellow")
character.begin_fill()
character.circle(100)  # Head radius
character.end_fill()

# Draw the eyes
character.penup()
character.goto(-40, 20)  # Left eye position
character.pendown()
character.color("black")
character.begin_fill()
character.circle(15)  # Eye radius
character.end_fill()

character.penup()
character.goto(40, 20)  # Right eye position
character.pendown()
character.begin_fill()
character.circle(15)  # Eye radius
character.end_fill()

# Draw the mouth
character.penup()
character.goto(-30, -30)  # Mouth position
character.pendown()
character.width(5)
character.right(90)
character.circle(30, 180)  # Draw a semicircle for the mouth

# Hide the turtle
character.hideturtle()

# Keep the window open
turtle.mainloop()
