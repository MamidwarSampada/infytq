"""
Problem Statement
Given a list of numbers, write a python function which returns true if one of the first 4 elements in the list is 9. Otherwise it should return false.
The length of the list can be less than 4 also.

Sample Input             Expected Output

[1, 2, 9, 3, 4]             True

[1, 2, 9]                   True

[1, 2,3,4]                  False
"""
#lex_auth_0127135811649044481146

def find_nine(nums):
    #Remove pass and write your code here
    if len(nums)>4:
        for i in range(4):
            if nums[i]==9:
                return True
        return False
    else:
        for i in range(len(nums)):
            if nums[i]==9:
                return True
        return False
        
    

nums=[1,9,4,5,6]
print(find_nine(nums))

 
