# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:16:58 2021

@author: Admin
"""

""" O(1) constant time
It takes constant time to access first element. 
"""
array = [1,2,3,4,5]
array[0] 

"""O(N) linear
linear time since it is visiting every element of array.
"""
array = [1,2,3,4,5]
for element in array:
    print(element)
    
"""O(logN) logarithmic
logarithmic time since it is visiting only some elements.
"""
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for index in range (0, len (array),3):
    print(array[index])

"""O(N^2) Quadratic
looking at every index in hte array twice
"""
array = [1,2,3,4,5]
for x in array:
    for y in array:
        print(x,y)

        
"""O(2^N) exponential
double recursion in fibonacci
"""
def fibonacci(n):
    assert n >= 0 and int(n) == n, 'fibonacci number cannot be negative number or non integer' 
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(4))