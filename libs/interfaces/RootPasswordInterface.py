import os
import sys
fileFolder: str = os.path.dirname(os.path.abspath(__file__))
PYTHONPATHFolder: str = fileFolder.replace('/interfaces', '')
sys.path.append(PYTHONPATHFolder)

from classes.GlobalVariables import *
from classes.CLIHandler import *
from classes.JSONHandler import *

def loadRootPasswordInterface():
    currentPassword = readJSONValue("RootAuth", "RootAuthValue")
    
    os.system("clear") # cls to clear
    print(foreBlue + f"Password currently saved: {currentPassword}" + defaultForeColor)
    print("")
    print(foreBlue + "Enter new root password below:" + defaultForeColor)
    
    newPassword = input(foreBlue + ">>" + defaultForeColor + "")
    if (newPassword == ""):
        tryAgainOption: bool = True
        while (tryAgainOption == True):
            print("")
            rootPasswordOption = input(foreBlue + "So, did you set up the root user without a password? ([Y]/[N]): >>" + defaultForeColor + "")
            if (
                rootPasswordOption == "Y"
                or rootPasswordOption == "y"
                or rootPasswordOption == "YES"
                or rootPasswordOption == "yes"
                or rootPasswordOption == "Yes"
            ):
                tryAgainOption = False
                
                print("")
                print(foreGreen + "You are a risk taker, I like it! Saving the password as an empty field." + defaultForeColor)
                updateJSONValue("RootAuth", "RootAuthValue", newPassword)
            elif (
                rootPasswordOption == "N"
                or rootPasswordOption == "n"
                or rootPasswordOption == "NO"
                or rootPasswordOption == "no"
                or rootPasswordOption == "No"
            ):
                tryAgainOption = False

                print("")
                print(foreGreen + "Ok then! Undo the root password edit." + defaultForeColor)
                settingsCLI()
            else:
                tryAgainOption = True
    else:
        updateJSONValue("RootAuth", "RootAuthValue", newPassword)
        print("")
        print(backGreen + "New password saved successfully!" + defaultBackColor)