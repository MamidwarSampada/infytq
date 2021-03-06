"""
Problem Statement
PizzaForYou is a pizza store which sells different kinds of pizzas based on customer's order.
Customer can either collect the order in person or opt for a door delivery.
Write a python program based on the class diagram given below.

Customer class:
validate_quantity(): A customer can order 1 to 5 pizzas
If quantity is valid, return true. Else return false

Pizzaservice class:
Initialize static variable counter to 100
Attribute, additional_topping is a boolean value which indicates whether additional topping is required or not.True – additional topping is required, False – additional topping is not required
validate_pizza_type(): Customers can order "small" or "medium" type pizzas
If pizza type is valid, return true. Else return false
calculate_pizza_cost(): Calculate pizza cost
Validate pizza type and quantity
If valid,
Identify pizza cost based on details mentioned in the table
Set attribute, pizza_cost with the calculated pizza cost
Auto-generate service_id starting from 101 prefixed by first letter of pizza type. Example – S101, s102, m103, S104, M105 etc
If invalid, set pizza_cost to -1

PizzaType       Cost/Pizza(in Rs)                   Additional topping cost/Pizza (in Rs), if applicable

Small              150                                        35

Medium             200                                        50

Doordelivery class:
validate_distance_in_kms(): Minimum distance for door delivery is 1km and maximum is 10kms
Validate distance_in_kms
If valid, return true. Else, return false
calculate_pizza_cost: Calculate pizza cost
Validate distance in kms
If valid,
Calculate pizza cost (Hint: Invoke overridden method in parent class)
If pizza_cost is not -1, identify delivery charge based on details mentioned below and add it to attribute, pizza_cost

Distance in kms                 Delivery Charge in km(in Rs)

For first 5 kms                          5

For remaining 5 kms                      7

Else, set pizza_cost to -1
Note: Perform case insensitive string comparison  
For testing :
Create objects of Pizzaservice and Doordelivery classes
Invoke calculate_pizza_cost() on Pizzaservice and Doordelivery objects
Display the details
"""
#lex_auth_012737222539321344835
#Start writing your code here
class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity
        
    def get_quantity(self):
        return self.__quantity
        
    def get_customer_name(self):
        return self.__customer_name
        
    def validate_quantity(self):
        if 5>=self.__quantity>=1:
            return True
        return False
        
class Pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__additional_topping=additional_topping
        self.__pizza_type=pizza_type
        self.__customer=customer
        self.__service_id=None
        self.pizza_cost=-1
        
    def get_additional_topping(self):
        return self.__additional_topping
        
    def get_pizza_type(self):
        return self.__pizza_type
        
    def get_customer(self):
        return self.__customer
        
    def get_service_id(self):
        return self.__service_id
        
    def calculate_pizza_cost(self):
        d={"small":[150,35],"medium":[200,50]}
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            self.pizza_cost=d[self.__pizza_type.lower()][0]*self.__customer.get_quantity()
            Pizzaservice.counter+=1
            self.__service_id=self.__pizza_type[0]+str(Pizzaservice.counter)
            if self.__additional_topping==True:
                self.pizza_cost+=d[self.__pizza_type.lower()][1]*self.__customer.get_quantity()
        else:
            self.pizza_cost-1
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in ["small","medium"]:
            return True
        return False
        
class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        super(). __init__(customer,pizza_type,additional_topping)
        self.__delivery_charge=None
        self.__distance_in_kms=distance_in_kms
        
    def get_delivery_charge(self):
        return self.__delivery_charge
        
    def get_distance_in_kms(self):
        return self.__distance_in_kms
        
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost!=-1:
                if self.__distance_in_kms<=5:
                    self.pizza_cost+=5*self.__distance_in_kms
                else:
                    self.pizza_cost+=25+(7*(self.__distance_in_kms-5))
                    
        else:
            self.pizza_cost=-1
    
    def validate_distance_in_kms(self):
        if 1<=self.__distance_in_kms<=10:
            return True
        return False
