"""
Problem Statement
Given a stack of integers, write a python program that updates the input stack such that all occurrences of the smallest values are at the bottom of the stack, while the order of the other elements remains the same.

For example:
Input stack (top-bottom) :   5 66  5  8  7
Output:  66  8  7  5  5
 """
#lex_auth_0127438990347550721631

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg
        
        
def change_smallest_value(number_stack):
    #write your logic here 
    l=[]
    while number_stack.is_empty()==False: 
        l.append(number_stack.pop()) 
    m=min(l) 
    c=l.count(m) 
    l.reverse() 
    for i in range(c): 
        number_stack.push(m)
    for i in l: 
        if i!=m: 
            number_stack.push(i) 
    
        
    

    return number_stack

#Add different values to the stack and test your program
number_stack=Stack(8)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(66)
number_stack.push(5)
print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()
