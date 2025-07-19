#Let's learn SET

#Creating a set 
#style 01:
set1= {1,2,3,4,5}
set2= {"Apple","Banana","Cherry"}
set3= {False, True}
set4= {1,2,"Apple", True}

#style: 02
set5= set((1,2,3,4,5))
set6= set(("Apple","Banana","Cherry"))
set7= set((False, True))
set8= set((1,2,"Apple", True))

#Printing the set
print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
print(set6)
print(set7)
print(set8)

"""gOutput
{1, 2, 3, 4, 5}
{'Cherry', 'Apple', 'Banana'}
{False, True}
{1, 2, 'Apple'}
{1, 2, 3, 4, 5}
{'Cherry', 'Apple', 'Banana'}
{False, True}
{1, 2, 'Apple'}
3
<class 'set'>"""

#Extra
print(len(set4))     #length of the set
print(type(set4))   #type of the set
 