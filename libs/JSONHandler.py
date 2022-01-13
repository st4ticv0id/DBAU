import sys
import os
import json

from datetime import date
from colorama import Fore, Back

defaultForeColor = Fore.WHITE
defaultBackColor = Back.BLACK

def generateSettingsJSON(MainDirPath: str):
    try:
        mainPath: str = MainDirPath

        createFile = open(f"{mainPath}/settings.json", "w+")
        createFile.close()

        jsonData: dict = {"DBAU-Settings": [{"FirstLaunch": [{"FirstLaunchValue": True}], "RootAuth": [{"RootAuthValue": ""}]}]} # default json string to be loaded in the settings.json file
        jsonString: str = json.dumps(jsonData) # converting the dictionary in a json readeable format

        settingsWriter = open(f"{mainPath}/settings.json", "w") # open the json file
        settingsWriter.write(jsonString) # write data to json
        settingsWriter.close() # close and save
    except Exception as jsonError:
        jsonErrorString: str = str(jsonError) # converting the NameError value into string
        
        todayDate = date.today() # getting current date
        currentDate = todayDate.strftime("%d%m%Y") # date format

        if (os.path.isfile(f"{mainPath}/logs/jsonError_{currentDate}.log") == False):
            jsonErrorFile = open(f"{mainPath}/logs/jsonError_{currentDate}.log", "w+")
            jsonErrorFile.write(f"BEGIN ERROR => {jsonErrorString} == END ERROR (issue report: INSERISCI QUI)")
            jsonErrorFile.close()

        print("")
        print(Back.RED + "ERROR: Some problems were occurred during json settings file generation. Please report your problem on INSERISCI QUI" + defaultBackColor) #Sostituire INSERISCI QUI con il link della pagina issue del progetto github
        print(Back.RED + f"attaching the file '{mainPath}/logs/jsonError_{currentDate}.log' or its contents. Sorry for the inconvenience!" + defaultBackColor)

        os.remove(f"{mainPath}/settings.json")
        
        sys.exit()

def readJSONValue(MainDirPath: str, SettingsName: str, SettingsNameValue: str):
    try:
        mainPath: str = MainDirPath

        settingsReader = open(f"{mainPath}/settings.json", "r")

        # begin reading of the FirstLaunchValue and getting value
        dataSettings = json.load(settingsReader)
        for key in dataSettings["DBAU-Settings"]:
            for value in key[SettingsName]:
                valueResult = value[SettingsNameValue]

        settingsReader.close()
        # end operation

        return valueResult
    except Exception as ReadJsonError:
        readJsonErrorString: str = str(ReadJsonError) # converting the NameError value into string
        
        todayDate = date.today() # getting current date
        currentDate = todayDate.strftime("%d%m%Y") # date format

        if (os.path.isfile(f"{mainPath}/logs/readJsonError_{currentDate}.log") == False):
            readJsonErrorFile = open(f"{mainPath}/logs/readJsonError_{currentDate}.log", "w+")
            readJsonErrorFile.write(f"BEGIN ERROR => {readJsonErrorString} == END ERROR (issue report: INSERISCI QUI)")
            readJsonErrorFile.close()

        print("")
        print(Back.RED + "ERROR: Some problems were occurred during reading a specific setting. Please report your problem on INSERISCI QUI" + defaultBackColor) #Sostituire INSERISCI QUI con il link della pagina issue del progetto github
        print(Back.RED + f"attaching the file '{mainPath}/logs/readJsonError_{currentDate}.log' or its contents. Sorry for the inconvenience!" + defaultBackColor)

        os.remove(f"{mainPath}/settings.json")
        
        sys.exit()

def updateJSONValue(MainDirPath: str, SettingsName: str, SettingsNameValue: str, NewValue):
    mainPath: str = MainDirPath

    settingsReader = open(f"{mainPath}/settings.json", "r")

    dataSettings = json.load(settingsReader)
    for key in dataSettings["DBAU-Settings"]:
        for value in key[SettingsName]:
            value[SettingsNameValue] = NewValue # setting up new value

    # begin edit of the FirstLaunchValue as specified before
    settingsWriter = open(f"{mainPath}/settings.json", "w")
    json.dump(dataSettings, settingsWriter)
    settingsWriter.close()
    settingsReader.close()
    # end operation