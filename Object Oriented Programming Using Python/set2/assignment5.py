"""
Problem Statement
Write a python program to find out if a given classroom is present in the left wing of a university building. Implement the class, Classroom given below.
Method/Attribute description:
classroom_list: Static list which store the name of the class rooms in the left wing
search_classroom(class_room): Static method which search for the given class room in the classroom_list. If found, return "Found". Else, return -1
Note: Perform case insensitive string comparison 
For testing:
Invoke search_classroom(class_room) static method on class, Classroom by passing the name of the class room to be searched
Display appropriate message based on the return value of search_classroom(class_room)
"""
#lex_auth_012751124968554496166
#Start writing your code her
class Classroom: 
    classroom_list=None
    @staticmethod
    def search_classroom(class_room):
        if class_room.title() in Classroom.classroom_list: 
            return "Found"
        else:
            return -1
