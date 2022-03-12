"""
Problem Statement
Given two queues, one integer queue and another character queue, write a python program to merge them to form a single queue.  Follow the below rules for merging:
Merge elements at the same position starting with the integer queue.
If one of the queues has more elements than the other, add all the additional elements at the end of the output queue.
Note : max_size of the merged queue should be the sum of the size of both the queues. 
For example,  
Input -- queue1: 3,6,8     queue2: b,y,u,t,r,o
Output -- 3,b,6,y,8,u,t,r,o
"""
#lex_auth_0127438930044108801627

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

def merge_queue(queue1,queue2): 
    merged_queue=Queue(queue1.get_max_size()+queue2.get_max_size()) 
    while queue1.is_empty()==False and queue2.is_empty()==False:  
        a=queue1.dequeue()
        b=queue2.dequeue()
        merged_queue.enqueue(a) 
        merged_queue.enqueue(b) 
    
    while queue1.is_empty()==False: 
        a=queue1.dequeue() 
        merged_queue.enqueue(a) 
    while queue2.is_empty()==False: 
        b=queue2.dequeue() 
        merged_queue.enqueue(b)
    #write your logic here
    return merged_queue
    
'''OTHER SOLUTION '''
merged_queue=Queue(queue1.get_max_size()+queue2.get_max_size())
    while queue1.is_empty()==False or queue2.is_empty()==False:
        if queue1.is_empty() and queue2.is_empty():
            pass
        elif queue1.is_empty(): 
            merged_queue.enqueue(queue2.dequeue())
        elif queue2.is_empty():
            merged_queue.enqueue(queue1.dequeue())
        else:
            merged_queue.enqueue(queue1.dequeue())
            merged_queue.enqueue(queue2.dequeue())
            
            
    return merged_queue

#Enqueue different values to both the queues and test your program

queue1=Queue(3)
queue2=Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merged_queue=merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merged_queue.display()
