import PySimpleGUI as sg

with sg.Window("Realtime Keyboard Test", return_keyboard_events=True, use_default_focus=False) as window:  
    layout = [[sg.Text("Hold down a key")],  
              [sg.Button("OK")]]

    window.Layout(layout)

    while True:  
        event, value = window.Read(timeout=0)  
        # print(event, value)
        if event == "OK"  or event is None:  
            print(event, value, "exiting")  
            break  
        if event != sg.TIMEOUT_KEY:  
            print(event)