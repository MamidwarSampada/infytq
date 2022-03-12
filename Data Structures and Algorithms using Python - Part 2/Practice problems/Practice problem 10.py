"""
Problem Statement
Given a stack of lunch boxes maintained in a container, identify the number of lunch boxes of a given color belonging to a manufacturer.
Write a python program to implement the class diagram given below.
Class Description - Container:
box_stack: Stack of lunch boxes where each element in the stack is a lunch box
identify_count(color): Accept a color and return a dictionary containing the name of the manufacturer (key) and count of lunch boxes (value) of mentioned color.
If a lunchbox with the specified color is not found, return 0.
Perform case insensitive string comparison.
Create objects of LunchBox class, push the LunchBox objects into a stack. Create an object of Container class by using the stack created and test your program by invoking the method, identify_count(color).
"""
#lex_auth_01275172151871897677
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
class LunchBox:
    def __init__(self,color,manufacturer): 
        self.__color=color
        self.__manufacturer=manufacturer
    def get_color(self):
        return self.__color
    def get_manufacturer(self):
        return self.__manufacturer 
    def __str__(self):
        print(self.__color+''+self.__manufacturer) 
class Container:
    def __init__(self,box_stack):
        self.__box_stack=box_stack 
    def get_box_stack(self):
        return self.__box_stack 
    def identify_count(self,color):
        l=[]
        d={}
        while self.__box_stack.is_empty()==False:
            l.append(self.__box_stack.pop())  
        r=0
        for i in l:
            if i.get_color()==color.title(): 
                r+=1
                if i.get_manufacturer() in d: 
                    d[i.get_manufacturer()]+=1 
                else: 
                    d[i.get_manufacturer()]=1
        if r>0:
            return d
        return 0
            
        

#start writing your code here
