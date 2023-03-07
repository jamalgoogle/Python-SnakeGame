import turtle 

wind = turtle.Screen()
wind.title('ping pong gameplay')
wind.setup(width=800 , height=600)
wind.tracer(0)



#madrab 1
madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape('square')
madrab1.color('blue')
madrab1.shapesize(stretch_wid= 5 , stretch_len= 1)
madrab1.penup()
madrab1.goto(-350 , 0)

#madrab 2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape('square')
madrab2.color('red')
madrab2.shapesize(stretch_wid= 5 , stretch_len= 1)
madrab2.penup()
madrab2.goto(350 , 0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('black')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15



    #madrap1 funciton
def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)
    
def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)
    
    #madrap2 funciton 
def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
    
def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)
    
#keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up , "w")
wind.onkeypress(madrab1_down , "s")


wind.onkeypress(madrab2_up , "Up")
wind.onkeypress(madrab2_down , "Down")



while True:
    wind.update()
    
    
#move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0 ,0)
        
    if ball.xcor() < -390:
        ball.goto(0 ,0)
        
    #touching between madrab and ballS
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 

    if(ball.xcor() < -340 and ball.xcor() > -350) and ( ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1 
        
