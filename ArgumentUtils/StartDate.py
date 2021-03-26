from datetime import datetime, date, time

#Get current date



def filterByStartDate(logEntryTouples, rawStartDate):
    splitStart = rawStartDate.split('-')
    startDate = datetime(int(splitStart[0]), int(splitStart[1]), int(splitStart[2]))
    poping = True

   

    while poping:

        if(logEntryTouples[0][0] < startDate):
            """ print(logEntryTouples[0])
            print(logEntryTouples[0][0])
            print(startDate) """
            logEntryTouples.pop(0)
        else:
            poping = False
    return logEntryTouples



    

