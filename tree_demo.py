from turtle import *

reset()
speed(0)
pu()
goto(0,-200)
# pd()
lt(90)
colormode(255)
tree_leaf = 40
turn_angle = 13

def drawTree(n):
    if n == 0:
        return
    color(255//(n+1), 255//(n+1), 0)
    # 绘制一个二叉
    lt(turn_angle)
    pd()
    fd(tree_leaf)  
    pu() 
    bk(tree_leaf)
    rt(turn_angle*2) 
    pd()   
    fd(tree_leaf) 
    pu()   
    bk(tree_leaf)
    lt(turn_angle)   

    # 来到二叉的左支
    lt(turn_angle)
    pu()
    fd(tree_leaf)
    drawTree(n-1) 
    pu()
    bk(tree_leaf)
    rt(turn_angle)

    # 来到二叉的右支进行绘制
    rt(turn_angle)
    pu()
    fd(tree_leaf)
    drawTree(n-1)
    pu()
    bk(tree_leaf)
    lt(turn_angle)
    
    # drawTree(1)

drawTree(6)

input()