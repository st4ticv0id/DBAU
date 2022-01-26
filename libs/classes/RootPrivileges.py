import os
import sys
fileFolder: str = os.path.dirname(os.path.abspath(__file__))
PYTHONPATHFolder: str = fileFolder.replace('/classes', '')
sys.path.append(PYTHONPATHFolder)
import subprocess

from classes.JSONHandler import *
from classes.GlobalVariables import *


def elevatePrivileges():
    try:
        mainPath = getMainPath()

        password: str = readJSONValue("RootAuth", "RootAuthValue")

        rootCommand = f"echo {password} | sudo -S whoami"
        outSudo = subprocess.Popen(
            rootCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        ) # executing an autonomous root login using the stored password and check if logs in

        stdout, stderr = outSudo.communicate() # read the standard output and standard error from the previous process

        if ("root".encode() in stdout): # if the result of whoami command output is 'root'
            print("")
            print(
                backGreen + "Root privileges obtained successfully." + defaultBackColor
            )
        else:
            print("")
            print(backRed + "ERROR: Sorry, can't obtain root privileges." + defaultBackColor)
            print(
                backRed
                + "Try changing the 'RootAuthValue' value in 'settings.json'."
                + defaultBackColor
            )

            sys.exit()
    except Exception:
        print("")
        print(backRed + "ERROR: Sorry, can't obtain root privileges." + defaultBackColor)
        print(
            backRed
            + "Try changing the 'RootAuthValue' value in 'settings.json'."
            + defaultBackColor
        )

        sys.exit()

def storePassword():
    tryagainOperation: bool = True

    while (tryagainOperation == True): # while loop for retry the user input and all operation
        print("")
        getPassword: str = input("Enter the root password. (It will only be used for the privileges required for the tool to work!): >>") # getting the root password from user input
        print("")
        
        mainPath = getMainPath()

        try:
            updateJSONValue("RootAuth", "RootAuthValue", getPassword)

            tryagainOperation = False

            print("")
            print(foreGreen + "Password stored successfully." + defaultForeColor)
        except Exception:
            print("")
            print(
                foreRed
                + "ERROR: An error is occured while storing password."
                + defaultForeColor
            )

            correctAnswer = False
            while (correctAnswer == False):
                print("")
                retryq = input("Do you want to try again? (Y/N): >>")
                if (
                    retryq == "Y"
                    or retryq == "y"
                    or retryq == "YES"
                    or retryq == "yes"
                    or retryq == "Yes"
                ):
                    tryagainOperation = True
                elif (
                    retryq == "N"
                    or retryq == "n"
                    or retryq == "NO"
                    or retryq == "no"
                    or retryq == "No"
                ):
                    tryagainOperation = False

                    sys.exit()
                else:
                    correctAnswer = False