from datetime import datetime, date, time

#Get current date



def filterByEndDate(logEntryTouples, rawStartDate):
    splitStart = rawStartDate.split('-')
    endDate = datetime(int(splitStart[0]), int(splitStart[1]), int(splitStart[2])+1)
    poping = True

   

    while poping:

        if(logEntryTouples[len(logEntryTouples)-1][0] > endDate):
            """ print(logEntryTouples[0])
            print(logEntryTouples[0][0])
            print(startDate) """
            logEntryTouples.pop(len(logEntryTouples)-1)
        else:
            poping = False
    return logEntryTouples



    

