import math as math
import heapq


#Creating a list to store the inputs from a input file
ls = []
statment = True
while (statment):
    try: 
        k = int(input())
    except:
        break

    ls.append(k)
    
#heapifying the list
heapq.heapify(ls)

"""
Function for printing info from a heap in such a way, that we can make
a balanced tree from the print output, by reading top to bottom. 
The function will first finish the right side of the tree, then 
the left side of the tree.

Parameters:
-----------

arr: the sorted array, which is now heapified in which you want to solve for.

"""
def balanced_tree(arr):
    length = len(arr)
    if length < 1:
        return 0

    mid = math.floor((length)/2)   
    
    print(arr[mid])

    arr_left = arr[0:mid]
    arr_right = arr[mid+1:length]

    if (length - mid - 1) <= 2:
        if (length - mid - 1) == 2:
            print(arr_right[1])
        print(arr_right[0])
        

    if (length - mid - 1) > 2:
        balanced_tree(arr_right)

    
    if (mid) <= 2:
        if (mid) == 2:
            print(arr_left[1])
        print(arr_left[0])


    if (mid) > 2:
        balanced_tree(arr_left)


balanced_tree(ls)