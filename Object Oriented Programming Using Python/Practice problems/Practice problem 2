"""
Problem Statement
Little Puppy Kennel sells dogs of different breeds. They want to automate their selling process.
Write a python program to implement the class diagram given below.

Class Description:
dog_breed_dict: Static dictionary which contains the breed of the dog as key and the number of dogs available as value. Initialize it with the sample data given.
Initialize static variable counter to 100
breed_list: List of dog breeds required by the customer. Initialize it in the constructor
dog_id_list: List of dog ids. Initialize it to an empty list in the constructor
price: Total price to be paid by the customer. Initialize it to 0 in the constructor
accessories_required: Boolean value – True indicated accessories are required and False indicated accessories are not required.                          Initialize it in the constructor
validate_breed(): Return true if all the breeds required by the customer are available. Else return false
validate_quantity(): Return true if one dog/breed is available for all the breeds requested by the customer. Else return false
generate_dog_id(breed): Accept the breed of the dog for which dog id should be generated.                                                                                Auto-generate dog id starting from 101 prefixed by the first character of the breed
get_dog_price(breed): Return the price of the dog whose breed is passed to the method
calculate_total_price(): Calculate the total price of all the dogs required by the customer.
Validate breed and quantity of all the dogs required by the customer
If valid,
For every breed in breed_list,
Update quantity in dog_breed_dict
Auto-generate dog id and append it to attribute, dog_id_list
Add price to attribute, price
If accessories are required, add 350 to attribute, price
If price is more than 1500, provide 5% discount on price
If any breed is not available, return -1
If quantity is not available for any breed, return -2

Breed                              Price             
Labrador Retriever                  800
German Shepherd                     1230
Beagle                               650

Perform case sensitive string comparison 

For testing:
Create objects of Dog class
Invoke calculate_total_price() on Dog objects
Display the details
"""

#lex_auth_0127390295941775362719
#Start writing you code here
class Dog:
    counter=100
    dog_breed_dict={"Labrador Retriever":6,"German Shepherd":12,"Beagle":3}
    def __init__(self,breed_list,accessories_required):
        self.__dog_id_list=[]
        self.__breed_list=breed_list
        self.__accessories_required=accessories_required
        self.__price=0
    def get_dog_id_list(self):
        return self.__dog_id_list
    def get_breed_list(self):
        return self.__breed_list
    def get_accessories_required(self):
        return self.__accessories_required
    def get_price(self):
        return self.__price
    def get_dog_price(self,breed):
        d={"Labrador Retriever":800,"German Shepherd":1230,"Beagle":650}
        return d[breed]
    def validate_breed(self):
        for i in self.__breed_list:
            if i not in Dog.dog_breed_dict:
                return False
                
        return True
    def validate_quantity(self):
        for i in  self.__breed_list:
            if i in Dog.dog_breed_dict and Dog.dog_breed_dict[i]>0:
                pass
            else:
                return False
        return True
        
                
    def generate_dog_id(self,breed):
        Dog.counter+=1
        return breed[0]+str(Dog.counter)
    def calculate_total_price(self):
        d={"Labrador Retriever":800,"German Shepherd":1230,"Beagle":650}
        if self.validate_breed():
            if self.validate_quantity():
                for i in self.__breed_list:
                    Dog.dog_breed_dict[i]+=1
                    self.__dog_id_list.append(self.generate_dog_id(i))
                    self.__price+=d[i]
                    #print(self.__price)
                if self.__accessories_required==True:
                    self.__price+=350
                        #print(self.__price)
        
                if self.__price>1500:
                    self.__price-=self.__price*0.05
                        
                        #print(self.__price)
            else:
                return -2
        else:
            return -1
            
    
        
        
        
c=Dog(["Labrador Retriever","Beagle"],True) 
c.calculate_total_price()
print(c.get_price())

        
       
