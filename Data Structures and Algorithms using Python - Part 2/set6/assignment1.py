"""
Problem Statement
Given a list of digits. The task is to find out the number of possible decoding of the given digit sequence.
Assume that the input list contains valid digits from 0 to 9 and there are no leading 0's, no trailing 0's and no two or more consecutive 0's in the input list.
Let 1 represent 'A', 2 represent 'B', …, 26 represent 'Z'.
Write a python function which accepts the list of digits and returns the total number of decoding possible from given digit sequence.

Sample Input                     Expected Output                                 Remark

digit_list=[1 ,2 ,2 ,4]                5                           The possible decoding are "ABBD", "LBD", "AVD", "ABX","LX"

digit_list=[1 ,2 ,2]                   3                            The possible decoding are "ABB", "LB", "AV"
"""
#lex_auth_0127667393053655043361
def count_decoding(digit_list): 
    n=len(digit_list)
    #Remove pass and write your logic here
    count = [0] * (n + 1); # A table to store 

                           # results of subproblems 

    count[0] = 1; 

    count[1] = 1; 
 

    for i in range(2, n + 1): 
 

        count[i] = 0
 

        # If the last digit is not 0, then last

        # digit must add to the number of words 

        if (digit_list[i - 1] > 0):

            count[i] = count[i - 1]
 

        # If second last digit is smaller than 2

        # and last digit is smaller than 7, then

        # last two digits form a valid character 

        if (digit_list[i - 2] == 1 or

           (digit_list[i - 2] == 2 and

            digit_list[i - 1] < 7) ): 

            count[i] += count[i - 2] 
 

    return count[n]

#Pass different values to the function and test your program
digit_list=[9,8,1,5]
print("Number of possible decodings for the given sequence is:",count_decoding(digit_list))
