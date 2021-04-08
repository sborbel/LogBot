#import LogBot.py


# hello_psg.py



import PySimpleGUI as sg

from textwrap import wrap
from datetime import datetime, date, time, timedelta
import ArgumentUtils.GenericUtils as GenericUtils
import ArgumentUtils.StartDate as StartDate
import ArgumentUtils.EndDate as EndDate
import ArgumentUtils.NumDays as NumDays
import ArgumentUtils.NumHours as NumHours
import ArgumentUtils.Pattern as Pattern



Categories = ["Auth", "Messages"]

def CommaToList(CSL):
    myList = CSL.split(",")
    for cat in myList:
        if not cat in Categories:
            print("Error: Category \"" + cat + "\" is not supported. Supported options are: " + ', '.join(Categories))
            exit(0)
    return myList



layout = [[sg.Text("Simplifies the log diagnosis process!")],[sg.Text("Start Date (YYYY-MM-DD):")], [sg.Input(key='startdate')],
            [sg.CalendarButton('Choose Start Date', target='startdate', key='startdate2')],
            [sg.Text("End Date (YYYY-MM-DD):")], [sg.Input(key='enddate')],
            [sg.CalendarButton('Choose End Date', target='enddate', key='enddate2')],
            [sg.Text("Number of Days:")], [sg.Input(key='numdays')],
            [sg.Text("Number of Hours:")], [sg.Input(key='numhours')],
            [sg.Text("Categories:")], [sg.Input(key='categories')],
            [sg.Text("Pattern:")], [sg.Input(key='pattern')],
            [sg.Button("SUBMIT")], [sg.Button("QUIT")],
            [sg.Text(size=(40,2), key='-OUTPUT-')],
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
        #window['-OUTPUT-'].update('Look at me: ' + values['-INPUT-'] + '\nWOW this text is fucking yellow!', text_color='yellow')

        # Make sure that if either/both the -s and/or -e flags are given, the -d and -H flags are not present. Also
        # if the -H flag is present, the -d flag must not be present and vice versa. - TO-DO

        if(values['categories'] != ''):
            categories = CommaToList(values['categories'])
            #Consolidate by category - TO-DO
            logList = GenericUtils.consolidateLogsByCategory(values['categories'])
        else:
            #Consolidate all log files
            logList = GenericUtils.consolidateLogs()

        if(values['startdate'] != ''):
            #Check if date is valid
            GenericUtils.checkDate(values['startdate'])
        
            start = wrap(values['startdate'], 10)
            logList = StartDate.filterByStartDate(logList, start[0])
        if(values['enddate'] != ''):
            #Check if date is valid
            GenericUtils.checkDate(values['enddate'])

            end = wrap(values['enddate'], 10)
            EndDate.filterByEndDate(logList, end[0])
        if(values['numdays'] != ''):
            days = int(values['numdays'])
            today = datetime.today()
            date = today - timedelta(days=days)
            logList = NumDays.filterByNumDays(logList, date)
        if(values['numhours'] != ''):
            hours = int(values['numhours'])
            today = datetime.today()
            date = today - timedelta(hours=hours)
            logList = NumHours.filterByNumHours(logList, date)
        if(values['pattern'] != ''):
            patternRaw = values['pattern']
        
            logList = Pattern.filterByPattern(logList, patternRaw)

        #Finalize Results

        with open('res.txt', 'w') as results:
            for l in logList:
                #window['textbox'].update((l[0].strftime("%b %d %Y %H:%M:%S") + " " + l[2] + " " + l[1] + '\n') + values['textbox'])
                results.write(l[0].strftime("%b %d %Y %H:%M:%S") + " " + l[2] + " " + l[1] + '\n')
    
        window['-OUTPUT-'].update("Completed successfully. Found " + str(len(logList)) +  " result(s). Output located in res.txt", text_color='red')

        # NEW POPUP WINDOW THAT SHOWS LIST OF OUTPUT LOGS WITH MANUAL SAVE BUTTON - TO DO
        #layout2 = [[sg.Text("RESULTS:")],
        #    [sg.Text("whatever you type here will be displayed when you click SUBMIT:")], [sg.Input(key='-INPUT-')],
        #    [sg.Multiline(size=(30, 5), key='textbox')]
        #]

        # Create the window
        #window2 = sg.Window("Results", layout2)

        # Create an event loop
        #while True:
        #    event, values = window2.read()
        #    # End program if user closes window or
        #    # presses the OK button
        #    if event == "QUIT":
        #        window2.close()
        #    if event == sg.WIN_CLOSED or event == 'Exit':
        #        break
        #window2.close()

window.close()