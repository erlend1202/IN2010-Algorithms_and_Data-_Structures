from collections import deque
import math as math

#Creating a class teque using the pre existing structure deque
class teque:
    def __init__(self, length=0):
        self.list = deque([])
        self.length = length

    def push_back(self, x):
        self.list.append(x)
        self.length = self.length + 1

    def push_front(self, x):
        self.list.appendleft(x)
        self.length = self.length + 1


    def push_middle(self, x):
        self.list.insert(math.floor((self.length + 1)/2), x)
        self.length = self.length + 1

    def get(self, i):
        print(self.list[i])


#Creating an instanse of the class teque
teque_list = teque()

#Finding number of string inputs 
N = int(input())
#Looping through the number of inputs, and doing an action for each one,
#based on the length of the string
for i in range(0,N):
    string = input()
    split_string = string.split(" ")
    length = len(split_string[0])
    value = int(split_string[1])
    if length == 9:
        teque_list.push_back(value)
    elif length == 10:
        teque_list.push_front(value)
    elif length == 11:
        teque_list.push_middle(value)
    elif length == 3:
        teque_list.get(value)            