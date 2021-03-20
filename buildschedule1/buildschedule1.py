#!/bin/python

#open schedule.txt file
myfile = open("./schedule.txt")

#read all lines from the file
mylines = myfile.readlines()


#define a dictionary to gather schedule per day
thisdict = {
   "Mon": [],
   "Tue": [],
   "Wed": [],
   "Thu": [],
   "Fri": []
}


#print each line from the file
#process one line at a time
for myline in mylines:
    #split the line using comma and convert into array of strings
    myline_list = myline.split(",")
    #print str(myline_list)
    #print myline
    #check if the first element in the array is one of the days in the dictionary
    if myline_list[0] in thisdict.keys():
       #print myline_list[0]
       #getting information after the first element or day
       sched=myline_list[1:]
       #print str(sched)
       #we are adding the schedule from the line to the list
       thisdict[myline_list[0]].append(sched)
    else:
       #if the day is not valid print error
       print "Invalid Day "+ str(myline_list[0])

#define the order of printing a schedule
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
#pick a day in the defined order
for day in days:
    #find the schedule for that day in the dictionary
    sched_list = thisdict[day]
    print str(day)
    #print each schedule for different timings
    for day_sched in sched_list:
        print str(day_sched)        

