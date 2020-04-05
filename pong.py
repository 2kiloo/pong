import turtle
#from tkinter import *

wn = turtle.Screen() #ccreate a window

wn.title("Pong by 2kiloo")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx =0.1
ball.dy =-0.1

#scorebaord
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.color("white")
pen.goto(0,260)
pen.hideturtle()
pen.write("Player A 0 - 0 Player B ",align="center",font=("Courier",24,"normal"))

#score
score_a =0
score_b =0


#Function paddle_a
def paddle_a_up():
    y =paddle_a.ycor()
    y +=20
    paddle_a.sety(y)
#Function paddle_a
def paddle_a_down():
    y =paddle_a.ycor()
    y -=20
    paddle_a.sety(y)
#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.listen()
wn.onkeypress(paddle_a_down,"s")

#Function paddle_b
def paddle_b_up():
    y =paddle_b.ycor()
    y +=20
    paddle_b.sety(y)
#Function paddle_b
def paddle_b_down():
    y =paddle_b.ycor()
    y -=20
    paddle_b.sety(y)
#keyboard binding
wn.listen()
wn.onkeypress(paddle_b_up,"Up")
wn.listen()
wn.onkeypress(paddle_b_down,"Down")


while True:
    wn.update()


    #move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #move border
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *=-1
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write("Player A  {} - {} Player B ".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b +=1
        pen.clear()
        pen.write("Player A  {} - {} Player B ".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    #ball and paddle collision

    if (ball.xcor() > 340 and ball.xcor() <350)and (ball.ycor()< paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor()< paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *=-1
