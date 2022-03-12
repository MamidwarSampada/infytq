"""
Problem Statement
LM Parking Lot wants to automate the process of calculating the parking charges for the vehicles parked. The parking lot can have limited number of vehicles and the vehicles parked can be only Two Wheeler or Four Wheeler. The vehicle that arrives first must be allowed to park first based on the parking space availability. The parking charge for a vehicle is calculated when it leaves the parking lot and any vehicle can leave the parking lot at any point of time.
Implement the class diagram given below.
LM Parking Lot wants to automate the process of calculating the parking charges for the vehicles parked. The parking lot can have limited number of vehicles and the vehicles parked can be only Two Wheeler or Four Wheeler. The vehicle that arrives first must be allowed to park first based on the parking space availability. The parking charge for a vehicle is calculated when it leaves the parking lot and any vehicle can leave the parking lot at any point of time.
Implement the class diagram given below.
Write a python program which implements the following functionalities.
Vehicle class maintains the vehicle details and ParkingLot class maintains the parking lot details.
total_no_of_lots specifies the total number of parking lots in the LM Parking Lot.
occupied_parking_lots is maintained as a linked list of vehicles. A new vehicle is always added at the end of the linked list based on the availability of total number of lots.
check_parking_availability(): It returns True if parking lot is available, otherwise it returns False.
Hint: The total number of vehicles in the occupied_parking_lots should be compared against the total_no_of_lots
allocate_parking_lot(): This method accepts the queue of vehicles as the input and allocates parking lot to the vehicles based on the availability. It should return the queue of vehicles, if there are any, for which the parking lots are not allocated.
Hint: If parking lot is available, each vehicle from the queue should be added to the end of the linked list. list_of_vehicles is a queue which contains the vehicles that are to be parked.
deallocate_parking_lot(): It de-allocates parking lot for a vehicle based on the registration number, and calculates the parking charges and returns a list which contains the vehicle details at index position 0 and its parking charge at index position 1. If the vehicle is not present in the parking lot then -1 should be returned.
Hint: Search the linked list for a vehicle with the specified registration number and remove it from the linked list.
calculate_parking_charge(): It returns the parking charge of the vehicle passed as an argument to it based on the following conditions:
If the vehicle is a two wheeler and if it has been parked for utmost 5 hours then the parking charge should be considered as Rs. 10. If the vehicle is a four wheeler and if it has been parked for utmost 5 hours then the parking charge should be considered as Rs. 20. If the vehicle, irrespective of the type, is parked for more than 5 hours then Rs. 10 per hour should be charged extra.
Perform case sensitive string comparison.
"""
#lex_auth_01275172530025267279
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

class Vehicle:
    def __init__(self,vehicle_type,registration_number,parking_hours): 
        self.__vehicle_type=vehicle_type 
        self.__registration_number=registration_number 
        self.__parking_hours=parking_hours 
    
    def get_vehicle_type(self):
        return self.__vehicle_type 
    def get_parking_hours(self):
        return self.__parking_hours 
    def get_registration_number(self):
        return self.__registration_number 

class ParkingLot: 
    occupied_parking_lots=LinkedList()
    def __init__(self,total_no_of_lots):
        self.__total_no_of_lots=total_no_of_lots 
    def get_total_no_of_lots(self): 
        return self.__total_no_of_lots 
    def check_parking_availability(self): 
        l=[]
        temp=ParkingLot.occupied_parking_lots.get_head() 
        
        while temp is not None:
            l.append(temp.get_data())
            temp=temp.get_next() 
        if len(l)<self.__total_no_of_lots:
            return True 
        return False
    def allocate_parking_lot(self,list_of_vehicles):
        while self.check_parking_availability():
            ParkingLot.occupied_parking_lots.add(list_of_vehicles.dequeue()) 
        return list_of_vehicles
    def deallocate_parking_lot(self,registration_number):
        l=[]
        temp=ParkingLot.occupied_parking_lots.get_head() 
        
        while temp is not None:
            l.append(temp.get_data())
            temp=temp.get_next()
        for i in l:
            if i.get_registration_number()==registration_number:
                c=self.calculate_parking_charge(i)
                g=[i,c] 
                ParkingLot.occupied_parking_lots.delete(i)
                return g
        return -1
                
                
            
    def calculate_parking_charge(self,vehicle):
        parking_charge=0
        if vehicle.get_vehicle_type()=='Two Wheeler':
            if vehicle.get_parking_hours()<=5:
                parking_charge=10
            else:
                parking_charge=10*(vehicle.get_parking_hours()-5)+10
        elif vehicle.get_vehicle_type()=='Four Wheeler':
            if vehicle.get_parking_hours()<=5:
                parking_charge=20
            else:
                parking_charge=10*(vehicle.get_parking_hours()-5)+20
        else:
            if vehicle.get_parking_hours()>5:
                parking_charge=(vehicle.get_parking_hours()-5)*10 
            else:
                parking_charge=10
        return parking_charge       
            
            
			
#start writing your code here
