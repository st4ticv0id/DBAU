import os
import sys
fileFolder: str = os.path.dirname(os.path.abspath(__file__))
PYTHONPATHFolder: str = fileFolder.replace('/debian', '')
sys.path.append(PYTHONPATHFolder)
import datetime
import subprocess

from time import sleep
from datetime import date, datetime
from classes.CheckConnection import *
from classes.GlobalVariables import *

def debianSystemUpdate():
    mainPath: str = getMainPath()

    animationsList: list = ["|", "/", "-", "\\"]

    tryagainCounter: int = 0
    connResult: int = 1

    while (connResult != 0):
        connResult = connectionStatus()

        if (connResult == 0):
            print("")
            print(foreGreen + "Connection status: Online" + defaultForeColor)
            print("")
            print(foreGreen + "Updating repositories. Please wait..." + defaultForeColor)

            updateCommand = "sudo apt-get update"
            outUpdate = subprocess.Popen(updateCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # running apt-get update command in a new process

            print("")
            print(foreGreen + "Repositories update complete." + defaultForeColor)
            print("")
            print(foreGreen + "Starting system upgrade. Don't exit or shutdown the computer..." + defaultForeColor)

            upgradeCommand = "sudo apt-get dist-upgrade -y"
            outUpgrade = subprocess.Popen(upgradeCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # running apt-get dist-upgrade command in a new process

            stdout,stderr = outUpgrade.communicate() # read the standard output and standard error from the previous process
            errorGeneric = "E: "
            errorSpecific1 = "E: Unable to correct problems, you have held broken packages"
            errorSpecific2 = "E: Sub-process /usr/bin/dpkg returned an error code (1)"
            
            todayDate = date.today() # getting current date
            currentDate = todayDate.strftime("%d-%m-%Y") # date format

            if (errorGeneric.encode() in stdout):
                print("")
                print(backRed + "ERROR: An error occurred during the update," + defaultBackColor)
                print(backRed + f"error log putted into '{mainPath}/Linux_APT_Updater/logs'." + defaultBackColor)

                try:
                    writeToFile = open(f"{mainPath}/logs/error_log_{currentDate}.log", "w")
                    writeToFile.writelines(stdout.decode("utf-8")) # decode and write in log file the apt-get dist-upgrade command result in case of errors
                except FileNotFoundError:
                    print("")
                    print(backRed + f"ERROR: Directory '{mainPath}/logs' could not be found." + defaultBackColor)

                try:
                    raise SystemExit
                except Exception:
                    sys.exit()
            elif (errorSpecific1.encode() in stdout):
                print("")
                print(backRed + "ERROR: An error occurred during the update," + defaultBackColor)
                print(backRed + f"error log putted into '{mainPath}/logs'." + defaultBackColor)

                try:
                    writeToFile = open(f"{mainPath}/logs/error_log_{currentDate}.log", "w")
                    writeToFile.writelines(stdout.decode("utf-8")) # decode and write in log file the apt-get dist-upgrade command standard output in case of errors
                except FileNotFoundError:
                    print("")
                    print(backRed + f"ERROR: Directory '{mainPath}/logs' could not be found." + defaultBackColor)

                try:
                    raise SystemExit
                except Exception:
                    sys.exit()
            elif (errorSpecific2.encode() in stdout):
                print("")
                print(backRed + "ERROR: An error occurred during the update," + defaultBackColor)
                print(backRed + f"error log putted into '{mainPath}/logs'." + defaultBackColor)

                try:
                    writeToFile = open(f"{mainPath}/logs/error_log_{currentDate}.log", "w")
                    writeToFile.writelines(stdout.decode("utf-8")) # decode and write in log file the apt-get dist-upgrade command standard output in case of errors
                except FileNotFoundError as DirNotFoundError:
                    DNFEString: str = str(DirNotFoundError) # converting the NameError value into string # DirNotFoundError => DNFE
        
                    todayDate = date.today() # getting current date
                    currentDate = todayDate.strftime("%d%m%Y") # date format

                    if (os.path.isfile(f"{mainPath}/logs/DirNotFoundError_{currentDate}.log") == False):
                        DNFEFile = open(f"{mainPath}/logs/DirNotFoundError_{currentDate}.log", "w+")
                        DNFEFile.write(f"BEGIN ERROR => {DNFEString} == END ERROR (issue report: https://github.com/st4ticv0id/DBAU/issues)")
                        DNFEFile.close()

                    print("")
                    print(backRed + f"ERROR: Directory '{mainPath}/logs' could not be found. Please report your problem on https://github.com/st4ticv0id/DBAU/issues" + defaultBackColor)
                    print(backRed + f"attaching the file '{mainPath}/logs/DirNotFoundError_{currentDate}.log' or its contents. Sorry for the inconvenience!" + defaultBackColor)

                try:
                    raise SystemExit
                except Exception:
                    sys.exit()
            else:
                dpkgCommand = "sudo dpkg --configure -a" # configuring installed but uncofigured packages
                autoremoveCommand = "sudo apt-get autoremove -y" # removing old unnecessary dependencies
                autocleanCommand = "sudo apt-get autoclean -y" # removing useless local downloaded packages 

                try:
                    outDpkg = subprocess.Popen(dpkgCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # opening process and execute 'dpkgCommand'
                    stdout, stderr = outDpkg.communicate()
                
                    outAutoremove = subprocess.Popen(autoremoveCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # opening process and execute 'autoremoveCommand'
                    stdout, stderr = outAutoremove.communicate()
                
                    outAutoclean = subprocess.Popen(autocleanCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # opening process and execute 'autocleanCommand'
                    stdout, stderr = outAutoclean.communicate()

                    try:
                        # getting current date and time
                        todayDate = date.today() # getting current date
                        currentDate = todayDate.strftime("%d/%m/%Y")

                        dateTime = datetime.now()
                        currentTime = dateTime.strftime("%H:%M:%S")

                        # write to string
                        successData: str = f"System update completed (Full Operation: configure and clean) - DATE => {currentDate} TIME => {currentTime}"

                        successUpdateFile = open(f"{mainPath}/logs/updates_success_list.log", "a") # open success system update log file
                        successUpdateFile.write("\n")
                        successUpdateFile.write(successData) # write the string inside the file
                        successUpdateFile.close() # close and save
                    except:
                        print("")
                        print(Fore.YELLOW + "Can't add new line into update log. Proceeding anyway..." + defaultForeColor)

                    print("")
                    print(backGreen + "System update completed successfully." + defaultBackColor)
                except Exception:
                    try:
                        # getting current date and time
                        todayDate = date.today() # getting current date
                        currentDate = todayDate.strftime("%d/%m/%Y")

                        dateTime = datetime.now()
                        currentTime = dateTime.strftime("%H:%M:%S")

                        # write to string
                        successData: str = f"System update completed (Half operation: no configure and/or clean) - DATE => {currentDate} TIME => {currentTime}"

                        successUpdateFile = open(f"{mainPath}/logs/updates_success_list.log", "a") # open success system update log file
                        successUpdateFile.write("\n")
                        successUpdateFile.write(successData) # write the string inside the file
                        successUpdateFile.close() # close and save
                    except:
                        print("")
                        print(Fore.YELLOW + "Can't add new line into update log. Proceeding anyway..." + defaultForeColor)
                    
                    print("")
                    print(Back.YELLOW + "WARNING: System update completed, but old packages can be cleaned or removed." + defaultBackColor)
                try:
                    raise SystemExit
                except Exception:
                    sys.exit()
        elif (connResult == 1):
            if (tryagainCounter >= 600):
                print("")
                print(foreRed + "ERROR: Too many failed attempts. Abort update operation." + defaultForeColor)

                tryagainCounter = 0

                try:
                    sys.exit()
                except Exception:
                    raise SystemExit
            elif (tryagainCounter < 600):
                sleep(1)
                while (connResult == 1):
                    for animation in animationsList:
                        print(f"Connection status: Offline - waiting for connection {animation}", end="\r")

                tryagainCounter += 1