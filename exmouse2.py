import turtle

def onmove(self, fun, add=None):
    """
    Bind fun to mouse-motion event on screen.

    Arguments:
    self -- the singular screen instance
    fun  -- a function with two arguments, the coordinates
        of the mouse cursor on the canvas.

    Example:

    >>> onmove(turtle.Screen(), lambda x, y: print(x, y))
    >>> # Subsequently moving the cursor on the screen will
    >>> # print the cursor position to the console
    >>> screen.onmove(None)
    """

    if fun is None:
        self.cv.unbind('<Motion>')
    else:
        def eventfun(event):
            fun(self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale)
        self.cv.bind('<Motion>', eventfun, add)

def onClickPos(self, fun, add=None):
    if fun is None:
        self.cv.unbind('<Button-1>')
    else:
        def eventfun(event):
            fun(self.cv.canvasx(event.x) / self.xscale, -self.cv.canvasy(event.y) / self.yscale)
        self.cv.bind('<Button-1>', eventfun, add)

def goto_handler(x, y):
    # onmove(turtle.Screen(), None)  # avoid overlapping events
    onClickPos(turtle.Screen(), None)
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    print(x,y)
    # onmove(turtle.Screen(), goto_handler)
    onClickPos(turtle.Screen(), goto_handler)

turtle.shape('turtle')

# onmove(turtle.Screen(), goto_handler)
onClickPos(turtle.Screen(), goto_handler)

turtle.mainloop()