#!/usr/bin/python

def rev(word):
    res=""
    for c in word:
        print "res="+res+", "+c
        res=c+res
    return res

myword="abcdefgh"
result=rev(myword)
print myword+" reversed to "+result
        
