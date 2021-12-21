from tkinter import * 
from tkinter import messagebox
import turtle
import time
import sys
import os

screen = turtle.Screen()
screen.setup(800,800)
screen.title("Tic Tac Toe - by Cutiey")
screen.setworldcoordinates(-5,-5,5,5)
screen.bgcolor('black')
screen.tracer(0,0)
turtle.hideturtle()

def draw_board():
    turtle.pencolor('green')
    turtle.pensize(10)
    turtle.up()
    turtle.goto(-3,-1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3,1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)

def draw_circle(x,y):
    turtle.up()
    turtle.goto(x,y-0.75)
    turtle.seth(0)
    turtle.color('red')
    turtle.down()
    turtle.circle(0.75, steps=100)

def draw_x(x,y):
    turtle.color('purple')
    turtle.up()
    turtle.goto(x-0.75,y-0.75)
    turtle.down()
    turtle.goto(x+0.75,y+0.75)
    turtle.up()
    turtle.goto(x-0.75,y+0.75)
    turtle.down()
    turtle.goto(x+0.75,y-0.75)
    
def draw_piece(i,j,p):
    if p==0: return
    x,y = 2*(j-1), -2*(i-1)
    if p==1:
        draw_x(x,y)
    else:
        draw_circle(x,y)
    
def draw(b):
    draw_board()
    for i in range(3):
        for j in range(3):
            draw_piece(i,j,b[i][j])
    screen.update()

def gameover(b):
    if b[0][0]>0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]: return b[0][0]
    if b[1][0]>0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]: return b[1][0]
    if b[2][0]>0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]: return b[2][0]
    if b[0][0]>0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]: return b[0][0]
    if b[0][1]>0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]: return b[0][1]
    if b[0][2]>0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]: return b[0][2]
    if b[0][0]>0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]: return b[0][0]
    if b[2][0]>0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]: return b[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p==9: return 3
    else: return 0
    
def play(x,y):
    global turn
    i = 3-int(y+5)//2
    j = int(x+5)//2 - 1
    if i>2 or j>2 or i<0 or j<0 or b[i][j]!=0: return
    if turn == 'x': b[i][j], turn = 1, 'o'
    else: b[i][j], turn = 2, 'x'
    draw(b)
    r = gameover(b)
    if r==1:
        screen.textinput("Game over!","X won!\nRate the game 1-10:")  
        messagebox.showinfo("Cutieys Tic Tac Toe", "Thank you for your feedback!\n\ntwitch.tv/cutiey")
        time.sleep(2)
        turtle.bye()
    elif r==2:
        screen.textinput("Game over!","O won!\nRate the game 1-10:")
        messagebox.showinfo("Cutieys Tic Tac Toe", "Thank you for your feedback!\n\ntwitch.tv/cutiey")
        time.sleep(2)
        turtle.bye()
    elif r==3:
        screen.textinput("Game over!", "Tie!\nRate the game 1-10:")
        messagebox.showinfo("Cutieys Tic Tac Toe", "Thank you for your feedback!\n\ntwitch.tv/cutiey")
        time.sleep(2)
        turtle.bye()

    
b = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]    
draw(b)
turn = 'x'
screen.onclick(play)
turtle.mainloop()