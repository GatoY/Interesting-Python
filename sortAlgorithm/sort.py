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
    print '花的时间为 '+str(endinsert-startinsert)+' s'
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
    print '花的时间为 '+str(endshell-startshell)+' s'    
    return s

# Lomuto partitioning sort.
def partitionsort(s):
    startpartition=time.clock()
    p=s[0]
    x=0
    for i in range(1,len(s)):
	if s[i]<p:
	    x=x+1
    	    temp=s[i]
	    s[i]=s[x]
	    s[x]=temp
    temp=s[0]
    s[0]=s[x]
    s[x]=temp
    endpartition=time.clock()
    print '花的时间为 '+str(endpartition-startpartition)+' s'
    return s

def hoarepartition(s,lo,hi):
    p=s[lo]
    i=lo
    j=hi
    while(i<j):
	while (i<hi and s[i]<=p):
	    i=i+1
    	while (j>=lo and s[j]>=p):
	    j=j-1
	temp=s[i]
	s[i]=s[j]
	s[j]=temp
    temp=s[i]
    s[i]=s[j]
    s[j]=temp
    s[lo]=s[j]
    s[j]=p
    return j
     
def quicksortf(s,lo,hi):
    if lo<hi:
	p=hoarepartition(s,lo,hi)
	quicksortf(s,lo,p-1)
	quicksortf(s,p+1,hi)
 


