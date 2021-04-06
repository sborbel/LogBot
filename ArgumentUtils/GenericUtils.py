from datetime import datetime, date, time

def getMonthFromShortName(shortName):
    if(shortName == "Jan"):
        return 1
    elif(shortName == "Feb"):
        return 2
    elif(shortName == "Mar"):
        return 3
    elif(shortName == "Apr"):
        return 4
    elif(shortName == "May"):
        return 5
    elif(shortName == "Jun"):
        return 6
    elif(shortName == "Jul"):
        return 7
    elif(shortName == "Aug"):
        return 8
    elif(shortName == "Sep"):
        return 9
    elif(shortName == "Oct"):
        return 10
    elif(shortName == "Nov"):
        return 11
    elif(shortName == "Dec"):
        return 12
    else:
        return 0
    
def checkDate(date):
    splitDate = date.split('-')
    year = int(splitDate[0])
    month = int(splitDate[1])
    day = int(splitDate[2])

    try:
        datetime(year, month, day)
    except ValueError:
        print("Error: Invalid date of " + date + " given - Exiting")
        exit(0)


def formatDate(dateType, array, filename):
    today = date.today()
    currMonth = today.month
    currYear = today.year
    DatetimeWithLogTouple = []
    if(dateType == 1):
        for line in array:
            splitLine = line.split()
            monthShortName = splitLine[0]
            day = int(splitLine[1])
            hour = splitLine[2].split(':')[0]
            minute = splitLine[2].split(':')[1]
            sec = splitLine[2].split(':')[2]
            month = getMonthFromShortName(monthShortName)
            if(month > currMonth):
                year = currYear - 1
            else:
                year = currYear
            logDatetime = datetime(year, month, day, int(hour), int(minute), int(sec))
            splitLine.pop(0)
            splitLine.pop(0)
            splitLine.pop(0)

            DatetimeWithLogTouple.append((logDatetime, " ".join(splitLine), filename))
        return DatetimeWithLogTouple
            
            
        

def consolidateLogsByCategory(cats):
    categories = cats.split(",")
    formattedLines = []
    delimeter = "#$"
    with open('logFiles.txt', 'r') as logLocations:
        lines = logLocations.readlines()
    logLocations.close()
    for logFile in lines:
        logCat = logFile.split(delimeter)[2].strip()
        if logCat in categories:
            with open(logFile.split(delimeter)[0], 'r') as currentLog:
                logLines = currentLog.readlines()
            dateType = int(logFile.split(delimeter)[1])
            formattedLines.extend(formatDate(dateType, logLines, logFile.split(delimeter)[0]))

    result = sorted(formattedLines, key=lambda x: x[0])
    
    
    return result

def consolidateLogs():
    formattedLines = []
    delimeter = "#$"
    with open('logFiles.txt', 'r') as logLocations:
        lines = logLocations.readlines()
    logLocations.close()
    for logFile in lines:
        with open(logFile.split(delimeter)[0], 'r') as currentLog:
            logLines = currentLog.readlines()
        dateType = int(logFile.split(delimeter)[1])
        formattedLines.extend(formatDate(dateType, logLines, logFile.split(delimeter)[0]))

    result = sorted(formattedLines, key=lambda x: x[0])
    
    
    return result




#consolidateLogs()