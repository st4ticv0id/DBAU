import os
import sys
fileFolder: str = os.path.dirname(os.path.abspath(__file__))
PYTHONPATHFolder: str = fileFolder.replace('/classes', '')
sys.path.append(PYTHONPATHFolder)

from classes.GlobalVariables import *
from interfaces.HelpInterface import *

def settingsCLI():
    isFirstLoad: bool = True
    if (isFirstLoad == True):
        os.system("clear") # change cls with clear
        print(upperLeftDoubleCorner + (horizontalDoubleBorder * 63) + upperRightDoubleCorner)                                                                                          # ╔═══════════════════════════════════════════════════════════════╗
        print(verticalDoubleBorder + (foreBlue + "             Debian Based Auto-Updater - Settings              " + defaultForeColor) + verticalDoubleBorder)             # ║             Debian Based Auto-Updater - Settings              ║
        print(verticalDoubleBorder + (" " * 63) + verticalDoubleBorder)                                                                                                    # ║                                                               ║
        print(verticalDoubleBorder + " What do you want to edit?:                                    " + verticalDoubleBorder)                                             # ║ What do you want to edit?:                                    ║
        print(verticalDoubleBorder + (" 1. " + backBlue + "Root password" + defaultBackColor + "                                              ") + verticalDoubleBorder)   # ║ 1. **Root password**                                          ║
        print(verticalDoubleBorder + " 2. Auto-update schedule                                       " + verticalDoubleBorder)                                             # ║ 2. Auto-update schedule                                       ║
        print(middleLeftSemiDoubleCorner + (horizontalDoubleBorder * 63) + middleRightSemiDoubleCorner)                                                                                # ╠═══════════════════════════════════════════════════════════════╣
        print(verticalDoubleBorder + (foreBlue + "        Use [↑]/[↓] to move and [↵] to select an option.       " + defaultForeColor) + verticalDoubleBorder)                                             # ║        Use [↑]/[↓] to move and [↵] to select an option.       ║
        print(lowerLeftDoubleCorner + (horizontalDoubleBorder * 63) + lowerRightDoubleCorner)                                                                                          # ╚═══════════════════════════════════════════════════════════════╝
        print("")
        isFirstLoad = False     
    try:       
        import interfaces.SettingsInterface as settingsgui
        settingsgui.loadSettingsInterface()
    except TypeError:
        pass
    except AttributeError:
        pass
    
def helpCLI():
    loadHelpInterface()
    