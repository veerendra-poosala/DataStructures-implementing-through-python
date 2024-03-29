#creating circular linked list
#uses :-
#The real life application where the circular linked list is used is our Personal Computers, where multiple applications are running. ...
#Another example can be Multiplayer games. ...
#Circular Linked List can also be used to create Circular Queue
from __future__ import print_function 
#creating Node class
class Node():
    def __init__ (self,data=None,next=None):
        self.data=data
        self.next=next

#creating circular linked list class
class cll():
    def __init__ (self,name="unknown CLL"):
        self.name=name
        self.head=None
    #creating inserting element function
    def insert_at_end(self,new_data):
        if self.head is None:
            newNode=Node(new_data)
            self.head=newNode
            newNode.next=self.head
            return
        firstNOde=self.head
        newNode=Node(new_data)
        newNode.next=firstNOde
        while firstNOde and  firstNOde.next!=self.head:
            firstNOde=firstNOde.next
        firstNOde.next=newNode
        #newNode.next=self.head

    #creating prepending function or inserting at beginning function
    def prepending_a_node(self,new_data):
        if self.head is None:
            newNode=Node(new_data)
            self.head=newNode
            newNode.next=self.head
            return
        firstNOde=self.head
        newNode=Node(new_data)
        newNode.next= firstNOde
        while firstNOde and  firstNOde.next!=self.head:
            firstNOde=firstNOde.next
        firstNOde.next=newNode
        self.head=newNode
    #creating a function for inserting at middle
    def insert_at_middle(self,index,new_data):
        if index < 0 and index >= self.get_length_of_cll():
            raise Exception("index error")
            return
        if index == 0:
            self.prepending_a_node(new_data)
            return
        firstNOde=self.head
        #newNode=Node(new_data)
        count = 0
        while firstNOde and firstNOde.next != self.head:
            if count == index -1:
                newNode=Node(new_data)
                newNode.next=firstNOde.next
                firstNOde.next = newNode
                break
            firstNOde=firstNOde.next
            count+=1

    #removing nodes on cll
    #removing at beginning function
    def removing_an_element_at_beg(self):
        n=self.name
        if self.head is None:
            print("Removing from Empty {} is Not Possible".format(n))
            return
        if self.head and self.get_length_of_cll() == 1:
            self.head=None
            return
        firstNOde=self.head    
        while firstNOde and firstNOde.next!=self.head:
            firstNOde=firstNOde.next
        firstNOde.next=None
        self.head=self.head.next
        firstNOde=None
    
    #removing an element at end
    def removing_an_element_at_end(self):
        n=self.name
        length=self.get_length_of_cll()
        if self.head is None:
            print("Removing from  Empty {} is Not Possible".format(n))
            return
        if self.head and length==1:
            self.head=None
            return
        firstNOde=self.head
        length2=length-2
        count=0
        while firstNOde and firstNOde.next != self.head:
            if count == length2:
                firstNOde.next=firstNOde.next.next
                break
            firstNOde=firstNOde.next
            count+=1
        

    #removing an element at middle
    def removing_an_element_at_middle(self,index):
        if index < 0 or index >= self.get_length_of_cll():
            raise Exception("index error")
            return
        if index == 0:
            self.removing_an_element_at_beg()
            return
        firstNOde=self.head
        count=0
        while firstNOde and firstNOde.next!=self.head:
            if count == index-1:
                firstNOde.next=firstNOde.next.next
            firstNOde=firstNOde.next
            count+=1




    #creating length function
    def get_length_of_cll(self):
        n=self.name
        if self.head is None:
            print("The Length of these {} is Empty or Zero".format(n))
            return
        firstNOde=self.head
        count=0
        while firstNOde:
            firstNOde=firstNOde.next
            count+=1
            if firstNOde == self.head:
                break
        #print("length of cll is {} ".format(count))
        return count



    #creating printing cll function
    def print_cll(self):
        n=self.name
        if self.head is None:
            print("{} is Empty CLL".format(n))
            return
        firstNOde=self.head
        string=" "
        while firstNOde : 
            string=str(firstNOde.data)+" --> "
            firstNOde=firstNOde.next
            print(string,end=" ")
            if firstNOde == self.head:
                break
        print()

#creating objects in main function
def main():
    c1=cll("first Circular linked list")
    c1.insert_at_end(89)
    c1.insert_at_end(90)
    c1.prepending_a_node(91)
    c1.prepending_a_node(1000)
    c1.insert_at_end(4646)
    c1.insert_at_end(1)
    c1.insert_at_middle(1,45)
    c1.get_length_of_cll()
    c1.print_cll()
    c1.removing_an_element_at_beg()
    c1.print_cll()
    c1.removing_an_element_at_end()
    c1.print_cll()
    c1.removing_an_element_at_middle(1)
    c=c1.get_length_of_cll()
    print("The length of the cll is {}".format(c))
    c1.print_cll()

    c2=cll("Second Circular Linked list")
    c2.removing_an_element_at_beg()
    c2.removing_an_element_at_end()
    c2.insert_at_middle(0,4545)
    c2.removing_an_element_at_middle(0)
    c2.print_cll()

if __name__=="__main__":
    main()