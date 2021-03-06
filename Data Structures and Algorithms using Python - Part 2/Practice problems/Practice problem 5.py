"""
Problem Statement
Write a python function which accepts two linked list containing integer data sorted in increasing order and returns a new linked list containing common elements from the two linked lists.
Assume that there always be at least one element in common between the two linked lists.

Sample Input                  Expected Output

list1- 1->2->3->4->5->6
                              2->4->6
list2- 2->4->6->8
"""
#lex_auth_01275171685269504062
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

def sorted_intersection_of_lists(list1,list2):
    #start writing your code her
    l1=[]
    l2=[]
    temp=list1.get_head()
    while(temp is not None):
        l1.append(temp.get_data())
        temp=temp.get_next() 
    temp=list2.get_head()
    while(temp is not None):
        l2.append(temp.get_data())
        temp=temp.get_next() 
    print(l1,l2) 
    g=LinkedList()
    for i in l1:
        if i in l2:
            g.add(i)
    return g
       
   
list1=LinkedList()

list1.add(1)
list1.add(2)
list1.add(3)
list1.add(4)
list1.add(5)
list1.add(6)

list2=LinkedList()
list2.add(2)
list2.add(4)
list2.add(6)
list2.add(8)
 
intersected_list=sorted_intersection_of_lists(list1, list2)
intersected_list.display()
