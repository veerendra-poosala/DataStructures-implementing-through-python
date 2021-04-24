#creating double linked list
from __future__ import print_function
#creating class node
class Node():
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

#creating class double linked list
class doubleLinkedList():
    def __init__ (self,name="Unknown DLL",head=None):
        self.name=name
        self.head=None

    #inserting elements to dll
    def insert_at_beginning(self,new_data):
        if self.head is None:
            new_node=Node(new_data)
            self.head=new_node
            new_node.next=None
            new_node.prev=None
            return
        first_node = self.head
        new_node=Node(new_data)
        new_node.next=first_node
        first_node.prev=new_node
        self.head=new_node
        new_node.prev=None
        first_node.next=new_node.next.next

    #inserting at end
    def insert_at_end(self,new_data):
        #length1=self.get_length()
        if self.head is None :
            self.insert_at_beginning(new_data)
            return
        first_node=self.head
        new_node=Node(new_data)
        while first_node.next:
            first_node=first_node.next
        first_node.next=new_node
        new_node.prev=first_node
        new_node.next=None






    #get length of dll
    def get_length(self):
        n=self.name
        if self.head is None:
            print("{0} is EMPTY DLL".format(n))
            return
        first_node=self.head
        count=0
        while first_node:
            first_node=first_node.next
            count+=1
        print("The length of the DLL is {}".format(count))
        return count



    #printing dll
    def print_dll(self):
        n=self.name
        if self.head is None:
            print("{0} is EMPTY DLL".format(n))
            return
        first_node=self.head
        string=""
        while first_node:
            string=str(first_node.data)+" ---> "
            first_node=first_node.next
            print(string,end=" ")
        print()


if __name__=="__main__":
    d1=doubleLinkedList("First DLL")
    d1.insert_at_beginning(45)
    d1.insert_at_beginning(44)
    d1.insert_at_beginning(43)
    d1.insert_at_end(46)
    d1.print_dll()

    d2=doubleLinkedList("Second DLL")
    d2.insert_at_end(85)
    d2.insert_at_end(86)
    d2.insert_at_end(87)
    d2.print_dll()