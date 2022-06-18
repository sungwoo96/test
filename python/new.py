import turtle
import time




t = turtle.Turtle()
s = turtle.title("2107110354 B반 조성우 태극기 그리기 과제")
t.speed(10)



# 태극기 긴 검은 줄
def long():
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(12.5)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(12.5)
    t.end_fill()



# 태극기 짧은 줄
def short():
    t.begin_fill()
    t.forward(45)
    t.left(90)
    t.forward(12.5)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(12.5)
    t.end_fill()



# 태극기 간격 1
def space1():
    t.left(180)
    t.penup()
    t.forward(18.75)
    t.pendown()
    t.right(90)



# 태극기 간격 2
def space2():
    t.left(90)
    t.penup()
    t.forward(55)
    t.pendown()



# 태극기 간격 3
def space3():
    t.right(90)
    t.penup()
    t.forward(55)
    t.pendown()
    t.left(180)



# 태극기 간격 4
def space4():
    t.penup()
    t.forward(18.75)
    t.pendown()
    t.left(90)



# 태극기 태극 문양
t.penup()
t.goto(100,0)
t.pendown()
t.left(90)
t.color("red")
t.begin_fill()
t.circle(100,180)
t.circle(50,180)
#t.penup()
#t.goto(100,0)
t.pendown()
t.circle(-50,180)
t.end_fill()
t.penup()
t.goto(-100,0)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(100,180)
t.circle(50,180)
#t.penup()
#t.goto(-100,0)
t.pendown()
t.circle(-50,180)
t.end_fill()



# 태극기 건
t.color("black")
t.penup()
t.goto(-150, 75)
t.pendown()
t.right(45)
long()
space1()
long()
space1()
long()



# 태극기 곤
t.penup()
t.goto(100, -150)
t.pendown()
t.left(90)
short()
space2()
short()
space4()
short()
space3()
short()
space4()
short()
space2()
short()



# 태극기 감
t.penup()
t.goto(160, 75)
t.left(90)
t.forward(12.5)
t.pendown()
t.left(90)
short()
space2()
short()
space4()
t.penup()
t.back(55)
long()
space4()
short()
space2()
short()



# 태극기 리
t.penup()
t.goto(-180, -100)
t.pendown()
t.right(90)
long()
space1()
short()
space2()
short()
t.penup()
t.left(180)
t.forward(18.75)
t.left(90)
t.forward(55)
t.left(180)
t.pendown()
long()


t.pu()
t.goto(300,0)
t.pd()
t.left(45)
t.forward(200)
t.right(90)
t.forward(600)
t.right(90)
t.forward(400)
t.right(90)
t.forward(600)
t.right(90)
t.forward(200)

time.sleep(999)