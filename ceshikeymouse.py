import PySimpleGUI as sg

# Recipe for getting keys, one at a time as they are released  
# If want to use the space bar, then be sure and disable the "default focus"

with sg.Window("Keyboard Test", return_keyboard_events=True, use_default_focus=False) as window:  
    text_elem = sg.Text("", size=(18, 1))  
    layout = [[sg.Text("Press a key or scroll mouse")],  
              [text_elem],  
              [sg.Button("OK")]]

    window.Layout(layout)  
    # ---===--- Loop taking in user input --- #  
while True:  
    event, value = window.Read()
    print(event)

    if event == "OK"  or event is None:  
        print(event, "exiting")  
        break  
    text_elem.Update(event)