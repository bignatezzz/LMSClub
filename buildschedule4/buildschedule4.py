#!/bin/python

#Author: Aashrith C
#Date: 4/17/21
#Description: This program loads the schedule file and converts into a dictionary and prints the schedule from the dictionary in an organized manner. This program organizes the program into functions. 

#global variables
#define a dictionary to gather schedule per day
g_thisdict = {}

#define the order of printing a schedule and valid days
g_days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

#define the order of times of the periods and valid times
g_times = ["8am-9am",
         "9am-10am",
         "10am-11am",
         "11am-12pm",
         "12pm-1pm",
         "1pm-2pm",
         "2pm-3pm"]
         "4pm-5pm"]

#this function parses the schedule file and loads into the dictionary
def load_schedule():
    #open schedule.txt file
    myfile = open("./schedule.txt")

    #read all lines from the file
    mylines = myfile.readlines()



    #process one line at a time
    for myline in mylines:

        #split the line using comma and convert into array of strings
        myline_list = myline.split(",")

        #get the day from the first element
        day = myline_list[0]

        #check if the first element in the array is one of the days in the dictionary
        if day in g_days:

           #if the day is not one of the keys create an empty dictionary for the day so you can add the data later
           if day not in g_thisdict.keys():
              g_thisdict[day] = {}

           #getting time, teacher, and period number from the list
           #remove spaces in the time to match with the valid times
           my_time = myline_list[2].replace(" ", "")
           my_teacher = myline_list[3]
           my_period = myline_list[1]

           #if my_time is not valid, ignore
           if my_time not in g_times:
              continue 

           #if my_time is not one of the keys create an empty list to capture the details of the schedule later
           if my_time not in g_thisdict[day].keys():
              g_thisdict[day][my_time] = []

           #we are adding the schedule from the line to the list
           g_thisdict[day][my_time].append(my_period)
           g_thisdict[day][my_time].append(my_teacher)
        else:
           #if the day is not valid print error
           print "Invalid Day "+ day

#this function is used to print the schedule
def print_schedule():
    print "**************Schedule of the Week*****************"
    #pick a day in the defined order
    for day in g_days:
        #find the schedule for that day in the dictionary
        sched_dict = g_thisdict[day]
        print str(day)
        #print each schedule for different timings
        for my_time in g_times:
            if my_time in sched_dict.keys():
               print str(my_time)+","+ str(g_thisdict[day][my_time][0])+ "," + str(g_thisdict[day][my_time][1])

def add_to_schedule(day,period,time_period,teacher): 

     my_time = time_period.replace(" ", "")
     #if my_time is not valid, ignore
     if my_time not in g_times:
        print "#### Failed to add new entry to schedule: Invalid Time "+ time_period
        return False 

     if day in g_days:
        #if the day is not one of the keys create an empty dictionary for the day so you can add the data later
        if day not in g_thisdict.keys():
           g_thisdict[day] = {}

        #getting time, teacher, and period number from the list
        #remove spaces in the time to match with the valid times
        my_teacher = teacher
        my_period = period

        #if my_time is not one of the keys create
        # an empty list to capture the details of the schedule later
        if my_time not in g_thisdict[day].keys():
           g_thisdict[day][my_time] = []

        #we are adding the schedule from the line to the list
        g_thisdict[day][my_time].append(my_period)
        g_thisdict[day][my_time].append(my_teacher)
        
        print "Successfully added new entry to the schedule"
        return True
     else:
        #if the day is not valid print error
        print "#### Failed to add new entry to schedule: Invalid Day "+ day
        return False

#this is the main routine
load_schedule()
print_schedule()
day="Wed"
period="period 9"
time_period="4 pm -5 pm"
teacher="Mr. B"
ret=add_to_schedule(day,period,time_period,teacher)
if ret is True:
   print_schedule()
