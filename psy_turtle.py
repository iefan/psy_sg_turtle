# import PySimpleGUI as sg 
import PySimpleGUI as sg 
import turtle as tt 
import tkinter.font
from tkinter import filedialog
import tkinter


# menuHistory = ["导出menu", ["导出",]]
layout = [[sg.Canvas(size=(500, 500), background_color='white', key='_canvas_'),\
            sg.Listbox(values=["命令历史："], size=(15, 29), key='_history_', bind_return_key=True,)],
                 [sg.InputText(focus=True, size=(67, 3), key='_command_',),], 
                 [sg.Button("运行",), sg.Button("退出",), sg.T(" "*55), sg.Button("执行文件",)],
                 [sg.Text("__"*40)],
                 [sg.Text("运行状态显示～～～",size=(40, 3), font=('宋体', 10), key="_status_")],
                 ]      

window = sg.Window('小海龟绘图', return_keyboard_events=True, font=('宋体', 12)).Layout(layout).Finalize()    

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
    if event is None or event == "退出":
        break
    
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
                window.FindElement('_status_').Update("无此命令")
                # pass
    if event is "执行文件":
        file_name = filedialog.askopenfilename(filetypes=(("小海龟脚本文件","*.psy"),), initialdir ='.') # show the 'get file' dialog box
        print(len(file_name), type(file_name))
        strcmd = "from turtle import *\n"
        if len(file_name)==0:
            pass
        else:
            with open(file_name) as f:
                strcmd += f.read()
            exec(strcmd, {}, {'t':t})

window.Close()