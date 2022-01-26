from colorama import *

## STRINGS ##
mp: str = "/mnt/c/Users/nicol/source/repos/Test/Debian Based Auto-Updater/Debian Based Auto-Updater" # (CON VALORE SOLO PER TEST PER PUBBLICAZIONE DEVE ESSERE "")mainPath

def getMainPath():
    global mp
    return mp
def setMainPath(newValue: str):
    global mp
    mp = newValue
    
sv: str = "1.0.0" # softwareVersion => change this value every update

def getSoftwareVersion():
    global sv
    return sv
def setSoftwareVersion(newValue: str):
    global sv
    sv = newValue

## INTEGERS ##
so: int = 1 # selectedOption

def getSelectedOption():
    global so
    return so
def setSelectedOption(newValue: int):
    global so
    if (newValue <= 0):
        so = 1
    else:
        so = newValue

## COLORS ##
defaultForeColor = "\033[m"
defaultBackColor = "\033[m"
foreBlue: str = Fore.BLUE
backBlue: str = Back.BLUE
foreRed: str = Fore.RED
backRed: str = Back.RED
foreGreen: str = Fore.GREEN
backGreen: str = Back.GREEN
foreYellow: str = Fore.YELLOW
backYellow: str = Back.YELLOW
    
## INTERFACE ELEMENTS ##
# DOUBLE LINE #
upperLeftDoubleCorner: str = foreBlue + "╔" + defaultForeColor
upperRightDoubleCorner: str = foreBlue + "╗" + defaultForeColor
lowerLeftDoubleCorner: str = foreBlue + "╚" + defaultForeColor
lowerRightDoubleCorner: str = foreBlue + "╝" + defaultForeColor
middleLeftSemiDoubleCorner: str = foreBlue + "╠" + defaultForeColor
middleRightSemiDoubleCorner: str = foreBlue + "╣" + defaultForeColor
horizontalDoubleBorder: str = foreBlue + "═" + defaultForeColor
verticalDoubleBorder: str = foreBlue + "║" + defaultForeColor
# SINGLE LINE #
upperLeftSingleCorner: str = foreBlue + "┌" + defaultForeColor
upperRightSingleCorner: str = foreBlue + "┐" + defaultForeColor
lowerLeftSingleCorner: str = foreBlue + "└" + defaultForeColor
lowerRightSingleCorner: str = foreBlue + "┘" + defaultForeColor
middleLeftSemiSingleCorner: str = foreBlue + "├" + defaultForeColor
middleRightSemiSingleCorner: str = foreBlue + "┤" + defaultForeColor
horizontalSingleBorder: str = foreBlue + "—" + defaultForeColor
verticalSingleBorder: str = foreBlue + "│" + defaultForeColor