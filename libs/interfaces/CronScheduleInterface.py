import os
import sys
fileFolder: str = os.path.dirname(os.path.abspath(__file__))
PYTHONPATHFolder: str = fileFolder.replace('/interfaces', '')
sys.path.append(PYTHONPATHFolder)

from classes.CrontabHandler import *
from classes.GlobalVariables import *

minuteValue: str
hourValue: str
domValue: str # dom => day of month
monthValue: str
dowValue: str # dow => day of week

tryAgainOperation: bool = True
inputPoint: int = 1 # counting which function to load

def loadCronScheduleInterface():
    
    global minuteValue, hourValue, domValue, monthValue, dowValue
    global tryAgainOperation, inputPoint
    
    os.system("clear")
    __HeaderText()
    
    while (tryAgainOperation == True and inputPoint != 6):
        if (inputPoint == 1):
            __inputMinute()
        elif (inputPoint == 2):
            __inputHour()
        elif (inputPoint == 3):
            __inputDayOfMonth()
        elif (inputPoint == 4):
            __inputMonth()
        elif (inputPoint == 5):
            __inputDayOfWeek()
    
    removeCrontabJob("dbaujob")
    addCrontabJob(minuteValue, hourValue, domValue, monthValue, dowValue)
    
    print("")
    print(backGreen + "Cron job added successfully!" + defaultBackColor)    
    
def __HeaderText():
    print(foreBlue + "Let's proceed to the configuration of a new cron job, please fill in the" + defaultForeColor)
    print(foreBlue + "fields that will appear below. (For more information on cron and crontab see: https://en.wikipedia.org/wiki/Cron)" + defaultForeColor)
        
def __inputMinute():
    global minuteValue
    global tryAgainOperation, inputPoint
    
    print("")
    minuteString: str = input(foreBlue + "Input minute. ([0 to 59]/[*]): >>" + defaultForeColor + "")
    if (minuteString.isdecimal() == True and (len(minuteString) >= 1 and len(minuteString) <= 3)):
        minuteInteger: int = int(minuteString) # convert to integer to remove some zeros in excess
        if (minuteInteger > 59 or minuteInteger < 0):
            print(foreRed + f"ERROR: '{minuteInteger}' isn't a valid input. (Input a minute between 0 and 59 or input '*' for all minutes)" + defaultForeColor)
            
            tryAgainOperation = True
            inputPoint = 1
        else:
            minuteValue = str(minuteInteger) # convert int to string
            
            tryAgainOperation = True
            inputPoint += 1 # add 1 and let code go to next function
    elif (minuteString == "*"):
        minuteValue = minuteString
        
        tryAgainOperation = True
        inputPoint += 1 # add 1 and let code go to next function
    else:
        print(foreRed + f"ERROR: '{minuteString}' isn't a valid input. (Input a minute between 0 and 59 or input '*' for all minutes)" + defaultForeColor)
        
        tryAgainOperation = True
        inputPoint = 1
        
def __inputHour():
    global hourValue
    global tryAgainOperation, inputPoint
    
    print("")
    hourString: str = input(foreBlue + "Input hour. ([0 to 23]/[*]): >>" + defaultForeColor + "")
    if (hourString.isdecimal() == True and (len(hourString) >= 1 and len(hourString) <= 3)):
        hourInteger: int = int(hourString) # convert to integer to remove some zeros in excess
        if (hourInteger > 23 or hourInteger < 0):
            print(foreRed + f"ERROR: '{hourInteger}' isn't a valid input. (Input an hour between 0 and 23 or input '*' for all hours)" + defaultForeColor)
            
            tryAgainOperation = True
            inputPoint = 2
        else:
            hourValue = str(hourInteger) # convert int to string
            
            tryAgainOperation = True
            inputPoint += 1 # add 1 and let code go to next function
    elif (hourString == "*"):
        hourValue = hourString
        
        tryAgainOperation = True
        inputPoint += 1 # add 1 and let code go to next function
    else:
        print(foreRed + f"ERROR: '{hourString}' isn't a valid input. (Input a hour between 0 and 23 or input '*' for all hours)" + defaultForeColor)
        
        tryAgainOperation = True
        inputPoint = 2
        
def __inputDayOfMonth():
    global domValue
    global tryAgainOperation, inputPoint
    
    print("")
    domString: str = input(foreBlue + "Input day. ([1 to 31]/[*]): >>" + defaultForeColor + "")
    if (domString.isdecimal() == True and (len(domString) >= 1 and len(domString) <= 3)):
        domInteger: int = int(domString) # convert to integer to remove some zeros in excess
        if (domInteger > 31 or domInteger < 1):
            print(foreRed + f"ERROR: '{domInteger}' isn't a valid input. (Input a day between 1 and 31 or input '*' for all days)" + defaultForeColor)
            
            tryAgainOperation = True
            inputPoint = 3
        else:
            domValue = str(domInteger) # convert int to string
            
            tryAgainOperation = True
            inputPoint += 1 # add 1 and let code go to next function
    elif (domString == "*"):
        domValue = domString
        
        tryAgainOperation = True
        inputPoint += 1 # add 1 and let code go to next function
    else:
        print(foreRed + f"ERROR: '{domString}' isn't a valid input. (Input a day between 1 and 31 or input '*' for all days)" + defaultForeColor)
        
        tryAgainOperation = True
        inputPoint = 3
        
def __inputMonth():
    global monthValue
    global tryAgainOperation, inputPoint
    
    print("")
    monthString: str = input(foreBlue + "Input month. ([1 to 12]/[1,2,3,4...]/[*]): >>" + defaultForeColor + "")
    if (monthString.isdecimal() == True and (len(monthString) >= 1 and len(monthString) <= 3)):
        monthInteger: int = int(monthString) # convert to integer to remove some zeros in excess
        if (monthInteger > 12 or monthInteger < 1):
            print(foreRed + f"ERROR: '{monthInteger}' isn't a valid input. (Input a month between 1 and 12, select specific months using commas: 'ex.: 1,3,7' or input '*' for all months)" + defaultForeColor)
            
            tryAgainOperation = True
            inputPoint = 4
        else:
            monthValue = str(monthInteger) # convert int to string
            
            tryAgainOperation = True
            inputPoint += 1 # add 1 and let code go to next function
    elif (monthString == "*"):
        monthValue = monthString
        
        tryAgainOperation = True
        inputPoint += 1 # add 1 and let code go to next function
    elif ("," in monthString):
        monthList: list = list(monthString.replace(',', ''))
        
        itemCount = len(monthList)
        if (itemCount > 12 or itemCount < 1):
            finalValue: str = ""
            for monthItem in monthList:
                monthInteger: int = int(monthItem)
                if (finalValue == ""):
                    finalValue = str(monthInteger)
                else:
                    finalValue = finalValue + "," + str(monthInteger)
            print(foreRed + f"ERROR: '{finalValue}' isn't a valid input. (Input specific months using commas: 'ex.: 1,3,7')" + defaultForeColor)
            
            tryAgainOperation = True
            inputPoint = 4
        else:
            finalValue: str = ""
            for monthItem in monthList:
                monthInteger: int = int(monthItem)
                if (finalValue == ""):
                    finalValue = str(monthInteger)
                else:
                    finalValue = finalValue + "," + str(monthInteger)
            monthValue = finalValue
        
            tryAgainOperation = True
            inputPoint += 1 # add 1 and let code go to next function
    else:
        print(foreRed + f"ERROR: '{monthString}' isn't a valid input. (Input a month between 1 and 12, select specific months using commas: 'ex.: 1,3,7' or input '*' for all months)" + defaultForeColor)
        
        tryAgainOperation = True
        inputPoint = 4
        
def __inputDayOfWeek():
    global dowValue
    global tryAgainOperation, inputPoint
    
    print("")
    dowString: str = input(foreBlue + "Input week day. ([0 to 6]/[sun,mon,tue,...]/[*]): >>" + defaultForeColor + "")
    if (dowString.isdecimal() == True and (len(dowString) >= 1 and len(dowString) <= 3)):
        dowInteger: int = int(dowString) # convert to integer to remove some zeros in excess
        if (dowInteger > 12 or dowInteger < 1):
            print(foreRed + f"ERROR: '{dowInteger}' isn't a valid input. (Input a week day between 0 and 6, select specific week days using commas: 'ex.: sun,mon,tue' or input '*' for all week days)" + defaultForeColor)
            
            tryAgainOperation = True
            inputPoint = 5
        else:
            dowValue = str(dowInteger) # convert int to string
            
            tryAgainOperation = False
            inputPoint += 1 # add 1 and let code go to next function
    elif (dowString == "*"):
        dowValue = dowString
        
        tryAgainOperation = False
        inputPoint += 1 # add 1 and let code go to next function
    elif ("," in dowString):
        dowList: list = list(dowString.split(","))
        
        itemCount = len(dowList)
        if (itemCount > 6 or itemCount < 0):
            finalValue: str = ""
            for dowItem in dowList:
                if (finalValue == ""):
                    finalValue = dowItem
                else:
                    finalValue = finalValue + "," + dowItem
            print(foreRed + f"ERROR: '{finalValue}' isn't a valid input. (Input specific week days using commas: 'ex.: sun,mon,tue')" + defaultForeColor)
            
            tryAgainOperation = True
            inputPoint = 5
        else:
            finalValue: str = ""
            for dowItem in dowList:
                if (finalValue == ""):
                    finalValue = dowItem
                else:
                    finalValue = finalValue + "," + dowItem
            dowValue = finalValue
        
            tryAgainOperation = False
            inputPoint += 1 # add 1 and let code go to next function
    else:
        print(foreRed + f"ERROR: '{dowString}' isn't a valid input. (Input a week day between 0 and 6, select specific week days using commas: 'ex.: sun,mon,tue' or input '*' for all week days)" + defaultForeColor)
        
        tryAgainOperation = True
        inputPoint = 5