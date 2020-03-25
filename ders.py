import turtle
t = turtle.Pen()
t.speed(0)
no_of_circles = int(turtle.numinput("No of circles",
                                    "Enter any number you like",6))
size_of_circle = int(turtle.numinput("size",
                                     "enter any number you like",10))
for (x) in range(no_of_circles):
    t.circle(size_of_circle)
    t.left(360/no_of_circles)