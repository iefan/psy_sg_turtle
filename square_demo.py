t.clear()
t.pu()
t.goto(0,-200)
t.pd()
a=-200
for i in range(40,9,-10):
    t.circle(i)
    t.goto(0,a+10)
    a+=10