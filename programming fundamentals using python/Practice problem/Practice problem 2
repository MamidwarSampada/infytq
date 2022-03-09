"""
Problem Statement
Write a python function which accepts a string containing a pattern of brackets and returns true if the pattern of brackets is correct. Otherwise it returns false.
The string of brackets is correct if it satisfies the following conditions:
1. Number of opening and closing brackets are equal.
2. Pattern should not start with closing bracket and end with opening bracket.

Sample Input                   Expected Output

)()((()())                        False

()((())())                        True
"""
#lex_auth_0127135773590405121141

def bracket_pattern(input_str):
    #Remove pass and write your code here
	if input_str.startswith(')') or input_str.endswith('('):
	    return False
	elif input_str.count('(')==input_str.count(')'):
	    return True
	return False

    
input_str="(())("
print(bracket_pattern(input_str))
