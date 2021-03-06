"""
roblem Statement
A group of students are waiting in a queue to collect their exam hall tickets from their teacher.
But due to heavy crowd, the teacher announced that the students should form two new queues – 
Queue1:students whose names start with "S" and end with "a" queue and 
Queue2:remaining students
The sequence should be maintained in both the queues as per the original queue.
Write a python function which accepts the original queue and returns a list of queues such that Queue1 is at index position 0 and Queue2 is at index position 1.
Perform case sensitive string comparison.
Assume that both the output queues have the same size as that of the input queue.

Sample Input                                                                                                                        Expected Output

Queue: front->rear("Andy", "Sana", "Nick", "Sam", "George","Veronica", "Samar", "Serena", "Roger", "Shanaya")    [ Queue("Sana","Serena","Shanaya"), Queue("Andy", "Nick","Sam","George", "Veronica", "Samar", "Roger") ]
"""
#lex_auth_01275171071766528059
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


def hall_ticket_collection(queue1): 
    l=[]
    SA_queue=Queue(queue1.get_max_size())
    other_queue=Queue(queue1.get_max_size())
    
    while queue1.is_empty()==False:
        l.append(queue1.dequeue())
    for i in l: 
        if i[0]=='S' and i[-1]=='a':
            SA_queue.enqueue(i) 
        else:
            other_queue.enqueue(i)
        
    #start writing your code here


    return [SA_queue,other_queue]
        
    
queue1=Queue(10)
queue1.enqueue("Andy")
queue1.enqueue("Sana")
queue1.enqueue("Nick")
queue1.enqueue("Sam")
queue1.enqueue("George")
queue1.enqueue("Veronica")
queue1.enqueue("Samar")
queue1.enqueue("Sarena")
queue1.enqueue("Roger")
queue1.enqueue("Shanaya")

result=hall_ticket_collection(queue1)

for i in result: 
    print("The elements in the new queue are:")   
    i.display()
