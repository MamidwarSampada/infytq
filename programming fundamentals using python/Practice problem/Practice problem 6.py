"""
Problem Statement
Write a python function which accepts a list of numbers and returns true, if 1, 2, 3 appears in sequence in the list.
Otherwise, it should return false.

Sample Input               Expected Output

[1, 1, 2, 3, 1]               True

[1, 1, 2, 4, 3]              False
"""
#lex_auth_0127135869481369601150

def list123(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False
    #start writing your code here

    

nums=[1,2,3,4,5]
print(list123(nums))
