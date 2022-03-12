"""
Problem Statement
Write a python function which accepts two linked lists containing integer data and an integer, n and merges the two linked lists, such that list2 is merged with list1 after n number of nodes.

Assume that value of n will always be less than or equal to the number of nodes in list1.

Sample Input                              Expected Output

list1- 1->2->4->3->5
list2- 9->8->11                       1->2->9->8->11->4->3->5
n- 2                              
"""
#lex_auth_01275171910432358466
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

def skip_n_merge_list(list1,list2,n):
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
    a=l1[:n]
    b=l1[n:]
    a.extend(l2)
    a.extend(b)

    list1=LinkedList()
    for i in a:
        list1.add(i)
    return list1

list1=LinkedList()
list1.add(1)   
list1.add(2)  
list1.add(4)  
list1.add(3)
list1.add(5) 

list2=LinkedList()
list2.add(9)
list2.add(8)
list2.add(11)
merged_list=skip_n_merge_list(list1, list2,2)
merged_list.display()
