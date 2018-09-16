import turtle
import time
pen1 = turtle.Turtle()
paper = turtle.Screen()
colorList = ["blue","red","yellow"]
#addcolorList = ["green"]
colorList = colorList +["green","black","pink"] + ["blue","red","yellow"]
#colorList = colorList[1:5]
#print(colorList)

#a =int(input("Enter the Sides  "))
a= 4
j = 360/a



t1 = time.time()
for i in range(a):
   pen1.color(colorList[i])
   pen1.fd(100)
   pen1.right(j)
   time.sleep(1)
t2 = time.time()
print(t2 - t1)

msg = "Bye"
print (msg.capitalize)
