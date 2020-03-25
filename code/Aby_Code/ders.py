import turtle
t = turtle.Pen()
t.spee
no_of_circles = int(turtle.numinput("enter any number"))
radius = int(turtle.numinput("enter any number"))
for (x) in range(no_of_circles):
    t.circle(radius)
    t.left(360/no_of_circles)