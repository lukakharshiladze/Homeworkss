from turtle import*

# we want to paint a house

# step 1; draw a square
speed(15)
shape("circle")
color("purple")
begin_fill()
width(4)
forward(300)
left(90)

forward(300)
left(90)

forward(300)
left(90) 

forward(300)
left(90)
end_fill()
# end of step 1


# step 2: draw a door

forward(120) 
color("grey")
begin_fill()
left(90)
forward (120)
right(90)
forward(80)
right(90)
forward(120)
end_fill()

#end of step 2

# step 3: draw a roof

penup()
goto(300,300)
pendown()

color("black")
begin_fill()
right(120)
forward(175)
left(60)
forward(175)
end_fill()

penup()
goto(40,260)
pendown()

#end of step 3

# drawing windows
color("red")
begin_fill()
left(60)
forward(70)
left(90)
forward(50)
left(90)
forward(70)
left(90)
forward(50)

penup()
goto(260,260)
pendown()

right(270)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(50)
end_fill()

#end of step 4


exitonclick()