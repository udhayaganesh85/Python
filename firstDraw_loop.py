import turtle
pen1 = turtle.Turtle()
pen2 = turtle.Turtle()
paper = turtle.Screen()
"""
#draw Square 
for i in range(4):
   if i == 0:
       pen.color("red")
   if i == 1:
       pen.color("blue")
   if i == 2:
       pen.color("yellow")
   if i == 3:
       pen.color("green")
   pen.fd(10)
   pen.right(90)

"""
     
#draw circle
#for i in range(360):
   # pen.fd(1)
  #  pen.right(1)
    #pen.fd(1)
i=0
while i< 360:
   i += 1
   pen1.fd(1)
   pen2.fd(1)
   pen1.right(1)
     
   if i%90 == 0:
       pen2.right(90)
 
""""
j=0
while j<360:
    pen.fd(1)
    pen.right(1)
    j +=1
"""


print("DONE")