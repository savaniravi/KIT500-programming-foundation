__author__ = "Ravi"

import turtle

def place_stamp(turtle_obj, color, x, y):
    """
    Draws the initials at a specified location with a given color.
    """
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.pendown()
    turtle_obj.pencolor(color)
    turtle_obj.speed(5)

    turtle_obj.penup()
    turtle_obj.right(135)

    # Drawing "R"
    turtle_obj.forward(200)
    turtle_obj.pendown()
    turtle_obj.right(135)
    turtle_obj.forward(200)
    turtle_obj.left(90)
    turtle_obj.circle(50, extent=-180)
    turtle_obj.left(300)
    turtle_obj.forward(115)

    turtle_obj.penup()
    turtle_obj.left(60)
    turtle_obj.forward(50)
    turtle_obj.pendown()
    turtle_obj.circle(2)
    turtle_obj.penup()
    turtle_obj.forward(50)
    turtle_obj.pendown()

    # Drawing "S"
    turtle_obj.circle(50, 160)
    turtle_obj.penup()
    turtle_obj.right(80)
    turtle_obj.forward(100)
    turtle_obj.right(8)
    turtle_obj.pendown()
    turtle_obj.left(135)
    turtle_obj.circle(64, 106)
    turtle_obj.penup()
    turtle_obj.forward(150)

    # resetting angle of pen
    turtle_obj.setheading(0)


def main():
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    
    place_stamp(t, "teal", -300, 0)
    place_stamp(t, "red", 0, 0)
    place_stamp(t, "blue", 300, 0)

    t.screen.mainloop()


if __name__ == "__main__":
    main()