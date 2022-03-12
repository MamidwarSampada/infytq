"""
Problem Statement
[Cornell University CS1110 Final Exam 2014 Spring]
Write a recursive python function which returns True if the input is well-formatted with respect to the list labels. Else it should return False.
We say that an input is well-formatted with respect to the labels if:
(a) input item is a list 
(b) input item has length at least two 
(c) input’s first item is in the list labels 
(d) each of the remaining items in input is either a string or a well-formatted list 

                     Sample input                                              Expected output

 input item                                list label

['VP', ['V', 'eat']]                      ['VP', 'V']                              True

['NP', ['N', 'a', 'or', 'b'], 'c']      ['NP', 'V', 'N']                           True

[1, [2, 'oui', [1, 'no']], 'no']             [1,2]                                 True

['VP', ['V', 'eat']]                         ['VP']                                False

['VP', ['V']]                              ['VP', 'V']                             False
"""
#lex_auth_0127136426924195841210

def check_well_formatted(input_item,list_label): 
    if(type(input_item)!=list
    	or (len(input_item)<2)
    		or (input_item[0] not in list_label)):
    			return False
    else:
    	for item in input_item[1:]:
    			         
    			         if type(item) != str and not check_well_formatted(item, list_label):
    			             print(item)
    			             return False
    			     
    	
    	return True
    #Start writing your code here


input_list1=['VP', ['V', 'eat']]
list_label1=['VP', 'V']
result=check_well_formatted(input_list1,list_label1)
if result is True:
    print("Well formatted")
else:
    print("Not Well formatted")
