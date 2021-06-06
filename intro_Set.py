''' creating a set in pyhton
A set is unordered collections of items.
It is immutableand having no duplicates value means to says that it is having unique value
'''


A_set={'hello',2,3,4,5,6,7,8,'python'}
print(A_set,type(A_set))

# creating a empty set in python is bit tough

A_set={}
print(A_set,type(A_set))
# it gives the dict type in the python console but at here we have to print a empty set so,
A_set=set()
print(A_set,type(A_set))

# unique in nature
a={'hello',2,2,3,4,5,6,7,8,'python'}
print(a)

# set does not follow the indexing

a={'hello',2,2,3,4,5,6,7,8,'python'}
c=a[0]
print(c)

# methods in sets(python)

# 1.add a element in the set
a={'hello',2,2,3,4,5,6,7,8,'python'}
s=a.add('gla')
print(a)

#remove any element from any set

a={'hello',2,2,3,4,5,6,7,8,'python'}
s=a.remove('python')
print(a)

#clear the all elements in the set

a={'hello',2,2,3,4,5,6,7,8,'python'}
a.clear()
print(a)

# union in set

a={'hello',2,2,3,4,5,6,7,8,'python'}
b={9,2,4,'GLA'}
s=a|b
print(s)

# set interjection

a={'hello',2,2,3,4,5,6,7,8,'python'}
b={9,2,4,'GLA'}
s=a&b
print(s)

#set difference

a={'hello',2,2,3,4,5,6,7,8,'python'}
b={9,2,4,'GLA'}
s=a-b
print(s)

#set symmetric difference

a={'hello',2,2,3,4,5,6,7,8,'python'}
b={9,2,4,'GLA'}
s=a^b
print(s)

