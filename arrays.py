# study the  

from array import *

# 1. create an array and traverse.

myarray = array('i',[1,2,3,4,5])
for i in myarray:
	print(i)

# 2. access individual elements through indexes

print("step 2")
print(myarray[3])

# 3. appaend any value to the array using append() method

print ("step 3")
myarray.append(6)
print(myarray)

# 4. insert value in array using insert() method, you cant use this to add the same number

print("step 4")
myarray.insert(3,11)
print(myarray)

# 5. extend python arrayusing extend() method

print("step 5")
myarray1 = array('i', [10,11,12])
myarray.extend(myarray1)
print(myarray)

# 6. add items from list into array using fromlist() method

print("step 6")
templist = [20,21,22]
myarray.fromlist(templist)
print(myarray)

# 7. remove any array element using remove() method

print("step 7")
myarray.remove(11)
print(myarray)

# 8. Remove last array element using pop() method

print("step 8")
myarray.pop()
print(myarray)

# 9. fetch any element through it's index using index() method

print("step 9")
print(myarray.index(21)) 

# 10. reverse a python array using reverse() method 

print("step 10")
myarray.reverse()
print(myarray)

# 11. get array buffer information through buffer_info() method

print("step 11")
print(myarray.buffer_info())

# 12. check for number of occurences using the count() method

print("step 12")
myarray.append(11)
print(myarray.count(11))
print(myarray)

# 13. convert array to string using tostring() method and use fromstring() method

print("step 13")
strtemp = myarray.tostring()
print(strtemp)
ints = array('i')
ints.fromstring(strtemp)
print(ints)

# 14. convert an array to list using tolist() method

print("step 14")
print(myarray.tolist())

# 15. slice elements from an array
print("step 16")

print(myarray[1:4])
print(myarray[:4])
print(myarray[2:4])
print(myarray[:])
print(myarray[3:4])