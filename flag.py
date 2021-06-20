import turtle
turtle.speed(10)
turtle.color("blue")
turtle.begin_fill()
turtle.fd(500)
turtle.left(90)
turtle.fd(125)
turtle.setpos(0,0)
turtle.end_fill()

#red color
turtle.color("red")
turtle.begin_fill()
turtle.fd(250)
turtle.setpos(500,125)
turtle.setpos(0,0)
turtle.end_fill()

#green color
turtle.setpos(0,250)
turtle.color("green")
turtle.begin_fill()
turtle.right(90)
turtle.fd(500)
turtle.right(90)
turtle.fd(125)
turtle.setpos(0,250)
turtle.end_fill()

#yellow color
turtle.color("red")
turtle.setpos(110,55)
yellow_pos=turtle.pos()
turtle.color("yellow")
turtle.begin_fill()
turtle.setheading(0)
turtle.right(30)
turtle.fd(15)
turtle.setheading(180)
turtle.fd(26)
turtle.setpos(yellow_pos)
list2=turtle.pos()
angle=0
turtle.end_fill()
i=20
j=0
k=0
turtle.setheading(0)
turtle.circle(70)

while(j<7):
	
	list=list2
	turtle.setheading(angle)
	turtle.setpos(list)
	turtle.begin_fill()
	turtle.circle(98,30)
	turtle.setheading(190+angle)
	turtle.fd(i)
	i+=3
	list2=turtle.pos()
	print(list2)
	turtle.setpos(list)
	angle+=17
	turtle.end_fill()
	turtle.dot("black")
	j+=1
	k+=3

angle=0
turtle.color("red")
turtle.setpos(yellow_pos)
turtle.color("yellow")
list2=turtle.pos()
i=10
j=0

while(j<7):
	
	list=list2
	turtle.setheading(180-angle)
	turtle.setpos(list)
	turtle.begin_fill()
	turtle.circle(-98,30)
	turtle.setheading(-10-angle)
	turtle.fd(i)
	i+=1
	list2=turtle.pos()
	print(list2)
	turtle.setpos(list)
	angle+=15
	turtle.end_fill()
	turtle.dot("black")
	j+=1

turtle.end_fill()









turtle.ht()
x=input()