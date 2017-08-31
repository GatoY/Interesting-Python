import random
# return random int array.
def ints(n,min,max):
    s=[]
    for i in xrange(n):
	s.append(random.randint(min,max))
    return s

# return random float.
def floats(n,min,max):
    s=[]
    for i in xrange(n):
	s.append(random.uniform(min,max))
    return s

