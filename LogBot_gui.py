#import LogBot.py


# hello_psg.py

import PySimpleGUI as sg

layout = [[sg.Text("Simplifies the log diagnosis process!")],
            [sg.Text("whatever you type here will be displayed when you click SUBMIT:")], [sg.Input(key='-INPUT-')],
            [sg.Text("End Date:")], [sg.Input()],
            [sg.Text("Number of Days:")], [sg.Input()],
            [sg.Text("Number of Hours:")], [sg.Input()],
            [sg.Text("Categories:")], [sg.Input()],
            [sg.Text("Pattern:")], [sg.Input()],
            [sg.Button("SUBMIT")], [sg.Button("QUIT")],
            [sg.Text(size=(40,2), key='-OUTPUT-')]
        ]

# Create the window
window = sg.Window("LogBot", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "QUIT":
        window.close()
    if event == "SUBMIT" or event == sg.WIN_CLOSED:
         window['-OUTPUT-'].update('Look at me: ' + values['-INPUT-'] + '\nWOW this text is fucking yellow!', text_color='yellow')

window.close()