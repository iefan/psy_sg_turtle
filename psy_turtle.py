# import PySimpleGUI as sg 
import PySimpleGUI as sg 
import turtle as tt 
import tkinter.font
from tkinter import filedialog
import tkinter
import platform 

if platform.system() == "Linux":
    size_history = (15, 28)
    size_command = (68, 3)
    size_blank = 50
    size_status = (70, 1)
    size_sep = 40
elif platform.system() == "Windows":
    size_history = (18, 29)
    size_command = (72, 3)
    size_blank = 59
    size_status = (80, 1)
    size_sep = 42


outputmenu = ['',['导出为psy文件', "清空当前历史"]]
layout = [[sg.Canvas(size=(500, 500), background_color='white', key='_canvas_'),\
            sg.Listbox(values=["命令历史："], size=size_history, key='_history_', bind_return_key=True,right_click_menu=outputmenu)],
            [sg.T("绘图命令："), sg.InputText(focus=True, size=size_command, key='_command_',),], 
            # [sg.T("背景命令："), sg.InputText(size=size_command, key='_commandTs_',),], 
            [sg.Button("运行",), sg.Button("退出",), sg.T(" "*size_blank), sg.Button("执行文件",)],
            [sg.Text("__"*size_sep)],
            [sg.Text("运行状态显示～～～",size=size_status, font=('宋体', 10), key="_status_")],
            ]      

window = sg.Window('小海龟绘图', return_keyboard_events=True, font=('宋体', 12)).Layout(layout).Finalize()    

# 按pixel排列
# window.FindElement('_canvas_').TKCanvas.place(x=0, y=0, height=500, width=500)l


#================= 绑定doubleclick =================================
# historywindow = window.FindElement('_history_').TKText
# def doubleClickSelToCommand(event):
#     # actual_callback(event) # this will select the word
#     w = historywindow.selection_get()
#     # print(historywindow.get(1,2), 'get===========')
#     window.FindElement('_command_').Update(w)
#     # print(w)
# historywindow.bind("<Double-Button-1>", lambda e: historywindow.after(2, doubleClickSelToCommand, e)) # wait 2 ms before running callback
#=====================================================================

#================= 绑定return =================================
# commandwindow = window.FindElement('_command_').TKEntry
# commandwindow.place(x=0, y=0, height=30, width=650)

# def enterKeyRun(event):
#     tmpcmd = commandwindow.get().strip()
#     if tmpcmd != "":
#         try:
#             tmpcmd = "t." + tmpcmd
#             eval(tmpcmd)
#             tmphistory = historywindow.get("1.0", "end")
#             tmphistory += tmpcmd[2:]
#             # print(window.FindElement('_history_').TKText.get("1.0", "end"))
#             window.FindElement('_history_').Update(disabled=False)  
#             window.FindElement('_history_').Update(tmphistory)
#             window.FindElement('_history_').Update(disabled=True)
#             # print(1)
#         except:
#             pass
#             # sg.MsgBox("不可识别的!")
#         commandwindow.delete(0, 'end')
# commandwindow.bind('<Return>',enterKeyRun)
#=====================================================================

# charpixels = tkinter.font.Font().measure('A')
# window.FindElement('_history_').Update("命令历史:")
# window.FindElement('_history_').Update(disabled=True)

# screenCmdLst = ['_RUNNING', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bgcolor', '_bgpic', '_bgpicname', '_bgpics', '_blankimage', '_color', '_colormode', '_colorstr', '_createimage', '_createline', '_createpoly', '_delay', '_delayvalue', '_delete', '_drawimage', '_drawline', '_drawpoly', '_image', '_incrementudc', '_iscolorstring', '_keys', '_listen', '_mode', '_onclick', '_ondrag', '_onkeypress', '_onkeyrelease', '_onrelease', '_onscreenclick', '_ontimer', '_pointlist', '_rescale', '_resize', '_setbgpic', '_setscrollregion', '_shapes', '_tracing', '_turtles', '_type', '_update', '_updatecounter', '_window_size', '_write', 'addshape', 'bgcolor', 'bgpic', 'canvheight', 'canvwidth', 'clear', 'clearscreen', 'colormode', 'cv', 'delay', 'getcanvas', 'getshapes', 'listen', 'mainloop', 'mode', 'numinput', 'onclick', 'onkey', 'onkeypress', 'onkeyrelease', 'onscreenclick', 'ontimer', 'register_shape', 'reset', 'resetscreen', 'screensize', 'setworldcoordinates', 'textinput', 'tracer', 'turtles', 'update', 'window_height', 'window_width', 'xscale', 'yscale']
# turtleCmdLst = ['DEFAULT_ANGLEOFFSET', 'DEFAULT_ANGLEORIENT', 'DEFAULT_MODE', 'START_ORIENTATION', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_angleOffset', '_angleOrient', '_cc', '_clear', '_clearstamp', '_color', '_colorstr', '_creatingPoly', '_degreesPerAU', '_delay', '_drawing', '_drawturtle', '_fillcolor', '_fillitem', '_fillpath', '_fullcircle', '_getshapepoly', '_go', '_goto', '_hidden_from_screen', '_mode', '_newLine', '_orient', '_outlinewidth', '_pencolor', '_pensize', '_poly', '_polytrafo', '_position', '_reset', '_resizemode', '_rotate', '_setDegreesPerAU', '_setmode', '_shapetrafo', '_shearfactor', '_shown', '_speed', '_stretchfactor', '_tilt', '_tracer', '_undo', '_undobuffersize', '_undogoto', '_update', '_update_data', '_write', 'back', 'backward', 'begin_fill', 'begin_poly', 'bk', 'circle', 'clear', 'clearstamp', 'clearstamps', 'clone', 'color', 'currentLine', 'currentLineItem', 'degrees', 'distance', 'dot', 'down', 'drawingLineItem', 'end_fill', 'end_poly', 'fd', 'fillcolor', 'filling', 'forward', 'get_poly', 'get_shapepoly', 'getpen', 'getscreen', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'isdown', 'isvisible', 'items', 'left', 'lt', 'onclick', 'ondrag', 'onrelease', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position', 'pu', 'radians', 'reset', 'resizemode', 'right', 'rt', 'screen', 'screens', 'seth', 'setheading', 'setpos', 'setposition', 'settiltangle', 'setundobuffer', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle', 'speed', 'st', 'stamp', 'stampItems', 'tilt', 'tiltangle', 'towards', 'turtle', 'turtlesize', 'undo', 'undobuffer', 'undobufferentries', 'up', 'width', 'write', 'xcor', 'ycor']
canvas = window.FindElement('_canvas_').TKCanvas
t = tt.RawTurtle(canvas)
s = t.getscreen()

screenCmdList = ['_RUNNING','_bgcolor','_bgpic','_bgpicname','_bgpics','_blankimage','_colormode','_createimage','_createline','_createpoly','_delayvalue','_delete','_drawimage','_drawline','_drawpoly','_image','_incrementudc','_iscolorstring','_keys','_listen','_onclick','_ondrag','_onkeypress','_onkeyrelease','_onrelease','_onscreenclick','_ontimer','_pointlist','_rescale','_resize','_setbgpic','_setscrollregion','_shapes','_tracing','_turtles','_type','_updatecounter','_window_size','addshape','bgcolor','bgpic','canvheight','canvwidth','clearscreen','colormode','cv','delay','getcanvas','getshapes','listen','mainloop','mode','numinput','onkey','onkeypress','onkeyrelease','onscreenclick','ontimer','register_shape','resetscreen','screensize','setworldcoordinates','textinput','tracer','turtles','update','window_height','window_width','xscale','yscale']
turtleCmdList = ['onclick','reset','clear','DEFAULT_ANGLEOFFSET','DEFAULT_ANGLEORIENT','DEFAULT_MODE','START_ORIENTATION','_angleOffset','_angleOrient','_cc','_clear','_clearstamp','_creatingPoly','_degreesPerAU','_drawing','_drawturtle','_fillcolor','_fillitem','_fillpath','_fullcircle','_getshapepoly','_go','_goto','_hidden_from_screen','_newLine','_orient','_outlinewidth','_pencolor','_pensize','_poly','_polytrafo','_position','_reset','_resizemode','_rotate','_setDegreesPerAU','_setmode','_shapetrafo','_shearfactor','_shown','_speed','_stretchfactor','_tilt','_tracer','_undo','_undobuffersize','_undogoto','_update_data','back','backward','begin_fill','begin_poly','bk','circle','clearstamp','clearstamps','clone','color','currentLine','currentLineItem','degrees','distance','dot','down','drawingLineItem','end_fill','end_poly','fd','fillcolor','filling','forward','get_poly','get_shapepoly','getpen','getscreen','getturtle','goto','heading','hideturtle','home','ht','isdown','isvisible','items','left','lt','ondrag','onrelease','pd','pen','pencolor','pendown','pensize','penup','pos','position','pu','radians','resizemode','right','rt','screen','screens','seth','setheading','setpos','setposition','settiltangle','setundobuffer','setx','sety','shape','shapesize','shapetransform','shearfactor','showturtle','speed','st','stamp','stampItems','tilt','tiltangle','towards','turtle','turtlesize','undo','undobuffer','undobufferentries','up','width','write','xcor','ycor']
# 'onclick','reset','clear',这三个命令在画布中也存在，本程序只放入小海龟绘图命令中
# cf = []
# for item in screenCmdLst:
#     if item in turtleCmdLst:
#         cf.append(item)
#         # print(item)

# print('[',end="")
# for item in turtleCmdLst:
#     if item not in cf:
#         print("'",item,"',",end="",sep="")
# print(']')

while True:
    event, values = window.Read()
    # print(event, values)
    if event is None or event == "退出":
        break

    if event is "清空当前历史":
        window.FindElement('_history_').Update(["命令历史："])

    if event is "导出为psy文件":
        f = filedialog.asksaveasfile(mode='w', filetypes=(("小海龟脚本文件","*.psy"),), initialdir ='.') # show the 'get file' dialog box
        tmphistory = window.FindElement('_history_').GetListValues()
        if f is not None:            
            f.write("t.reset()\n" + "\n".join(tmphistory[1:]))
        
    if event == "_history_":
        # print(values['_history_'])
        if "命令历史" not in values['_history_'][0]:
            tmpcmd = values['_history_'][0]
            window.FindElement('_command_').Update(tmpcmd[2:])
            
    if event == "\r" or event is "运行":
        tmpcmd = values["_command_"].strip()
        # tmpcmdTs = values["_commandTs_"].strip()
        if tmpcmd != "":
            try:
                if "(" not in tmpcmd:
                    tmpcmd = tmpcmd.split(' ')
                    while '' in tmpcmd:
                        tmpcmd.remove('')
                    curcmd = tmpcmd[0] + "("
                    # print(tmpcmd, curcmd, "======, 1")
                    curcmd += ",".join(tmpcmd[1:]) + ")"
                    tmpcmd = curcmd
                    # print(tmpcmd, curcmd, "~~~~~~~~~~~~2")
                    # print(eval(tmpcmd))
                if tmpcmd[:tmpcmd.index("(")] in turtleCmdList:
                    tmpcmd = "t."+tmpcmd
                elif tmpcmd[:tmpcmd.index("(")] in screenCmdList:
                    tmpcmd = "s."+tmpcmd
                
                print(tmpcmd)
                status = eval(tmpcmd)
                print(status)

                tmphistory = window.FindElement('_history_').GetListValues()
                tmphistory.append(tmpcmd)
                window.FindElement('_history_').Update(tmphistory)
                window.FindElement('_command_').Update("")
                if status is None:
                    window.FindElement('_status_').Update("执行成功")
                else:
                    window.FindElement('_status_').Update(str(status))
            except:
                window.FindElement('_status_').Update("无此命令或命令需要带参数")

        # if tmpcmdTs != "":
        #     try:
        #         if "(" not in tmpcmdTs:
        #             tmpcmdTs = tmpcmdTs.split(' ')
        #             curcmd = tmpcmdTs[0] + "("
        #             # print(tmpcmdTs, curcmd, "======, 1")
        #             curcmd += ",".join(tmpcmdTs[1:]) + ")"
        #             tmpcmdTs = curcmd
        #             # print(tmpcmdTs, curcmd, "~~~~~~~~~~~~2")
        #             # print(eval(tmpcmdTs))
        #         status = eval("s."+tmpcmdTs)
        #         # print(status)
        #         tmphistory = window.FindElement('_history_').GetListValues()
        #         tmphistory.append("s."+ tmpcmdTs)
        #         window.FindElement('_history_').Update(tmphistory)
        #         window.FindElement('_commandTs_').Update("")
        #         if status is None:
        #             window.FindElement('_status_').Update("执行成功")
        #         else:
        #             window.FindElement('_status_').Update(str(status))
        #     except:
        #         window.FindElement('_status_').Update("无此命令")
                # pass
    if event is "执行文件":
        file_name = filedialog.askopenfilename(filetypes=(("小海龟脚本文件","*.psy"),), initialdir ='.') # show the 'get file' dialog box
        # print(len(file_name), type(file_name))
        strcmd = "from turtle import *\n"
        if len(file_name)==0:
            pass
        else:
            with open(file_name, encoding='UTF-8') as f:
                strcmd += f.read()                        
            try:
                exec(strcmd, {'t':t, 's':s}, {})
                window.FindElement('_status_').Update("脚本执行成功！")
            except Exception as e:
                window.FindElement('_status_').Update(e)

window.Close()