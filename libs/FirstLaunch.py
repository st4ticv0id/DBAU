import os
import os.path
import sys
import json
import subprocess
import apt

import libs.JSONHandler as jsonhdlr
import libs.RootPrivileges as rootpvlg

from os import path
from colorama import Fore, Back
from crontab import CronTab

defaultForeColor = Fore.WHITE
defaultBackColor = Back.BLACK

def firstLaunch(MainDirPath: str):
    aptCache = apt.Cache()
    isFirstLaunch: bool = False
    mainPath: str = MainDirPath

    isFirstLaunch = jsonhdlr.readJSONValue(mainPath, "FirstLaunch", "FirstLaunchValue")

    if (isFirstLaunch == True):
        rootpvlg.storePassword(mainPath)
        rootpvlg.elevatePrivileges(mainPath)

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

                    jsonhdlr.updateJSONValue(mainPath, "FirstLaunch", "FirstLaunchValue", True)

                    sys.exit()
        except Exception:
            response = Back.RED + "ERROR: Can't define if the package is installed. Manually proceed to install 'cron' package." + defaultBackColor

            print("")
            print(response)

            jsonhdlr.updateJSONValue(mainPath, "FirstLaunch", "FirstLaunchValue", True)

            sys.exit()
        cronEnableCommand = ("sudo systemctl enable cron") # enable cron execution at system startup
        outCronEnable = subprocess.Popen(cronEnableCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # opening process and execute 'dpkgCommand'
        stdout, stderr = outCronEnable.communicate()

        try:
            userCron = CronTab(user=True)
            schedule = userCron.new(command=f'python3 {mainPath}/DBAU.py')
            schedule.every(12).hours();
            userCron.write();
        except Exception:
            print("")
            print(Fore.RED + "ERROR: Can't add cron schedule to crontab." + defaultForeColor)
            print(Fore.RED + f"Add schedule manually by adding this line inside crontab: '00 12 * * * python3 {mainPath}/DBAU.py'" + defaultForeColor)

            jsonhdlr.updateJSONValue(mainPath, "FirstLaunch", "FirstLaunchValue", True)

            sys.exit()
        print("")
        print(Back.GREEN + "All set up correctly. Proceeding with the first auto-update." + defaultBackColor)

        jsonhdlr.updateJSONValue(mainPath, "FirstLaunch", "FirstLaunchValue", False)

        return None
    elif (isFirstLaunch == False):
        rootpvlg.elevatePrivileges(mainPath)

        return None