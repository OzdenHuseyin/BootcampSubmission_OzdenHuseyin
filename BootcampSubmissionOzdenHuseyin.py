#Task: Finding the most recurring number in a list

#1. Create Dictionairy
#2. Add all numbers into dictionary, without repetition
#3. Get max from dictionary by looping through each number in the dictionary

#List to search through
newList = [1,1,2,3,44,4,4,4,4]

#Empty dictionary (to store key : value pair)
myDic = {}

#iterating through each number in the dictionary.
#If a number exists already, add one to the count.
#Else, add new number to dictionary with a count of one.
for num in newList:
    if num in myDic:
        myDic[num] += 1

    else:
        myDic[num] = 1

#Cycle through each number in the dictionairy.
#If the number's "count" is larger than res, assign res to larger number.
res = 0
for num in myDic:
    if myDic[num] > res:
        res = num

#printing solution
print(res)
