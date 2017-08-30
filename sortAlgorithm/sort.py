# -*- coding:utf-8 -*-
import time
#insertions sort. Worst case running time is n^2, linear for the almost sorted array.
def insertionsort(s):
    startinsert=time.clock()
    for i in range(1,len(s)):
        a=s[i]
        j=i-1
	while (j>=0 and a<s[j]):
	    s[j+1]=s[j]
	    j=j-1
	s[j+1]=a
    endinsert=time.clock()
    print '花的时间为 '+str(endinsert-startinsert)
    return s
 
