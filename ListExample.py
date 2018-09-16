import turtle
pen1 = turtle.Turtle()
paper = turtle.Screen()
colorList = ["blue","red","yellow"]
#addcolorList = ["green"]
colorList = colorList +["green","black","pink"]
colorList = colorList[1:5]
print(colorList)

a =input("Enter the Sides = ")

for i in range(a):
   pen1.color(colorList[i])
   pen1.fd(100)
   pen1.right(90)

msg = "Bye"
print (msg.capitalize)
