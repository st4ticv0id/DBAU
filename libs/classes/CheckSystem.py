import os
import sys
fileFolder: str = os.path.dirname(os.path.abspath(__file__))
PYTHONPATHFolder: str = fileFolder.replace('/classes', '')
sys.path.append(PYTHONPATHFolder)
import distro
import subprocess

from classes.GlobalVariables import *
from classes.JSONHandler import *

def checkOS():
    try:
        if sys.platform.startswith("linux") or sys.platform.startswith("linux2"): # check if system is Linux or Linux2
            exactDistro = distro.id() # check the specific distribution name
            distroResult = f"{sys.platform}|{exactDistro}"

        elif sys.platform.startswith("aix"): # check if system is IBM AIX
            distroResult = "aix"

        elif (
            sys.platform.startswith("win32") # check if system is Windows NT
            or sys.platform.startswith("cygwin") # check if system is Windows/cygwin
            or sys.platform.startswith("msys") # check if system is Windows/msys
        ):
            distroResult = "win32/cygwin/msys"

        elif sys.platform.startswith("os2") or sys.platform.startswith("os2emx"): # check if system is IBM-Microsoft OS/2 or OS/2EMX
            distroResult = "os2/os2emx"

        elif sys.platform.startswith("riscos"): # check if system is riscOS
            distroResult = "riscos"

        elif sys.platform.startswith("atheos"): # check if system is atheOS
            distroResult = "atheos"

        elif sys.platform.startswith("freebsd") or sys.platform.startswith("openbsd"): # check if system is freeBSD or openBSD
            distroResult = "freebsd/openbsd"

        elif sys.platform.startswith("darwin"): # check if system is MacOS
            distroResult = "darwin"
        else:
            distroResult = "unknown" # this will throw an error

        if "linux" in distroResult and "|" in distroResult:
            splitDistro = distroResult.split("|")[1]

            if "debian" == splitDistro or "ubuntu" == splitDistro or "linuxmint" == splitDistro: # check throught various options if the system is known by the 'distro' module
                isFirstLaunch: bool = readJSONValue("FirstLaunch", "FirstLaunchValue")
                if (isFirstLaunch == True):
                    print(
                        backGreen
                        + "Compatible operating system. Proceeding..."
                        + defaultBackColor
                    )
                    print("")
            else:
                correctAnswer = False
                while correctAnswer == False:
                    print("")
                    retryq = input("I cannot recognize if your system is using apt package manager. Does the os use it? (Y/N): >>") # if not ask user if the system uses apt package manager
                    if (
                        retryq == "Y"
                        or retryq == "y"
                        or retryq == "YES"
                        or retryq == "yes"
                        or retryq == "Yes"
                    ):
                        upgradeCommand = "sudo apt-get dist-upgrade -y"
                        outUpgrade = subprocess.Popen(upgradeCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # running apt-get dist-upgrade command in a new process

                        stdout,stderr = outUpgrade.communicate() # read the standard output and standard error from the previous process
                        errorGeneric = ""

                        print(
                            backGreen
                            + "Ok then! Compatible operating system. Proceeding..."
                            + defaultBackColor
                        )
                    elif (
                        retryq == "N"
                        or retryq == "n"
                        or retryq == "NO"
                        or retryq == "no"
                        or retryq == "No"
                    ):
                        print(
                            backRed
                            + "Sorry! Incompatible operating system. Quitting..."
                            + defaultBackColor
                        )

                        sys.exit()
                    else:
                        correctAnswer = False
        elif ("linux" not in distroResult):
            print(
                backRed
                + "Incompatible operating system. Quitting..."
                + defaultBackColor
            )

            sys.exit()
        else:
            error = backRed + "ERROR: Unable to define operating system." + defaultBackColor
            raise Exception(error) # error for 'unknown' system
            
            sys.exit()
    except Exception:
        print(backRed + "ERROR: Unable to define operating system." + defaultBackColor)