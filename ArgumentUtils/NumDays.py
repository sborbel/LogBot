from datetime import datetime, date, time

#Get current date



def filterByNumDays(logEntryTouples, startDatetime):
    poping = True

   

    while poping:
        #print(len(logEntryTouples) > 0)
        if(len(logEntryTouples) > 0):
            #print(str(logEntryTouples[0][0]) + " : " + str(startDatetime))
            #print(logEntryTouples[0][0] < startDatetime)
            if(logEntryTouples[0][0] < startDatetime):
                """ print(logEntryTouples[0])
                print(logEntryTouples[0][0])
                print(startDate) """
                logEntryTouples.pop(0)
            else:
                poping = False
        else:
            poping = False
    
    return logEntryTouples

