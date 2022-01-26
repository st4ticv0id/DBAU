import os
import sys
fileFolder: str = os.path.dirname(os.path.abspath(__file__))
PYTHONPATHFolder: str = fileFolder.replace('/interfaces', '')
sys.path.append(PYTHONPATHFolder)

from classes.GlobalVariables import *

def loadHelpInterface():
    print(foreBlue + "Debian Based Auto-Updater - Help" + defaultForeColor)
    print("")
    print(foreBlue + "Example: python3 DBAU.py <argument>" + defaultForeColor)
    print("")
    print(foreBlue + "ARGUMENTS:")
    print(foreBlue + "-h   --help   Show available arguments" + defaultForeColor)
    print(foreBlue + "-s   --settings   It allows you to edit the tool settings" + defaultForeColor)
    print(foreBlue + "-v   --version   Print out the current version of the tool" + defaultForeColor)
    