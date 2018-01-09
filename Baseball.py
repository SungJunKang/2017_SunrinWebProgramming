import turtle as t

t.speed(0)

#야구공 그리기
t.circle(100)

t.goto(40, 7)
t.right(270)
t.color("red")
t.forward(185)

t.penup()
t.goto(-50, 185)
t.pendown()

t.right(180)
t.forward(170)

t.penup()
t.forward(200)
t.pendown()

t.color("brown")
#배트 몸통
t.left(90)
t.forward(300)
t.left(90)
t.forward(50)
t.left(90)
t.forward(300)
t.left(90)
t.forward(50)

#배트 손잡이
t.right(92)
t.forward(200)
t.left(90)
t.forward(30)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(30)
t.left(92)
t.forward(200)

