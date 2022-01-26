from crontab import CronTab
from classes.GlobalVariables import *

def addCrontabJob(minute: str, hour: str, dom: str, month: str, dow: str):
    mainPath: str = getMainPath()
    
    try:
        userCron = CronTab(user=True) # use current linux user
        schedule = userCron.new(command=f'python3 {mainPath}/DBAU.py', comment="dbaujob") # command to be executed from cron and a comment to handle it
        schedule.setall(f"{minute} {hour} {dom} {month} {dow}") # set up the job time
        userCron.write(); # save and write to crontab
        
        return True # code works fine
    except Exception:
        print("")
        print(Fore.RED + "ERROR: Can't add cron schedule to crontab." + defaultForeColor)
        print(Fore.RED + f"Add schedule manually by adding this line inside crontab: '{minute} {hour} {dom} {month} {dow} python3 {mainPath}/DBAU.py # dbaujob'" + defaultForeColor)
        
        return False # errors

# def updateCrontabJob(crontabComment: str, minute: str, hour: str, dayOfMonth: str, monthOfYear: str, dayOfWeek: str): # All values ​​accept numbers, to indicate 'always' use '*'
#     try:
#         userCron = CronTab(user=True)
#         for schedule in userCron:
#             if schedule.comment == crontabComment:
#                 schedule.setall(f"{minute} {hour} {dayOfMonth} {monthOfYear} {dayOfWeek}")
#                 userCron.write();
                
#         return True # code works fine
#     except Exception:
#         print()
        
#         return False # errors

def removeCrontabJob(crontabComment: str):
    try:
        userCrontab = CronTab(user=True)
        for schedule in userCrontab: # gets all crontab jobs
            if schedule.comment == crontabComment: # search for specific job with our comment
                userCrontab.remove(schedule) # remove it
                userCrontab.write()
                
        return True # code works fine
    except Exception:
        print("")
        print(foreRed + "ERROR: Can't delete cron schedule from crontab." + defaultForeColor)
        print(foreRed + "Remove schedule manually by deleting the line with comment '# dbaujob' using this console command: crontab -e" + defaultForeColor)
        
        return False # errors