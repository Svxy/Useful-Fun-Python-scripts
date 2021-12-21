import random
import turtle
tim = turtle.Turtle()
tim.speed(0)

def sky(colour):
  wn = turtle.Screen()
  wn.bgcolor(colour)
  
sky ('black')

def pen(colour):
  tim.color(colour)
  
pen('red')

def firework1(size):
  for num in range(20):
    tim.fd(size)
    tim.rt(180-(360/20))
    
firework1(60)

def move():
  tim.pu()
  x=random.randint(-150,150)
  y=random.randint(-150,150)
  tim.goto(x,y)
  tim.pd()
  
move()
pen('yellow')
firework1(30)
move()
pen('blue')
firework1(57)
move()
pen('purple')
firework1(80)
move()
pen('lightblue')
firework1(120)
move()
pen('pink')
firework1(100)
move()
pen('orange')
firework1(54)
move()
pen('violet')
firework1(33)
move()
pen('green')
firework1(68)
move()
pen('gold')
firework1(150)
move()
pen('silver')
firework1(47)
move()
pen('darkgreen')
firework1(99)