# FlattenList
FlattenList is the code to perform Flattening on a List in Python3.


## Algorithm
Flatten_List(initialList, finalList)
1. Iterate over the initialList (for loop).
2. For ever element of initialList, check if the element is a list.
3. If No, then add the element in the finalList.
4. If Yes, then make a recursive call to the function (flattenList) with current element of initialList and finalList as arguments.
5. Finally, the finalList generated is the desired list, i.e. Flatten List.
