# 
# Program: This is an example program that shows how to use functions.
#           1. We are printing inside a function-printMySchedule
#           2. We get the schedule from a function and print that schedule
#              outside the function-getMySchedule.
# Author: Aashrith
# Date : 9/18/20

def printMySchedule():
    a = """Day           Time.                        Subject
            Monday   10:00 - 11:00 AM    Period 1
                     11:30-12:30 AM.    Math
            Tuesday  9:00-11:00 AM     PE
                     10:00-11:00 AM.    Science"""
    print(a)

def getMySchedule():
    a = """Day           Time.                        Subject
            Monday   10:00 - 11:00 AM    Period 1
                     11:30-12:30 AM.    Math
            Tuesday  9:00-11:00 AM     PE
                     10:00-11:00 AM.    Science"""
    return a

print("print schedule inside a function:")
printMySchedule()

print("get schedule from a function:")
schedule = getMySchedule()
print(schedule)