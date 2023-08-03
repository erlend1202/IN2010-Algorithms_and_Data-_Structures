import numpy as np
import math as math
from collections import deque

#Creating a list to store the inputs from a input file
ls = []
statment = True
while (statment):
    try: 
        k = int(input())
    except:
        break

    ls.append(k)

#Making an array out of this list, to make it faster    
arr = np.array(ls)
output = deque([])

"""
Function for arranging a sorted array in such a way, that we can make
a balanced tree by going left to right in the array. The function will
first finish the right side of the tree, then the left side of the tree.

Parameters:
-----------

arr: the sorted array in which you want to solve for

fill: an empty list to store the output data
"""
def balanced_tree(arr, fill):
    length = len(arr)
    if length < 1:
        return 0

    #calculating the mid value, to then use as 'root'
    mid = math.floor((length)/2)   
    
    #appending in mid value to the list
    fill.append(arr[mid])

    #Splitting our array in two parts, excluded of the mid value
    arr_left = arr[0:mid]
    arr_right = arr[mid+1:length]

    #Checking if the right side array is smaller or equal to 2, in which
    #case we dont need to split it, and can just append in the values left
    if (length - mid - 1) <= 2:
        if (length - mid - 1) == 2:
            fill.append(arr_right[1])
        fill.append(arr_right[0])

    #Checking if right side array is larger than 2, in which case we send it
    #throug the program again
    if (length - mid - 1) > 2:
        balanced_tree(arr_right, fill)

    #Doing exactly the same as we did with right side array, just
    #this time with left side array
    if (mid) <= 2:
        if (mid) == 2:
            fill.append(arr_left[1])
        fill.append(arr_left[0])

    #and again, as long as the left side array is larger than 2, we call 
    #the function again
    if (mid) > 2:
        balanced_tree(arr_left, fill)


#Calling the function
balanced_tree(arr, output)

#printing in format as expected from the task
for i in output:
    print(i)