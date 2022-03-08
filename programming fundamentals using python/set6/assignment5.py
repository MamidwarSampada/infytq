"""
Problem Statement
A 10-substring of a number is a substring of its digits that sum up to 10.
For example, the 10-substrings of the number 3523014 are:
3523014, 3523014, 3523014, 3523014
Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.
Handle the possible errors in the code written inside the function.

Sample Input                  Expected Output

'3523014'               ['5230', '23014', '523', '352']
"""
#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    l=[]
    for i in range(len(num_str)):
        s=int(num_str[i])
        m=num_str[i]
        for j in range(i+1,len(num_str)):
            s+=int(num_str[j])
            m+=num_str[j]
            if s==10:
                l.append(m)
                
    return list(set(l))
            
            
    #Remove pass and write your logic here

num_str="3523014"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
