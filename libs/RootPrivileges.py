import sys
import subprocess
import json

import libs.JSONHandler as jsonhdlr

from colorama import Fore, Back

defaultForeColor = Fore.WHITE
defaultBackColor = Back.BLACK


def elevatePrivileges(MainDirPath: str):
    try:
        mainPath = MainDirPath

        password: str = jsonhdlr.readJSONValue(mainPath, "RootAuth", "RootAuthValue")

        rootCommand = f"echo {password} | sudo -S whoami"
        outSudo = subprocess.Popen(
            rootCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        ) # executing an autonomous root login using the stored password and check if logs in

        stdout, stderr = outSudo.communicate() # read the standard output and standard error from the previous process

        if ("root".encode() in stdout): # if the result of whoami command output is 'root'
            print("")
            print(
                Back.GREEN + "Root privileges obtained successfully." + defaultBackColor
            )
        else:
            print("")
            print(Back.RED + "ERROR: Sorry, can't obtain root privileges." + defaultBackColor)
            print(
                Back.RED
                + "Try changing the 'RootAuthValue' value in 'settings.json'."
                + defaultBackColor
            )

            sys.exit()
    except Exception:
        print("")
        print(Back.RED + "ERROR: Sorry, can't obtain root privileges." + defaultBackColor)
        print(
            Back.RED
            + "Try changing the 'RootAuthValue' value in 'settings.json'."
            + defaultBackColor
        )

        sys.exit()

def storePassword(MainDirPath: str):
    tryagainOperation: bool = True

    while (tryagainOperation == True): # while loop for retry the user input and all operation
        print("")
        getPassword: str = input("Enter the root password. (It will only be used for the privileges required for the tool to work!): >>") # getting the root password from user input
        print("")
        
        mainPath = MainDirPath

        try:
            jsonhdlr.updateJSONValue(mainPath, "RootAuth", "RootAuthValue", getPassword)

            tryagainOperation = False

            print("")
            print(Fore.GREEN + "Password stored successfully." + defaultForeColor)
        except Exception:
            print("")
            print(
                Fore.RED
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