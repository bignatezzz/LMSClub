#!/bin/python

#open schedule.txt file
myfile = open("./schedule.txt")

#read all lines from the file
mylines = myfile.readlines()


#define a dictionary to gather schedule per day
thisdict = {}

#define the order of printing a schedule and valid days
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

#define the order of times of the periods and valid times
times = ["8am-9am",
         "9am-10am",
         "10am-11am",
         "11am-12pm",
         "12pm-1pm",
         "1pm-2pm",
         "2pm-3pm"]

#process one line at a time
for myline in mylines:

    #split the line using comma and convert into array of strings
    myline_list = myline.split(",")

    #get the day from the first element
    day = myline_list[0]

    #check if the first element in the array is one of the days in the dictionary
    if day in days:

       #if the day is not one of the keys create an empty dictionary for the day so you can add the data later
       if day not in thisdict.keys():
          thisdict[day] = {}

       #getting time, teacher, and period number from the list
       #remove spaces in the time to match with the valid times
       my_time = myline_list[2].replace(" ", "")
       my_teacher = myline_list[3]
       my_period = myline_list[1]

       #if my_time is not valid, ignore
       if my_time not in times:
          continue 

       #if my_time is not one of the keys create an empty list to capture the details of the schedule later
       if my_time not in thisdict[day].keys():
          thisdict[day][my_time] = []

       #we are adding the schedule from the line to the list
       thisdict[day][my_time].append(my_period)
       thisdict[day][my_time].append(my_teacher)
    else:
       #if the day is not valid print error
       print "Invalid Day "+ day

#pick a day in the defined order
for day in days:
    #find the schedule for that day in the dictionary
    sched_dict = thisdict[day]
    print str(day)
    #print each schedule for different timings
    for my_time in times:
        if my_time in sched_dict.keys():
           print str(my_time)+","+ str(thisdict[day][my_time][0])+ "," + str(thisdict[day][my_time][1])
