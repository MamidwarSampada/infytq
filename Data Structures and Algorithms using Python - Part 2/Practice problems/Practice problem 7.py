"""
Problem Statement
Write a python function which accepts a stack of integers, sorts it in ascending order and returns the sorted stack.

Sample Input                             Expected Output

Stack:top->bottom (9,3,56,6,2,7,4)     Stack(2,3,4,6,7,9,56)
"""
#lex_auth_01275172167565312069
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
        
def sort_stack(stack1):
    l=[]
    #start writing your code here
    while stack1.is_empty()==False:
        l.append(stack1.pop())
    l.sort(reverse=True)
    for i in l:
        stack1.push(i)
    return stack1

stack1=Stack(7)
stack1.push(4)
stack1.push(7)
stack1.push(2)
stack1.push(6)
stack1.push(56)
stack1.push(3)
stack1.push(9)
result=sort_stack(stack1)
print("The sorted elements are:")
result.display()
