"""
Problem Statement
A post office wants to automate the process of allocation of letters to different postmen based on their allocated area.
Write a python program to implement the class diagram given below.

Class description

Letter class:
Initialize static variable counter to 1
Auto-generate attribute, letter_id starting from 1 in the constructor

PostMan class:
Initialize static variable counter to 100
Auto-generate attribute, postman_id starting from 101 prefixed by “P” in the constructor
post_list_to_deliver: List of letter objects to be delivered by the postman

PostOffice class:
area_list: List of names of areas under the post office
postmen_list: List of postman objects working in the post office. There is one to one correspondence between the two lists – which means postman at index position 0 delivers letters in the area at index position 0 of area_list
validate_letter(letter): Accept the letter and validate its receiver area. If letter.receiver_area is present in area_list, return the index position of that area in area_list. Else return -1
allocate_posts(letter_list): Allocate letters in the letter_list to the appropraie postman
For every letter in letter_list
Validate letter.receiver_area
If valid, append the letter to the corresponding postman's post_list_to_deliver
Else, add it to an invalid letter list
Return invalid letter list
Perform case sensitive comparison.
Create objects of Letter class, PostMan class and PostOffice class, invoke appropriate methods and test your program.
"""
#lex_auth_012752569709305856308
#Start writing you code here
class Letter:
    counter=1
    def __init__(self,sender_area,receiver_area):
        self.letter_id=Letter.counter
        Letter.counter+=1
        self.__sender_area=sender_area
        self.__receiver_area=receiver_area
        
    def get_sender_area(self):
        return self.__sender_area
        
    def get_receiver_area(self):
        return self.__receiver_area
        
class PostMan:
    counter=100
    def __init__(self,name):
        PostMan.counter+=1
        self.postman_id="P"+str(PostMan.counter)
        self.__name=name
        self.__post_list_to_deliver=[]
        
    def get_post_list_to_deliver(self):
        return self.__post_list_to_deliver
    
    def get_name(self):
        return self.__name
        
        
class PostOffice:
    def __init__(self,postmen_list,area_list):
        self.__area_list=area_list
        self.__postmen_list=postmen_list
        
    def get_area_list(self):
        return self.__area_list
    
    def get_postmen_list(self):
        return self.__postmen_list
        
    def validate_letter(self,letter):
        if letter.get_receiver_area() in self.__area_list: 
            return self.__area_list.index(letter.get_receiver_area())
        return -1
    def allocate_posts(self,letter_list): 
        invalid_letter_list=[]
        for i in letter_list:
            if self.validate_letter(i)>=0: 
                self.get_postmen_list()[self.validate_letter(i)].get_post_list_to_deliver().append(i)

            else:
                invalid_letter_list.append(i) 
        return invalid_letter_list
