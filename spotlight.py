# import package
import turtle

# basic setup
win = turtle.Screen()
win.title("Spotlight")
win.bgcolor("black")

# outline of the spotlight
pen = turtle.Turtle()
pen.color("yellow")
pen.width(3)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)

# red light
red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0, 40)


# yellow light
yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0, 0)


# green light
green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0, -40)

# basic setup: loop
win.mainloop()
