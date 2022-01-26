import os
import os.path
import sys
fileFolder: str = os.path.dirname(os.path.abspath(__file__))
PYTHONPATHFolder: str = fileFolder.replace('/debian', '')
sys.path.append(PYTHONPATHFolder)
import subprocess
import apt

from os import path
from classes.CrontabHandler import *
from classes.GlobalVariables import *
from classes.JSONHandler import *
from classes.RootPrivileges import *

def firstLaunch():
    aptCache = apt.Cache()
    isFirstLaunch: bool = False
    mainPath: str = getMainPath()

    isFirstLaunch = readJSONValue("FirstLaunch", "FirstLaunchValue")

    if (isFirstLaunch == True):
        storePassword()
        elevatePrivileges()

        if (path.exists(f"{mainPath}/logs") == False):
            os.makedirs(f"{mainPath}/logs")

        aptCache.open() # setting up apt-cache for reading
        try:
            if (aptCache["cron"].is_installed == True): # checking if cron package is installed and running on cache
                response = Fore.GREEN + "Cron is installed, proceeding with schedule configuration..." + defaultForeColor

                print("")
                print(response)
            else:
                response = Fore.YELLOW + "WARNING: Cron is not installed, proceeding with installation..." + defaultForeColor

                print("")
                print(response)

                aptCache["cron"].mark_install() # mark cron package for installation
                try:
                    aptCache.commit() # commit and install marked packages
                except Exception:
                    print("")
                    print(Back.RED + "ERROR: Sorry, package installation failed." + defaultBackColor)

                    updateJSONValue(mainPath, "FirstLaunch", "FirstLaunchValue", True)

                    sys.exit()
        except Exception:
            response = Back.RED + "ERROR: Can't define if the package is installed. Manually proceed to install 'cron' package." + defaultBackColor

            print("")
            print(response)

            updateJSONValue(mainPath, "FirstLaunch", "FirstLaunchValue", True)

            sys.exit()
        cronEnableCommand = ("sudo systemctl enable cron") # enable cron execution at system startup
        outCronEnable = subprocess.Popen(cronEnableCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # opening process and execute 'dpkgCommand'
        stdout, stderr = outCronEnable.communicate()
        
        addCronJob: bool = addCrontabJob(0, 12, "*", "*", "*")
        if (addCronJob == False):
            updateJSONValue(mainPath, "FirstLaunch", "FirstLaunchValue", True)

            sys.exit()
        
        print("")
        print(Back.GREEN + "All set up correctly. Proceeding with the first auto-update." + defaultBackColor)

        updateJSONValue("FirstLaunch", "FirstLaunchValue", False)

        return None
    elif (isFirstLaunch == False):
        elevatePrivileges()

        return None