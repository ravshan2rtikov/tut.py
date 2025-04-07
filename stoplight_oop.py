# packages
import turtle

# main window
win = turtle.Screen()
win.title("Stoplight made with OOP")
win.bgcolor("black")


# class
class Stoplight:
    def __init__(self, x, y):
        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("yellow")
        self.pen.goto(x - 30, y + 60)
        self.pen.down()
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)
        self.pen.rt(90)
        self.pen.fd(60)
        self.pen.rt(90)
        self.pen.fd(120)

        self.red_light = turtle.Turtle()
        self.yellow_light = turtle.Turtle()
        self.green_light = turtle.Turtle()

        self.red_light.speed(0)
        self.yellow_light.speed(0)
        self.green_light.speed(0)

        self.red_light.color("grey")
        self.yellow_light.color("grey")
        self.green_light.color("grey")

        self.red_light.shape("circle")
        self.yellow_light.shape("circle")
        self.green_light.shape("circle")

        self.red_light.penup()
        self.yellow_light.penup()
        self.green_light.penup()

        self.red_light.goto(x, y + 40)
        self.yellow_light.goto(x, y)
        self.green_light.goto(x, y - 40)


stoplight = Stoplight(0, 0)
stoplight2 = Stoplight(-100, 0)
stoplight3 = Stoplight(100, 0)


win.mainloop()
