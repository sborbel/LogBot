import re


def filterByPattern(logEntryTouples, searchStr):
    newList = []
    for ent in logEntryTouples:
        if re.search(searchStr, ent[1]) != None:
            newList.append(ent)
    return newList

      