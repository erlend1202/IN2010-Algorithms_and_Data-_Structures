#Storing the start node
K = int(input())
#Creating two lists, one for storing the entire tree structure, and one 
#for storing the path down the tree
full_list = []
output_list = [K]

#Looping through the inputs until i have stored -1 in my list, then i stop
statement = True
while (statement):
    string = input()   
    split_string = string.split(" ")
    temp_list = []
    for number in split_string:
        temp_list.append((int(number)))

    full_list.append(temp_list)    
    if string == "-1":
        statement = False
        
current_node = K 
i = 0


statement = True
#Looping through the entire list to find the parent node to our current node
#if it doesnt hit, we know the cat is all the way down, and we can therefore stop
while(statement):
    statement = False        
    for i in range(0, len(full_list)):
        for j in range(1,len(full_list[i])):
            if full_list[i][j] == current_node:
                current_node = full_list[i][0]
                output_list.append(current_node)
                statement = True

#Printing the path in the format specified by the task
for i in output_list:
    print (i, end= ' ')