import turtle
import time
# initialising
global playerA_score, playerB_score, replays
playerA_score = 0
playerB_score = 0
replays = 0

wn = turtle.Screen()
wn.title("pong by @Liangchen219")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.hideturtle()
pen.write("Press return to play", align='center', font=24)


#paddle movements
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y+20)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        paddle_a.sety(y-20)


def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y+20)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        paddle_b.sety(y-20)

def replay():
    global playerA_score, playerB_score, replays
    replays += 1
    playerA_score = 0
    playerB_score = 0
    ball.dx = 0.08 + 0.01*replays
    ball.dy = 0.08 + 0.01*replays
    pen.clear()
    pen.write("player A score:0, player B score:0", align='center', font='24')

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(replay, "Return")

# Main game loop
while True:
    wn.update()
    # ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # ball collision with boundary
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 390 or ball.xcor() < -390:
        #score management
        pen.clear()
        if ball.xcor() > 390:
            playerA_score += 1
            pen.write(f"player A score:{playerA_score}, player B score:{playerB_score}", align='center', font='24')
        else:
            playerB_score += 1
            pen.write(f"player A score:{playerA_score}, player B score:{playerB_score}", align='center', font='24')

        #reset ball
        ball.dx *= -1
        ball.goto(0, 0)

        # pauses
        time.sleep(1)

    # ball collision with paddles
    if (340 < ball.xcor() < 350) and (paddle_b.ycor()-55 < ball.ycor() < paddle_b.ycor()+55):
        ball.dx *= -1
    if (-350 < ball.xcor() < -340) and (paddle_a.ycor()-55 < ball.ycor() < paddle_a.ycor()+55):
        ball.dx *= -1

    #game over
    if (playerA_score == 2 or playerB_score==2):
        if playerA_score == 2:
            pen.clear()
            pen.write("Player A won! Press enter to replay! (It gets faster)", font='24', align='center')
        elif playerB_score == 2:
            pen.clear()
            pen.write("Player B won! Press enter to replay! (It gets faster)", font='24', align='center')
        ball.dx, ball.dy = 0, 0
        ball.goto(0, 0)
    
    
    