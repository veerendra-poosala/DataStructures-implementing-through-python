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

    #inserting at middle
    def insert_at_middle(self,index,new_data):
        if index < 0:
            raise Exception("INVALID INDEX")
            return
        if index>self.get_length():
            raise Exception("INVALID INDEX")
            return
        
        if self.head is None and index == 0:
            self.insert_at_beginning(new_data)
            return
        if index == 0:
            self.insert_at_beginning(new_data)
            return
        elif index == self.get_length():
            self.insert_at_end(new_data)
            return
        first_node = self.head
        count=0
        nxt=first_node.next
        new_node=Node(new_data)
        while first_node.next:
            if count == index-1:
                new_node.prev=first_node.next
                first_node.next=new_node
                new_node.next=new_node.prev    
            first_node=first_node.next
            count+=1


    #deletining elements
    #deleting an element at beginning
    def removing_an_element_at_beg(self):
        n=self.name
        if self.head is None:
            print("Removing from {} is NOt Possible".format(n))
            return
        first_node=self.head
        nxt=first_node.next
        prev=first_node.prev
        self.head=nxt
        nxt.prev =None
    
    #deleting an element at ending
    def removing_an_element_at_end(self):
        n=self.name
        length1=self.get_length()
        #print("length of dll is {}".format(length1))
        if self.head is None:
            print("Removing from {} is NOt Possible".format(n))
            return
        if length1 == 1:
            self.removing_an_element_at_beg()
            return
        first_node=self.head
        nxt=first_node.next
        prev=first_node.prev
        length2=length1-2
        #print(length2)
        count=0
        while first_node.next:
            if count == length2:
                first_node.next=nxt.next
                nxt.prev=None
                nxt.next=None
                break
            first_node=first_node.next
            count+=1
            




        








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
        #print("The length of the DLL is {}".format(count))
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
    d1.insert_at_end(48)
    d1.insert_at_middle(4,47)
    d1.print_dll()
    #d1.removing_an_element_at_beg()
    d1.removing_an_element_at_end()
    d1.print_dll()

    d2=doubleLinkedList("Second DLL")
    d2.insert_at_end(85)
    d2.insert_at_end(86)
    d2.insert_at_end(87)
    d2.print_dll()
    d2.removing_an_element_at_beg()
    d2.print_dll()