from turtle import *
speed(15)
color('purple')
bgcolor('black')

a = 100

sety(a)
sety(-a)
sety(0)
setx(a)
setx(-a)
#right arm
goto(a, 0)
goto(a, a)
goto(a, 0)
goto(0, 0)
#up arm
goto(0, a)
goto(-a, a)
goto(0, a)
goto(0, 0)
#left arm
goto(-a, 0)
goto(-a, -a)
goto(-a, 0)
goto(0, 0)
#down arm
goto(0, -a)
goto(a, -a)
goto(0, -a)
goto(3 * 100, 0)


"""left(50)
up(a)
down(a)
right(a)"""

"""up(a)
right(a)
left(a)
down(a)

right(a)
down(a)
up(a)
left(a)

down(a)
left(a)
right(a)
up(a)"""

i =200

while i > 0:
    left(i)
    forward(i+3)
    i -= 1
