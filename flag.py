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
turtle.right(15)
turtle.fd(45)
turtle.setheading(180)
turtle.fd(96)
turtle.setpos(yellow_pos)
list2=turtle.pos()
angle=0
turtle.end_fill()
i=20
j=0
k=0
turtle.setheading(0)
#turtle.circle(70)

while(j<8):
	
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
	#turtle.dot("black")
	j+=1
	k+=3

angle=0
turtle.color("red")
turtle.setpos(yellow_pos)
turtle.color("yellow")
list2=turtle.pos()
i=20
j=0

while(j<8):
	
	list=list2
	turtle.setheading(180-angle)
	turtle.setpos(list)
	turtle.begin_fill()
	turtle.circle(-98,30)
	turtle.setheading(-10-angle)
	turtle.fd(i)
	i+=3
	list2=turtle.pos()
	print(i)
	print(list2)
	turtle.setpos(list)
	angle+=17
	turtle.end_fill()
	#turtle.dot("black")
	j+=1
turtle.end_fill()
turtle.color("red")
turtle.setpos(yellow_pos)
turtle.color("yellow")
turtle.setheading(90)
j=0

while(j<6):
	turtle.setheading(90)
	turtle.fd(15)
	list=turtle.pos()
	turtle.begin_fill()
	if(j%2==0):
		turtle.setheading(0)
		turtle.circle(35,90)
		turtle.setheading(190)
		turtle.fd(15)
		turtle.setpos(list)
	else:
		turtle.setheading(180)
		turtle.circle(-35,90)
		turtle.setheading(-10)
		turtle.fd(15)
		turtle.setpos(list)
	turtle.end_fill()
	j+=1
turtle.penup()
turtle.home()
turtle.pendown()
turtle.pensize(10)
turtle.pencolor("black")
turtle.setheading(90)
turtle.fd(300)
turtle.setheading(-90)
turtle.fd(600)



turtle.ht()
x=input()