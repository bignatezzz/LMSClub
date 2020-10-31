#!/usr/bin/python

def reverseStr(word):
    resStr=""
    lenStr = len(word)
    while lenStr > 0:
          print "resStr="+resStr+", lenStr="+str(lenStr)
          resStr+=word[lenStr-1]
          lenStr-=1 
    return resStr

myword="abcdefgh"
result=reverseStr(myword)
print myword+" reversed to "+result
