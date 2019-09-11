t.reset()
t.pu()
t.goto(-240,0)
t.pd()
t.goto(240,0)
t.stamp()
t.pu()
t.goto(0,-240)
t.lt(90)
t.pd()
t.goto(0,240)
t.stamp()
t.pu()
t.goto(0,0)
t.dot()
t.goto(5,-10)
t.write('o')
t.goto(240,20)
t.write('x')
t.goto(20,240)
t.write('y')
gap = 22
for i in range(1, 11):
    t.goto(gap*i, 0)
    t.pd()
    t.goto(gap*i, 10)
    t.pu()
    t.goto(gap*i, -20)
    t.write(i)

    t.goto(-1*gap*i, 0)
    t.pd()
    t.goto(-1*gap*i, 10)
    t.pu()
    t.goto(-1*gap*i-3, -20)
    t.write(-i)

    t.goto(0, gap*i)
    t.pd()
    t.goto(10, gap*i)
    t.pu()
    t.goto(-16, gap*i-4)
    t.write(i)

    t.goto(0, -1*gap*i)
    t.pd()
    t.goto(10, -1*gap*i)
    t.pu()
    t.goto(-16, -1*gap*i-6)
    t.write(-i)

#t.ht()
while True:
    zuobiao = s.textinput("提示", "请输入坐标，以','分开, 'quit'退出")
    if zuobiao.lower() == 'quit':
        break
    #t.st()
    pos_x,pos_y = zuobiao.split(",")
    t.pu()
    t.goto(int(pos_x)*gap, int(pos_y)*gap)
    t.dot()
    #t.ht()

