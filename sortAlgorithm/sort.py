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

# gap=2^k-1, running time: n^1.5
def shellsort(s):
    startshell=time.clock()
    gap = len(s)/2 - 1
    while(gap>=1):
	for i in range(gap,len(s)):
	    j = i-gap
	    temp=s[i]
	    while(j>=0 and s[j]>temp):
		s[j+1]=s[j]
		j=j-gap
	    s[j+gap]=temp
	gap=(gap+1)/2-1
    endshell=time.clock()
    print '花的时间为 '+str(endshell-startshell)    
    return s
     
