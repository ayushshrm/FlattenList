# Python program to Flatten a List

# function flatten_list() takes two arguments "initialList" and "finalList"

def flatten_list(initialList, finalList):
    # loop iterates over the elements present in initialList
    for i in range(len(initialList)):
        
        # The condition checks whether the "type" of initialList is not of <class 'list'>
        if str(type(initialList[i]))!="<class 'list'>":         
            
            # if true the element is simply appended to the finalList
            finalList.append(initialList[i])                    
        
        else:
            
            # if false, i.e. the elements at the ith index of initialList is a list, 
            # a recursive call is given to the function flatten_list(), 
            # with the element as the second argument
            flatten_list(initialList[i],finalList)              

# all the manipulations in the list at each recursive call are reflected 
#in the actual list and can be accessed outside the function

inputList=[[1,2,3,[30,40,50],100],[4,5,6],7,8]              
finalList=[]

flatten_list(inputList,finalList)
print(finalList)
