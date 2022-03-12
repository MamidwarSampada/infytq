"""
Problem Statement
Consider an input_queue containing characters as elements and an input_stack containing integers (integers can be either 1 or 2 only). 
Example for input_queue (Front -> Rear): A, B, C 
Example for input_stack (Top -> Bottom): 2, 1, 2 
Write a function which takes input_queue and input_stack as input parameters and returns an output_queue which contains the elements of the input_queue but in a different order. The ordering of elements in output_queue is determined by the elements of input_stack as mentioned below – 
For every element in the input_stack, input queue is reordered based on the below rule –
If the element is 1, then the first element in the input_queue (element at front) will become last element (element at rear).
If the element is 2, then the last element (element at rear) in the input_queue will become the first element (element in front).

Example: 
input_queue(Front -> Rear): A, B, C 
input_stack (Top -> Bottom): 2, 1, 2 
output_queue (Front -> Rear): C, A, B

Step 1: For the first element in the input_stack that is 2, the last element in the input_queue that is 'C' is moved to the front, so the input_queue is now reordered as (Front -> Rear) C, A, B. 
Step 2: For the second element in the input_stack that is 1, the first element in the reordered input_queue as per step 1 that is 'C' is moved to the rear of the input_queue, the input_queue is now reordered as (Front -> Rear) A, B, C 
Step 3: For the last element in the input_stack that is 2, the last element in the reordered input_queue as per step 2 is 'C' is moved to the front, so the input_queue is now reordered as (Front -> Rear) C, A, B 
Step 4: The output_queue should contain the elements as per step 3 which is as (Front -> Rear) C, A, B 

Assumption:
input_queue and input_stack will always contain at least one element each
input_queue will always contain single character strings
The elements in the input_stack can be either 1 or 2

Sample Input and Output:

input_queue(Front->Rear)     input_stack(Top->Bottom)         output_queue(Front->Rear)

'A'                                  1                                 'A'
'A','B','C'                          1,2,1                          'B','C','A'
'x','y','z','o','t'                  1,1,1                       'o','t','x','y','z'
'X','a','B','C'                      1,2,1,2                       'X','a','B','C'
"""
#lex_auth_012761717559443456689
"""*********************Queue*****************************"""
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

"""*********************Stack*****************************"""
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


"""*********************Linkedlist************************"""
class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail


    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list")

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

def queue_ordering(input_queue,input_stack):
    #Do not modify the size of output_queue
    output_queue=Queue(input_queue.get_max_size())
    s=[]
    q=[]
    while not input_stack.is_empty():
        s.append(input_stack.pop())
    while not input_queue.is_empty():
        q.append(input_queue.dequeue()) 
    for i in s:
        if i==1:
            q.append(q[0])
            q.remove(q[0])
        elif i==2:
            l=[q[-1]]
            l.extend(q)
            l.pop(-1) 
            q=l
    for i in q: 
        print(q)
        output_queue.enqueue(i)
            
            
    #Write your code here
    return output_queue

#You may modify the below code for testing
input_stack=Stack(5)
input_stack.push(1)
input_stack.push(2)
input_stack.push(1)
input_stack.push(1)
input_stack.push(1)

input_queue=Queue(3)
input_queue.enqueue('A')
input_queue.enqueue('C')
input_queue.enqueue('B')
output_queue=queue_ordering(input_queue, input_stack)
output_queue.display()

