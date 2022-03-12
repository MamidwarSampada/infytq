"""
Problem Statement
Mega Mart, a retail shop, wants to record the number of items bought by its customers.
Write a python program to implement the class diagram given below.

Class Description:

list_of_items: Static list which contains the list of items available in the store. Initialize it with sample data as given - [Cake, Soap, Jam, Cereal, Hand Sanitizer, Biscuits, Bread]
list_of_count_of_each_item_sold: Static list which contains count of items sold. Initialize count of each item to 0
The above two lists have one-to-one correspondence
items_purchased: List which contains the list of items purchased by the customer. Initialize it to an empty list in the constructor
item_on_offer: Name of the item provided as an offer. Initialize it to None in the constructor
provide_offer(): The shop has decided to give 1 Hand sanitizer free if soap is bought by the customer
Increment the count of hand sanitizer in list_of_count_of_each_item_sold by 1
Update the instance variable, item_on_offer to "HAND SANITIZER"
sell_items(list_of_items_to_be_purchased): Accept the list of items that are to be purchased by the customer
For every item in list_of_items_to_be_purchased
Increment count of the item in the static list, list_of_count_of_each_item_sold by 1
Add the item to attribute, items_purchased list
If soap is purchased by the customer, then provide the offer by invoking the appropriate method
find_total_items_sold(): Return the total number of items sold by the shop

Note:
Perform case insensitive string comparison 
Assume that customer purchases only 1 quantity of each item and an item will appear only once in the list, list_of_items_to_be_purchased

For testing:
Create objects of Purchase class
Invoke sell_items() on Purchase object by passing the list of items to be purchased by the customer
Display the details
"""
#lex_auth_0127390120635678722716
#Start writing you code her
class Purchase:
    list_of_items=["Cake","Soap","Jam","Cereal","Hand Sanitizer","Biscuits","Bread"]
    list_of_count_of_each_item_sold=[0,0,0,0,0,0,0]
    def __init__(self):
        self.__items_purchased=[]
        self.__item_on_offer=None
    def get_items_purchased(self):
        return self.__items_purchased
    def get_item_on_offer(self):
        return self.__item_on_offer
        
    def provide_offer(self):
        if "Soap".title() in self.__items_purchased:
            Purchase.list_of_count_of_each_item_sold[Purchase.list_of_items.index("Hand Sanitizer")]+=1
            self.__item_on_offer="Hand Sanitizer"
    
    def sell_items(self,list_of_items_to_be_purchased): 
        for i in list_of_items_to_be_purchased: 
            if i.title() in Purchase.list_of_items: 
                Purchase.list_of_count_of_each_item_sold[Purchase.list_of_items.index(i.title())]+=1 
                self.__items_purchased.append(i.title())
        if "soap".title() in list_of_items_to_be_purchased:
            self.provide_offer() 
    @staticmethod
                
    def find_total_items_sold(): 
        s=sum(Purchase.list_of_count_of_each_item_sold)
        return s
    
p=Purchase()
p.sell_items(["jam","Bread"])
print(Purchase.find_total_items_sold())
print(p.get_item_on_offer())
print(p.get_items_purchased())
    
    
