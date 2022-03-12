"""
Problem Statement
ARS builders has the plan of constructing new buildings with the sections of land they have. Each section has 2 plots on either sides of the road.
Given an input number of sections . The task is to find out all the possible ways for constructing buildings in the plots such that there is a space between any 2 buildings.
Note:
A new building can be placed on a section if the section just before it has space. A space can be placed anywhere (it doesn’t matter whether the previous section has a building or not).
Write a python function to return the total number of possible ways for constructing the buildings.

Sample Input           Expected Output

n- 3                       25
Example:
No of sections=3,which means possible ways for one side are BSS, BSB, SSS, SBS, SSB where B represents a building and S represents an empty space. Total possible ways are 25, because a way to place on one side can correspond to any of 5 ways on other side.
Possible ways of constructing the buildings: 25
"""
#lex_auth_012751752635383808104
def count_ways(n): 
    a=[0 for i in range(n)]

    b=[0 for i in range(n)]

    a[0] = b[0] = 1

    for i in range(1,n):

        a[i] = a[i-1] + b[i-1]

        b[i] = a[i-1]

     

    return (a[n-1] + b[n-1])**2 
    
    '''if (N == 1) :

        # 2 for one side and 4 

        # for two sides

        return 4
 

    # countB is count of ways with a 

    # building at the end 

    # countS is count of ways with a

    # space at the end 

    # prev_countB and prev_countS are 

    # previous values of 

    # countB and countS respectively. 
 

    # Initialize countB and countS 

    # for one side 

    countB=1

    countS=1
 

    # Use the above recursive formula 

    # for calculating 

    # countB and countS using previous values 

    for i in range(2,N+1) :

     

        prev_countB = countB

        prev_countS = countS
 

        countS = prev_countB + prev_countS

        countB = prev_countS

     
 

    # Result for one side is sum of ways 

    # ending with building 

    # and ending with space 

    result = countS + countB
 

    # Result for 2 sides is square of 

    # result for one side 

    return (result*result)'''
 
    #start writing your code here


n= 5
print("Number of possible ways in which buildings can be constructed is: ",count_ways(n))
