### OPEN SOURCE PROJECT - CREATE A COPY OF THIS PROJECT AND EDIT IT AS YOU LIKE ###
### LANG VERSION: PYTHON 3 ###

from genericpath import isdir, isfile
import os
import sys
import datetime
import subprocess

import libs.CheckConnection as checkconn
import libs.CheckSystem as checksys
import libs.FirstLaunch as fl
import libs.JSONHandler as jsonhdlr

from time import sleep
from datetime import date, datetime
from colorama import Fore, Back

defaultForeColor = Fore.WHITE
defaultBackColor = Back.BLACK

def DBAU():
    checksys.checkOS()

    mainPath: str = os.path.dirname(os.path.abspath(__file__)) # getting the DBAU.py path

    if (os.path.isdir(f"{mainPath}/logs") == False):
        try:
            os.makedirs(f"{mainPath}/logs")
        except Exception:
            print(Back.RED + f"ERROR: Can't create missing 'logs' folder. Create it manually inside '{mainPath}'." + defaultBackColor)

    if (os.path.isfile(f"{mainPath}/logs/updates_success_list.txt") == False):
        createFile = open(f"{mainPath}/logs/updates_success_list.txt", "w+")
        createFile.close()

    if (os.path.isfile(f"{mainPath}/settings.json") == False):
        jsonhdlr.generateSettingsJSON(mainPath)

    fl.firstLaunch(mainPath)

    tryagainCounter = 0
    connResult = 1

    while (connResult != 0):
        connResult = checkconn.connectionStatus()

        if (connResult == 0):
            print("")
            print(Fore.GREEN + "Connection status: Online" + defaultForeColor)
            print("")
            print(Fore.GREEN + "Updating repositories. Please wait..." + defaultForeColor)

            updateCommand = "sudo apt-get update"
            outUpdate = subprocess.Popen(updateCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # running apt-get update command in a new process

            print("")
            print(Fore.GREEN + "Repositories update complete." + defaultForeColor)
            print("")
            print(Fore.GREEN + "Starting system upgrade. Don't exit or shutdown the computer..." + defaultForeColor)

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
                print(Back.RED + "ERROR: An error occurred during the update," + defaultBackColor)
                print(Back.RED + f"error log putted into '{mainPath}/Linux_APT_Updater/logs'." + defaultBackColor)

                try:
                    writeToFile = open(f"{mainPath}/logs/error_log_{currentDate}.log", "w")
                    writeToFile.writelines(stdout.decode("utf-8")) # decode and write in log file the apt-get dist-upgrade command result in case of errors
                except FileNotFoundError:
                    print("")
                    print(Back.RED + f"ERROR: Directory '{mainPath}/logs' could not be found." + defaultBackColor)

                try:
                    raise SystemExit
                except Exception:
                    sys.exit()
            elif (errorSpecific1.encode() in stdout):
                print("")
                print(Back.RED + "ERROR: An error occurred during the update," + defaultBackColor)
                print(Back.RED + f"error log putted into '{mainPath}/logs'." + defaultBackColor)

                try:
                    writeToFile = open(f"{mainPath}/logs/error_log_{currentDate}.log", "w")
                    writeToFile.writelines(stdout.decode("utf-8")) # decode and write in log file the apt-get dist-upgrade command standard output in case of errors
                except FileNotFoundError:
                    print("")
                    print(Back.RED + f"ERROR: Directory '{mainPath}/logs' could not be found." + defaultBackColor)

                try:
                    raise SystemExit
                except Exception:
                    sys.exit()
            elif (errorSpecific2.encode() in stdout):
                print("")
                print(Back.RED + "ERROR: An error occurred during the update," + defaultBackColor)
                print(Back.RED + f"error log putted into '{mainPath}/logs'." + defaultBackColor)

                try:
                    writeToFile = open(f"{mainPath}/logs/error_log_{currentDate}.log", "w")
                    writeToFile.writelines(stdout.decode("utf-8")) # decode and write in log file the apt-get dist-upgrade command standard output in case of errors
                except FileNotFoundError as DirNotFoundError:
                    genericErrorString: str = str(DirNotFoundError) # converting the NameError value into string # DirNotFoundError => DNFE
        
                    todayDate = date.today() # getting current date
                    currentDate = todayDate.strftime("%d%m%Y") # date format

                    if (os.path.isfile(f"{mainPath}/logs/genericError_{currentDate}.log") == False):
                        DNFEFile = open(f"{mainPath}/logs/genericError_{currentDate}.log", "w+")
                        DNFEFile.write(f"BEGIN ERROR => {genericErrorString} == END ERROR (issue report: https://github.com/st4ticv0id/DBAU/issues)")
                        DNFEFile.close()

                    print("")
                    print(Back.RED + f"ERROR: Directory '{mainPath}/logs' could not be found. Please report your problem on https://github.com/st4ticv0id/DBAU/issues" + defaultBackColor)
                    print(Back.RED + f"attaching the file '{mainPath}/logs/genericError_{currentDate}.log' or its contents. Sorry for the inconvenience!" + defaultBackColor)

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
                    print(Back.GREEN + "System update completed successfully." + defaultBackColor)
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
                print(Fore.RED + "ERROR: Too many failed attempts. Abort update operation." + defaultForeColor)

                tryagainCounter = 0

                try:
                    sys.exit()
                except Exception:
                    raise SystemExit
            elif (tryagainCounter < 600):
                sleep(1)

                print(Fore.RED + "Connection status: Offline - Waiting for connection..." + defaultForeColor)

                tryagainCounter += 1
DBAU()