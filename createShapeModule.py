
import threading
import turtle
import time
pen = turtle.Turtle()
pen2 = turtle.Turtle()
paper = turtle.Screen()

def drawCircle():
    for i in range(360):
      pen.fd(1)
      pen.right(1)
         
def pentagon(no):
    if no == 5:
        for i in range(5):
          pen.fd(100)
          pen.right(360/5)

    if no == 6:
        for i in range(6):
          pen.fd(100)
          pen.right(360/6)
 


 
