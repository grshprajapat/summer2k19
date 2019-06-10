#!/usr/bin/python3
adhoc = [1,2,3,1,4,5,66,22,2,6,0,9]
print ("The list : " + str(adhoc))
k=5
j=3
print ("the num which are greater than 5")
l=[i    for i in adhoc	if i>k   ]
print(l)
print ("the num less or equal to 2")
m=[i    for i in adhoc   if i<j   ]
print(m)
