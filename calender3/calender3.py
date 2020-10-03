# 
# Program: This is an example program that shows how to use str functions.
#           1. We are printing captilize Schedule
#           2. find if the schedule has a day of your intrest
# Author: Aashrith
# Date : 10/03/20


 
def capitalizeMySchedule(str):
    print(str.upper())

def isMyDayPresent(str, findStr):  
    #for i in range(len(str)):
    #    print(i,str[i])
    strLower = str.lower()
    findStrLower = findStr.lower()
    #print( "strLower ",strLower)
    #print( "findStrLower ",findStrLower)
    result = strLower.find(findStrLower)

    if result > -1:
        print( findStr, " is in the schedule at ", result)
    else: 
        print( findStr, " is not in the schedule.")

#The main code starts here
strSchedule = """Day           Time.                        Subject
        Monday   10:00 - 11:00 AM    Period 1
                 11:30-12:30 AM.    Math
        Tuesday  9:00-11:00 AM     PE
                 10:00-11:00 AM.    Science
        Wednesday  9:00-11:00 AM   Period 3
                 10:00-11:00 AM.    Science"""

print("Get my schedule from function and print in uppercase.")
capitalizeMySchedule(strSchedule)

print("Check if the character is in schedule")
isMyDayPresent(str=strSchedule, findStr = "Wednesday" )

isMyDayPresent(strSchedule, "Monday" )

isMyDayPresent(strSchedule, "tuesdaY")
