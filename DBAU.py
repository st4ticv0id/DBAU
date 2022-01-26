### OPEN SOURCE PROJECT - CREATE A COPY OF THIS PROJECT AND EDIT IT AS YOU LIKE ###
### LANG VERSION: PYTHON 3 ###
  
import sys
import os
fileFolder: str = os.path.dirname(os.path.abspath(__file__))
PYTHONPATHFolder: str = fileFolder.replace('/classes', '')
sys.path.append(PYTHONPATHFolder)

try:
    from libs.classes.CheckSystem import *
    from libs.classes.CLIHandler import *
    from libs.classes.GlobalVariables import *
    from libs.classes.JSONHandler import *
    from libs.debian.FirstLaunch import *
    from libs.debian.DebianSystemUpdate import *

    def DBAU():
        checkOS()

        argsCount: int = 0

        mainPath: str = os.path.dirname(os.path.abspath(__file__)) # getting the DBAU.py path
        setMainPath(mainPath)
        
        filename: str = os.path.basename(__file__)

        if (os.path.isdir(f"{mainPath}/logs") == False):
            try:
                os.makedirs(f"{mainPath}/logs")
            except Exception:
                print(backRed + f"ERROR: Can't create missing 'logs' folder. Create it manually inside '{mainPath}'." + defaultBackColor)
        
        if (os.path.isfile(f"{mainPath}/logs/updates_success_list.txt") == False):
            try:
                createFile = open(f"{mainPath}/logs/updates_success_list.txt", "w+")
                createFile.close()
            except Exception as fileCreationError:
                if (os.path.isdir(f"{mainPath}/logs") == True):
                    fileCreationErrorString: str = str(fileCreationError) # converting the NameError value into string
            
                    todayDate = date.today() # getting current date
                    currentDate = todayDate.strftime("%d%m%Y") # date format

                    if (os.path.isfile(f"{mainPath}/logs/fileCreationError_{currentDate}.log") == False):
                        DNFEFile = open(f"{mainPath}/logs/fileCreationError_{currentDate}.log", "w+")
                        DNFEFile.write(f"BEGIN ERROR => {fileCreationErrorString} == END ERROR (issue report: https://github.com/st4ticv0id/DBAU/issues)")
                        DNFEFile.close()

                    print("")
                    print(backRed + f"ERROR: File could't be created because the directory '{mainPath}/logs' could not be found. Please report your problem on https://github.com/st4ticv0id/DBAU/issues" + defaultBackColor)
                    print(backRed + f"attaching the file '{mainPath}/logs/fileCreationError_{currentDate}.log' or its contents. Sorry for the inconvenience!" + defaultBackColor)
                else:
                    print(backRed + "ERROR: File could't be created because the directory '{mainPath}/logs' could not be found." + defaultBackColor)

        if (os.path.isfile(f"{mainPath}/settings.json") == False):
            generateSettingsJSON()

        firstLaunch()
        
        argsList: list[str] = sys.argv
        argsList.remove(filename)

        for arg in argsList:
            argsCount += 1
            
        if (("-s" in argsList or "--settings" in argsList) and argsCount == 1):
            settingsCLI()
        elif (("-h" in argsList or "--help" in argsList) and argsCount == 1):
            helpCLI()
        elif (("-v" in argsList or "--version" in argsList) and argsCount == 1):
            softwareVersion  = getSoftwareVersion()
            print(f"DBAU version: {softwareVersion}")
        else:
            debianSystemUpdate()
except Exception:
    from colorama import Fore, Back
    
    defaultForeColor = "\033[m"
    defaultBackColor = "\033[m"
    
    def DBAU():
        print(Fore.RED + "For some reason it is not possible to run the tool on this system." + defaultForeColor)
        print(Fore.RED + "It is very likely that it is not compatible. I'm sorry :(" + defaultForeColor)
        
        sys.exit()
DBAU()
