# import PySimpleGUI as sg 
import PySimpleGUI as sg 
import turtle as tt 
import tkinter.font
from tkinter import filedialog

layout = [[sg.Canvas(size=(500, 500), background_color='white', key='canvas'),sg.Multiline(size=(100//7, 20//7), key='history', font=('宋体', 12))],      
                 [sg.InputText(focus=True,do_not_clear=False, size=(510//10, 20//7), key='command', font=('宋体', 16)),], 
                 [sg.Button("运行", font=('宋体', 16)), sg.Button("退出", font=('宋体', 16)), sg.T(" "*96), sg.Button("执行文件", font=('宋体', 16))]]      

window = sg.Window('小海龟绘图').Layout(layout).Finalize()    

historywindow = window.FindElement('history').TKText
def doubleClickSelToCommand(event):
    # actual_callback(event) # this will select the word
    w = historywindow.selection_get()
    window.FindElement('command').Update(w)
    print(w)
historywindow.bind("<Double-Button-1>", lambda e: historywindow.after(2, doubleClickSelToCommand, e)) # wait 2 ms before running callback


commandwindow = window.FindElement('command').TKEntry
def enterKeyRun(event):
    tmpcmd = commandwindow.get().strip()
    if tmpcmd != "":
        try:
            tmpcmd = "t." + tmpcmd
            eval(tmpcmd)
            # print(1)
        except:
            pass
            # sg.MsgBox("不可识别的!")
        commandwindow.delete(0, 'end')
commandwindow.bind('<Return>',enterKeyRun)

# charpixels = tkinter.font.Font().measure('A')
window.FindElement('history').Update("命令历史:")
window.FindElement('history').Update(disabled=True)


canvas = window.FindElement('canvas').TKCanvas
t = tt.RawTurtle(canvas)
t.pencolor("#ff0000") # Red

t.pendown() # Regarding one of the comments
t.fd(100)

while True:
    event, values = window.Read()
    print(event, '===', values)
    if event is None or event == "退出":
        break
    if event is '运行':
        tmpcmd = values["command"].strip()
        if tmpcmd != "":
            try:
                eval("t."+tmpcmd)
                tmphistory = values['history'] + tmpcmd
                # historywindow.Update(tmphistory)
                # print(tmphistory, '----')
                window.FindElement('history').Update(disabled=False)  
                window.FindElement('history').Update(tmphistory)
                window.FindElement('history').Update(disabled=True)
            except:
                print(tmpcmd)
                pass
    if event is "执行文件":
        # filedialog.askopenfilename(initialdir ='.')
        file_name = filedialog.askopenfilename(filetypes=(("小海龟角本文件","*.psy"),), initialdir ='.') # show the 'get file' dialog box
        print(len(file_name), type(file_name))
        strcmd = "from turtle import *\n"
        if len(file_name)==0:
            pass
        else:
            with open(file_name) as f:
                strcmd += f.read()
            print(strcmd)
            exec(strcmd, {}, {'t':t})
        # print(t, type(t))
        # exec("print(t, type(t),'==')", {}, {"t":t})

        # print(values["command"], type(values))
        
    # elif event is 'Red':
    #     window.FindElement('canvas').TKCanvas.itemconfig(cir, fill = "Red")


# event, values = window.Read()    
window.Close()

# text_input = values[0]    
# print(values)
