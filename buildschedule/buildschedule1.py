#!/bin/python

#open schedule.txt file
myfile = open("./schedule.txt")

#read all lines from the file
mylines = myfile.readlines()

#print each line from the file
for myline in mylines:
    myline_list = myline.split(",")
    #print str(myline_list)
    #print myline
    if myline_list[0] in "Mon":
       print myline_list[0]
       sched=myline_list[1:]
       print str(sched)

for myline in mylines:
    myline_list = myline.split(",")
    #print str(myline_list)
    #print myline
    if myline_list[0] in "Tue":
       print myline_list[0]
       sched=myline_list[1:]
       print str(sched)

for myline in mylines:
    myline_list = myline.split(",")
    #print str(myline_list)
    #print myline
    if myline_list[0] in "Wed":
       print myline_list[0]
       sched=myline_list[1:]
       print str(sched)

for myline in mylines:
    myline_list = myline.split(",")
    #print str(myline_list)
    #print myline
    if myline_list[0] in "Thu":
       print myline_list[0]
       sched=myline_list[1:]
       print str(sched)

for myline in mylines:
    myline_list = myline.split(",")
    #print str(myline_list)
    #print myline
    if myline_list[0] in "Fri":
       print myline_list[0]
       sched=myline_list[1:]
       print str(sched)