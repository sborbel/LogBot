import sys
import HelpPages.MainHelp as MainHelp
#for arg in sys.argv[1:]:
    #print(arg)
#def printHelpMessage():
    #print("This is the help message.")


args = sys.argv
numArgs = len(args)

if(numArgs > 1):
    if(args[1] == "help"):
        MainHelp.printHelpMessage()
    
    

