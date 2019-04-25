# import PySimpleGUI as sg 
import PySimpleGUI as sg 
import turtle as tt 

layout = [[sg.Canvas(size=(500, 500), background_color='white', key='canvas'),],      
                 [sg.InputText(key='command')],      
                 [sg.Button("运行"), sg.Button("退出")]]      

window = sg.Window('Window Title').Layout(layout).Finalize()    

canvas = window.FindElement('canvas').TKCanvas
t = tt.RawTurtle(canvas)
t.pencolor("#ff0000") # Red

# t.penup()   # Regarding one of the comments
t.pendown() # Regarding one of the comments
t.fd(100)
t.pu()

while True:
    event, values = window.Read()
    if event is None or event == "退出":
        break
    if event is '运行':
        tmpcmd = values["command"].strip()
        if tmpcmd != "":
            try:
                eval("t."+tmpcmd)
            except:
                pass

        # print(values["command"], type(values))
        
    # elif event is 'Red':
    #     window.FindElement('canvas').TKCanvas.itemconfig(cir, fill = "Red")


# event, values = window.Read()    
window.Close()

# text_input = values[0]    
# print(values)