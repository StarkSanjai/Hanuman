from turtle import *
clr = ["yellow","gold","orange","red","maroon","violet","magenta","purple","navy","blue","skyblue","cyan","turquoise","lightgreen","green","green","darkgreen","chocolate","brown","black","gray","white"]
def goto_f(x,y):
    penup()
    goto(x,y)
    pendown()
speed(0)
pencolor("black")
def box():
    fillcolor("#fc6603")
    begin_fill()
    fd(325)
    rt(90)
    fd(782)
    rt(90)
    fd(705)
    rt(90)
    fd(782)
    rt(90)
    fd(380)
    end_fill()
    
def outsideL():
	fillcolor("black")
	begin_fill()
	rt(60)
	circle(-52,34)
	lt(90)
	circle(-21,100)
	fd(15)
	circle(300,8)
	lt(68)
	fd(33)
	lt(10)
	bk(36)
	lt(-40)
	circle(60,50)
	circle(-40,60)
	fd(1)
	lt(8)
	circle(-40,-60)
	rt(25)
	circle(-50,105)
	lt(50)
	circle(-50,-35)
	circle(-3,-180)
	circle(45,-18)
	rt(12)
	circle(50,-41)
	rt(100)
	circle(-55,108)
	lt(150)
	circle(-25,75)
	fd(5)
	lt(5)
	circle(40,65)
	lt(60)
	circle(25,-105)
	rt(36)
	fd(25)
	lt(95)
	fd(10)
	circle(-30,90)
	fd(20)
	circle(8,90)
	lt(25)
	bk(20)
	circle(8,-95)
	bk(20)
	circle(-2,-180)
	bk(15)
	lt(180)
	circle(-40,75)
	fd(15)
	lt(130)
	fd(8)
	circle(-60,80)
	fd(25)
	bk(25)
	circle(-51,-100)
	circle(10,-145)
	bk(15)
	circle(-10,-100)
	bk(8)
	rt(90)
	circle(5,90)
	lt(60)
	circle(-35,-100)
	bk(8)
	lt(20)
	fd(16)
	lt(157)
	circle(-190,35)
	lt(90)
	fd(25)
	circle(-10,70)
	fd(20)
	circle(20,40)
	lt(40)
	circle(20,-55)
	lt(180)
	circle(2,190)
	fd (15)
	lt(30)
	circle (-70,95)
	fd(15)
	lt(15)
	bk(25)
	circle(-45,-95)
	circle(40,-60)
	rt(180)
	circle(2,185)
	fd(20)
	lt(23)
	circle(-130,20)
	lt(10)
	circle(-120,-35)
	lt(95)
	fd(2)
	rt(70)
	circle(-40,38)
	lt(140)
	fd(20)
	circle(500,15)
	lt(137)
	circle(-250,32)
	lt(130)
	circle(-200,19)
	lt(5)
	circle(-200,-19)
	rt(30)
	bk(13)
	rt(106)
	circle(-250,-35)
	lt(50)
	bk(8)
	rt(54)
	circle(-270,33)
	rt(74)
	fd(110)
	rt(30)
	circle(200,25)
	lt(7)
	circle(200,-30)
	rt(110)
	fd(30)
	lt(65)
	circle(-350,18)
	lt(9)
	circle(-350,-16)
	rt(66)
	circle(200,38)
	circle(9,110)
	rt(100)
	bk(15)
	fd(35)
	lt(165)
	circle(-170,26)
	lt(5)
	circle(-170,-42)
	rt(5)
	bk(10)
	rt(170)
	fd(70)
	circle(2,145)
	p=pos()
	fd(20)
	rt(90)
	fd(20)
	rt(100)
	fd(18)
	circle(200,15)
	lt(115)
	fd(25)
	rt(65)
	fd(65)
	lt(28)
	fd(30)
	bk(93)
	rt(50)
	circle(200,5)
	rt(105)
	circle(-20,60)
	lt(50)
	circle(9,80) 
	rt(5)
	circle(60,60)
	rt(18)
	circle(-60,54)
	circle(30,45)
	circle(-1,150)
	fd(15)
	lt(124)
	circle(200,35)
	lt(130)
	fd(30)
	rt(160)
	circle(150,35) 
	fd(20)
	stamp()
	lt(5)
	circle(85,58) 
	fd(25)
	circle(15,95)
	fd(10)
	circle(-2,145) 
	rt(20)
	fd(29)
	lt(72)
	fd(32)
	lt(45)
	fd(45)
	lt(24)
	circle(121,-29)
	rt(42)
	end_fill()
	return p

def outsideR(p):
	penup()
	goto(p)
	pendown()
	begin_fill()
	lt(100)
	fd(10)
	lt(180)
	circle (200,-23)
	circle(10,-12)
	circle(200,-25)
	lt(30)
	circle(250,-30)
	circle(1,-178)
	circle(-250,-25)
	lt(128)
	bk(78)
	lt(25)
	fd (27)
	circle(2,165)
	circle(150,15)
	lt(10)
	fd(27)
	rt(29)
	bk(25)
	lt(17)
	circle(400,20)
	rt(58)
	fd(115)
	rt(90)
	fd(782)
	rt(90)
	fd(175)
	rt(122)
	circle(200,45)
	circle(-90,42)
	circle(10,102)
	rt(65)
	circle(20,-50)
	bk(3)
	circle(1,-175)
	bk(2)
	circle(-20,-46)
	rt(142)
	fd(30)
	lt(120)
	fd(3)
	rt(165)
	circle(30,80)
	lt(25)
	bk(17)
	lt(113)
	fd(30)
	lt(60)
	circle(-20,65)
	fd(45)
	circle(1,170)
	fd(45)
	circle(45,80)
	rt(71)
	fd(22)
	rt(102)
	fd(12)
	lt(60)
	fd(60)
	rt(70)
	circle(20,95)
	rt(79)
	circle(60,75)
	lt(80)
	circle(-28,70)
	rt(125)
	fd(41)
	circle(8,72)
	fd(22)
	lt(145)
	circle(-45,57)
	rt(60)
	circle(70,60)
	circle(-1,170)
	fd(50)
	circle(180,28)
	circle(1,174)
	circle(-180,26)
	circle(180,25)
	rt(160)
	circle(220,15)
	fd(20)
	circle(1,177)
	fd(20)
	circle(-120,21)
	circle(-120,15)
	circle(-1,155)
	fd(50)
	circle(1,173)
	fd(60)
	circle(-1,155)
	fd(80)
	circle(300,28)
	circle(1,175)
	circle(-300,32)
	circle(200,48)
	rt(180)
	fd(17)
	circle(8,42)
	fd(22)
	lt(155)
	circle (-55,42)
	circle(50,33)
	circle(-40,36)
	rt(100)
	fd(35)
	end_fill()
	
def eye1():
    lt(20)
    color("#fc6603")
    begin_fill()
    bk(18)
    bk(27)
    lt(45)
    circle(-15,-90)
    lt(45)
    bk(25)
    lt(46)
    bk(30)
    end_fill()
    rt(45)
    fd(20)
    color("black")
    begin_fill()
    circle(8,145)
    rt(155)
    fd(8)
    circle(-4,95)
    fd(8.5)
    lt(105)
    bk(14)
    end_fill()
    
def t1():
	lt(285)
	begin_fill()
	circle(200,17)
	fd(130)
	rt(5)
	bk(130)
	circle(-200,-17)
	end_fill()
	rt(15)
	bk(8)
	penup()
	fd(138)
	rt(90)
	fd(25)
	pendown()
	begin_fill()
	rt(93) 
	fd(90)
	circle(-200,15)
	circle(-10,140)
	circle(-200,15)
	fd(90)
	bk(70)
	rt(5)
	circle(-300,-14)
	circle(-15,-155)
	circle(-300,-11)
	end_fill()
	
def ear():
    lt(105)
    begin_fill()
    lt(25)
    pensize(2)
    circle(55,99)
    circle(40,123)
    fd(32)
    pensize(6)
    rt(90)
    bk(5)
    fd(5)
    lt(90)
    pensize(0)
    fd(33)
    lt(10)
    fd(35)
    lt(145)
    fd(10)
    circle(-1,165)
    fd(18)
    circle(1,125)
    fd(10)
    circle(-0.6,125)
    fd(13)
    circle(1,164)
    fd(52)
    rt(38)
    circle(55,30)
    color("#fc6603")
    end_fill()
    lt(130)
    fd(15)
    color("black")
    rt(135)
    fd(25)
    lt(15)
    circle(7,20)
    fd(15)
    begin_fill()
    circle(17,187)
    fd(42)
    circle(-9,50)
    fd(14)
    circle(-4,100)
    fd(5)
    lt(70)
    fd(5)
    rt(140)
    fd(24)
    circle(8,67)
    fd(18)
    circle(-4,16) 
    circle(-35,120)
    rt(20)
    circle(-20,50)
    fd(10)
    end_fill()
    goto_f(40,4)
    rt(24)
    begin_fill()
    circle(60,45)
    circle(20,155)
    circle(50,55)
    circle(2,155)
    color("#fc6603")
    fd(25)
    circle(-15,150)
    end_fill()
    
def eye2():
	color("black")
	begin_fill()
	lt(180)
	fd(20)
	rt(110)
	circle(40,30) 
	lt(45)
	fd(10)
	lt(130)
	fd(10)
	circle(-10,90)
	fd(50)
	circle(80,25)
	circle(1,176)
	circle(-90,20)
	rt(15)
	fd(40)
	rt(155)
	fd(75)
	rt(2)
	bk(80)
	lt(15)
	fd(40)
	lt(9)
	circle(-100,35)
	bk(8)
	rt(35)
	circle(80,-37)
	bk(18)
	circle(-2,-180)
	bk(27)
	rt(1)
	circle(60,-40)
	lt(138)
	fd(70)
	rt(128)
	circle(-140,8)
	rt(61)
	pensize(3)
	circle(80,30)
	circle(20,122)
	circle(20,-122)
	circle(80,-30)
	lt(61)
	pensize(1)
	circle(-140,12)
	rt(130)
	circle(12,110)
	rt(70)
	circle(8,-100)
	lt(68)
	circle(-10,-47)
	lt(80)
	circle(-140,26)
	lt(160)
	circle(90,54)
	rt(45)
	circle(40,52)
	rt(106)
	circle(-5,93)
	fd(128)
	lt(163)
	fd(22)
	lt(8)
	circle(-30,38)
	rt(8)
	circle(20,60)
	fd(15)
	circle(-1,170)
	fd(20)
	circle(-20,78)
	fd(8)
	lt(70)
	fd(25)
	lt(175)
	circle(-20,85)
	circle(10,95)
	fd(47)
	rt(110)
	fd(15)
	circle(-10,80)
	fd(5)
	lt(160)
	fd(5)
	circle(15,80)
	fd(15)
	rt(25)
	fd(15)
	rt(145)
	circle(160,20)
	rt(30)
	fd(80)
	lt(178)
	fd(100)
	lt(16)
	fd(32)
	rt(31)
	fd(30)
	rt(135)
	fd(8)
	lt(154)
	circle(-60,35)
	end_fill()

def ff():
    begin_fill()
    lt(206)
    fd(35)
    circle(-12,68)
    fd(16)
    circle(8,115)
    fd(10)
    lt(160)
    fd(12)
    rt(95)
    fd(27)
    circle(12,60)
    lt(40)
    circle(-12,-60)
    bk(35)
    lt(80)
    bk(8)
    lt(100)
    bk(29)
    circle(12,-69)
    bk(35)
    rt(20)
    bk(42)
    circle(12,-92)
    bk(40)
    lt(90)
    bk(30)
    lt(115)
    bk(53)
    circle(-10,-48)
    bk(15)
    lt(51)
    fd(15)
    circle(10,82)
    fd(40)
    circle(-12,133)
    fd(35)
    lt(165)
    fd(45)
    circle(16,144)
    fd(48)
    circle(-12,92)
    fd(42) 
    end_fill()
    penup()
    bk(42)
    circle(-12,-92)
    bk(43)
    pendown()
    circle(50,-51)
    circle(-2,-104)
    circle(-100,-74)
    

goto_f(25,400)
box()
goto_f(55,400)
p=outsideL()
outsideR(p)
goto_f(-220,126)
eye1()
goto_f(-155,178)
t1()
goto_f(109,65)
ear()
goto_f(-140,125)
eye2()
goto_f(-151,-40)        
ff()
goto_f(180,360)    
goto_f(90,320)
hideturtle()
for i in range(22):
    color(clr[i])
    delay(70)
    write('Jai Hanuman',font=("Bookman Old Style",18))
done()
