"""
Problem Statement
A teacher is in the process of generating few reports based on the marks scored by the students of her class in a project based assessment.
Assume that the marks of her 10 students are available in a tuple. The marks are out of 25.
Write a python program to implement the following functions:
1. find_more_than_average(): Find and return the percentage of students who have scored more than the average mark of the class.
2. generate_frequency(): Find how many students have scored the same marks. For example, how many have scored 0, how many have scored 1, how many have scored 3….how many have scored 25. The result should be populated in a list and returned.
3. sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values should be populated in a list and returned.

Sample Input                                                                    Expected Output

list_of_marks = (12,18,25,24,2,5,18,20,20,21)                                      70.0 
                                                                         [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 1]
                                                                         [2, 5, 12, 18, 18, 20, 20, 21, 24, 25]
 """
#lex_auth_01269438947391897654

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    l=[]
    avg=sum(list_of_marks)//len(list_of_marks)
    for i in list_of_marks:
        if i>avg:
            l.append(i)
    p=len(l)*10
    return p
    #Remove pass and write your logic here

def sort_marks():
    l=list(list_of_marks)
    l.sort()
    return l
    #Remove pass and write your logic here

def generate_frequency():
    l=[]
    for i in range(26):
        l.append(list_of_marks.count(i))
    return l
    #Remove pass and write your logic here

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
