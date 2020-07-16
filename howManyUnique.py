import numpy as np

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
    return arr


f = open("firstCommitDifference.txt", "r")
fullList = f.read().split()
myList = []
for i in range(len(fullList)):
    print("Iteration " + str(i))
    if fullList[i] not in myList:
        myList.append(fullList[i])

myList = insertionSort(myList)

for i in range(len(myList)):
    print(myList[i])
