"""
KIT101 2.1PP Turtle Graphics of initials
"""

__author__ = "Ravi"

import turtle

def main():
    t = turtle.Turtle()

    t.pencolor("teal")
    t.speed(5)

    t.penup()
    t.right(135)

    "R start"
    t.forward(200)
    t.pendown()
    t.right(135)
    t.forward(200)
    t.left(90)
    t.circle(50, extent=-180)
    t.left(300)
    t.forward(115)
    "R end"

    
    t.penup()
    t.left(60)
    t.forward(50)
    t.pendown()
    t.circle(2)
    t.penup()
    t.forward(50)
    t.pendown()

    "S start"
    t.circle(50, 160)
    t.penup()
    t.right(80)
    t.forward(100)
    t.right(8)
    t.pendown()
    t.left(135)
    
    t.circle(64, 106)
    
    t.penup()
    t.forward(150)

    "t.circle(50, -270)"

    "S end"

    t.screen.mainloop()


if __name__ == "__main__":
    main()
