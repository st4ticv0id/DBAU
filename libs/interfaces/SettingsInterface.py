try:
    import os
    import sys
    fileFolder: str = os.path.dirname(os.path.abspath(__file__))
    PYTHONPATHFolder: str = fileFolder.replace('/interfaces', '')
    sys.path.append(PYTHONPATHFolder)
    
    from pynput import keyboard
    from classes.GlobalVariables import *
    from interfaces.CronScheduleInterface import *
    from interfaces.RootPasswordInterface import *
    
    def loadSettingsInterface(key):
        maxOptionNumber: int = 3 # change this value with the max option number

        # Make selection possible => If the value of 'selectedOption' is greater than or equal to 1 and less than the maximum number of options available 
        # then it increases by one, otherwise if the value is equal to the maximum number of options it returns to one.
        
        selectedOption: int = getSelectedOption() # gets 'selectedOption' value from GlobalVariables library

        if (key == keyboard.Key.up):
            if (selectedOption <= maxOptionNumber and selectedOption > 1):
                decreaseOperation: int = selectedOption - 1
                setSelectedOption(decreaseOperation) # sets 'selectedOption' value from GlobalVariables library
            elif (selectedOption == 1):
                setSelectedOption(maxOptionNumber)
            __SettingsInterface()
        elif (key == keyboard.Key.down): 
            if (selectedOption >= 1 and selectedOption < maxOptionNumber): 
                increaseOperation:int = selectedOption + 1
                setSelectedOption(increaseOperation)
            elif (selectedOption == maxOptionNumber):
                setSelectedOption(1)
            __SettingsInterface()
        elif (key == keyboard.Key.enter):
            if (selectedOption == 1):
                loadRootPasswordInterface()
            elif (selectedOption == 2):
                loadCronScheduleInterface()
            elif (selectedOption == 3):
                print(foreBlue + "Exiting..." + defaultForeColor)

                sys.exit();
            setSelectedOption(1) # reset 'selectedOption' counter to 1
            return False # exit listener thread

    def __SettingsInterface():
        selectedOption = getSelectedOption()
        
        if (selectedOption == 1):
            os.system("clear")
            print(upperLeftDoubleCorner + (horizontalDoubleBorder * 63) + upperRightDoubleCorner)                                                                              # ╔═══════════════════════════════════════════════════════════════╗
            print(verticalDoubleBorder + (foreBlue + "             Debian Based Auto-Updater - Settings              " + defaultForeColor) + verticalDoubleBorder)             # ║             Debian Based Auto-Updater - Settings              ║
            print(verticalDoubleBorder + (" " * 63) + verticalDoubleBorder)                                                                                                    # ║                                                               ║
            print(verticalDoubleBorder + " What do you want to edit?:                                    " + verticalDoubleBorder)                                             # ║ What do you want to edit?:                                    ║
            print(verticalDoubleBorder + (" 1. " + backBlue + "Root password" + defaultBackColor + "                                              ") + verticalDoubleBorder)   # ║ 1. **Root password**                                          ║
            print(verticalDoubleBorder + " 2. Auto-update schedule                                       " + verticalDoubleBorder)                                             # ║ 2. Auto-update schedule                                       ║
            print(verticalDoubleBorder + " 3. Exit                                                       " + verticalDoubleBorder)                                             # ║ 3. Exit                                                       ║
            print(middleLeftSemiDoubleCorner + (horizontalDoubleBorder * 63) + middleRightSemiDoubleCorner)                                                                    # ╠═══════════════════════════════════════════════════════════════╣
            print(verticalDoubleBorder + "        Use [↑]/[↓] to move and [↵] to select an option.       " + verticalDoubleBorder)                                             # ║        Use [↑]/[↓] to move and [↵] to select an option.       ║
            print(lowerLeftDoubleCorner + (horizontalDoubleBorder * 63) + lowerRightDoubleCorner)                                                                              # ╚═══════════════════════════════════════════════════════════════╝
            print("")
        elif (selectedOption == 2):
            os.system("clear")
            print(upperLeftDoubleCorner + (horizontalDoubleBorder * 63) + upperRightDoubleCorner)                                                                              # ╔═══════════════════════════════════════════════════════════════╗
            print(verticalDoubleBorder + (foreBlue + "             Debian Based Auto-Updater - Settings              " + defaultForeColor) + verticalDoubleBorder)             # ║             Debian Based Auto-Updater - Settings              ║
            print(verticalDoubleBorder + (" " * 63) + verticalDoubleBorder)                                                                                                    # ║                                                               ║
            print(verticalDoubleBorder + " What do you want to edit?:                                    " + verticalDoubleBorder)                                             # ║ What do you want to edit?:                                    ║
            print(verticalDoubleBorder + " 1. Root password                                              " + verticalDoubleBorder)                                             # ║ 1. Root password                                              ║
            print(verticalDoubleBorder + (" 2. " + backBlue + "Auto-update schedule" + defaultBackColor + "                                       ") + verticalDoubleBorder)   # ║ 2. **Auto-update schedule**                                   ║
            print(verticalDoubleBorder + " 3. Exit                                                       " + verticalDoubleBorder)                                             # ║ 3. Exit                                                       ║
            print(middleLeftSemiDoubleCorner + (horizontalDoubleBorder * 63) + middleRightSemiDoubleCorner)                                                                    # ╠═══════════════════════════════════════════════════════════════╣
            print(verticalDoubleBorder + "        Use [↑]/[↓] to move and [↵] to select an option.       " + verticalDoubleBorder)                                             # ║        Use [↑]/[↓] to move and [↵] to select an option.       ║
            print(lowerLeftDoubleCorner + (horizontalDoubleBorder * 63) + lowerRightDoubleCorner)                                                                              # ╚═══════════════════════════════════════════════════════════════╝
            print("")
        elif (selectedOption == 3):
            os.system("clear")
            print(upperLeftDoubleCorner + (horizontalDoubleBorder * 63) + upperRightDoubleCorner)                                                                              # ╔═══════════════════════════════════════════════════════════════╗
            print(verticalDoubleBorder + (foreBlue + "             Debian Based Auto-Updater - Settings              " + defaultForeColor) + verticalDoubleBorder)             # ║             Debian Based Auto-Updater - Settings              ║
            print(verticalDoubleBorder + (" " * 63) + verticalDoubleBorder)                                                                                                    # ║                                                               ║
            print(verticalDoubleBorder + " What do you want to edit?:                                    " + verticalDoubleBorder)                                             # ║ What do you want to edit?:                                    ║
            print(verticalDoubleBorder + " 1. Root password                                              " + verticalDoubleBorder)                                             # ║ 1. Root password                                              ║
            print(verticalDoubleBorder + " 2. Auto-update schedule                                       " + verticalDoubleBorder)                                             # ║ 2. Auto-update schedule                                       ║
            print(verticalDoubleBorder + " 3. " + backBlue + "Exit" + defaultBackColor + "                                                       " + verticalDoubleBorder)     # ║ 3. **Exit**                                                   ║
            print(middleLeftSemiDoubleCorner + (horizontalDoubleBorder * 63) + middleRightSemiDoubleCorner)                                                                    # ╠═══════════════════════════════════════════════════════════════╣
            print(verticalDoubleBorder + "        Use [↑]/[↓] to move and [↵] to select an option.       " + verticalDoubleBorder)                                             # ║        Use [↑]/[↓] to move and [↵] to select an option.       ║
            print(lowerLeftDoubleCorner + (horizontalDoubleBorder * 63) + lowerRightDoubleCorner)                                                                              # ╚═══════════════════════════════════════════════════════════════╝
            print("")

    # run input listener as new thread
    with keyboard.Listener(
            on_release=loadSettingsInterface) as listener:
        listener.join() # join with the main thread
except TypeError:
    pass
except ImportError:
    import os
    import sys
    fileFolder: str = os.path.dirname(os.path.abspath(__file__))
    PYTHONPATHFolder: str = fileFolder.replace('/interfaces', '')
    sys.path.append(PYTHONPATHFolder)

    from classes.GlobalVariables import *
    from interfaces.CronScheduleInterface import *
    from interfaces.RootPasswordInterface import *
    
    def loadSettingsInterface():
        tryAgainOperation: bool = True
        while(tryAgainOperation == True):
            os.system("clear")
            
            print(foreBlue + "Debian Based Auto-Updater - Settings" + defaultForeColor)
            print("")
            print(foreBlue + "What do you want to edit?:" + defaultForeColor)
            print(foreBlue + "1. Root password" + defaultForeColor)
            print(foreBlue + "2. Auto-update schedule" + defaultForeColor)
            print(foreBlue + "3. Exit" + defaultForeColor)
            print("")
            
            optionInput = input(foreBlue + "Select an option ([1]/[2]/[3]): >>" + defaultForeColor + "")
            if (
                optionInput == "1"
                or optionInput == "01"
            ):
                tryAgainOperation = False
                
                loadRootPasswordInterface()
            elif (
                optionInput == "2"
                or optionInput == "02"
            ):
                tryAgainOperation = False

                loadCronScheduleInterface()
            elif (
                optionInput == "3"
                or optionInput == "03"
            ):
                tryAgainOperation = False

                print("")
                print(foreBlue + "Exiting..." + defaultForeColor)
                
                sys.exit()
            else:
                tryAgainOperation = True