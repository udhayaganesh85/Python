import time
import threading
import turtle
import time
pen1 = turtle.Turtle()
paper = turtle.Screen()

a= 4
                   
#def first(a):
   
def second():
    global a
    while True:
        b = int(input("Enter the Sides  "))
        a = b
      
    #first(4)
secThd = threading.Thread(target = second)
secThd.start()
   ## secThd.join()

while True:
    pen1.fd(100)
    pen1.right(360/a)


