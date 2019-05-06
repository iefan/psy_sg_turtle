# import PySimpleGUI as sg 
import PySimpleGUI as sg 
import turtle as tt 
import tkinter.font
from tkinter import filedialog
import tkinter
import platform 

if platform.system() == "Linux":
    size_history = (15, 25)
    size_command = (67, 3)
    size_blank = 86
    size_status = (40, 1)
elif platform.system() == "Windows":
    size_history = (18, 29)
    size_command = (82, 3)
    size_blank = 59
    size_status = (40, 1)


outputmenu = ['',['导出为psy文件']]
layout = [[sg.Canvas(size=(500, 500), background_color='white', key='_canvas_'),\
            sg.Listbox(values=["命令历史："], size=size_history, key='_history_', bind_return_key=True,right_click_menu=outputmenu)],
            [sg.InputText(focus=True, size=size_command, key='_command_',),], 
            [sg.Button("运行",), sg.Button("退出",), sg.T(" "*size_blank), sg.Button("执行文件",)],
            [sg.Text("__"*42)],
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


canvas = window.FindElement('_canvas_').TKCanvas
t = tt.RawTurtle(canvas)

while True:
    event, values = window.Read()
    # print(event, values)
    if event is None or event == "退出":
        break
    
    if event is "导出为psy文件":
        f = filedialog.asksaveasfile(mode='w', filetypes=(("小海龟脚本文件","*.psy"),), initialdir ='.') # show the 'get file' dialog box
        tmphistory = window.FindElement('_history_').GetListValues()
        if f is not None:            
            f.write("t.reset()\nt." + "\nt.".join(tmphistory[1:]))
        
    if event == "_history_":
        if "命令历史" not in values['_history_'][0]:
            window.FindElement('_command_').Update(values['_history_'][0])
        
    if event == "\r" or event is "运行":
        tmpcmd = values["_command_"].strip()
        if tmpcmd != "":
            try:
                if "(" not in tmpcmd:
                    tmpcmd = tmpcmd.split(' ')
                    curcmd = tmpcmd[0] + "("
                    # print(tmpcmd, curcmd, "======, 1")
                    curcmd += ",".join(tmpcmd[1:]) + ")"
                    tmpcmd = curcmd
                    # print(tmpcmd, curcmd, "~~~~~~~~~~~~2")
                status = eval("t."+tmpcmd)
                # print(status)
                tmphistory = window.FindElement('_history_').GetListValues()
                tmphistory.append(tmpcmd)
                window.FindElement('_history_').Update(tmphistory)
                window.FindElement('_command_').Update("")
                if status is None:
                    window.FindElement('_status_').Update("执行成功")
                else:
                    window.FindElement('_status_').Update(str(status))
            except:
                window.FindElement('_status_').Update("无此命令")
                # pass
    if event is "执行文件":
        file_name = filedialog.askopenfilename(filetypes=(("小海龟脚本文件","*.psy"),), initialdir ='.') # show the 'get file' dialog box
        # print(len(file_name), type(file_name))
        strcmd = "from turtle import *\n"
        if len(file_name)==0:
            pass
        else:
            with open(file_name) as f:
                strcmd += f.read()
            exec(strcmd, {}, {'t':t})

window.Close()