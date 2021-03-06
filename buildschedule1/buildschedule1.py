#!/bin/python

#open schedule.txt file
myfile = open("./schedule.txt")

#read all lines from the file
mylines = myfile.readlines()


thisdict = {
   "Mon": [],
   "Tue": [],
   "Wed": [],
   "Thu": [],
   "Fri": []
}


#print each line from the file
for myline in mylines:
    myline_list = myline.split(",")
    #print str(myline_list)
    #print myline
    if myline_list[0] in thisdict.keys():
       #print myline_list[0]
       sched=myline_list[1:]
       #print str(sched)
       thisdict[myline_list[0]].append(sched)
    else:
       print "Invalid Day "+ str(myline_list[0])

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
for day in days:
    sched_list = thisdict[day]
    print str(day)
    for day_sched in sched_list:
        print str(day_sched)        

