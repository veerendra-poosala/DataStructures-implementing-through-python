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


    #creating prepending function or inserting at beginning function
    def prepending_a_node(self,new_data):
        if self.head is None:
            newNode=Node(new_data)
            self.head=newNode
            newNode.next=self.head
            return
        firstNOde=self.head
        newNode=Node(new_data)
        self.head=newNode
        newNode.next=firstNOde
    #creating a function for inserting at middle
    def insert_at_middle(self,index,new_data):
        if index < 0 or index >= self.get_length_of_cll():
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
        self.head=firstNOde.next
        firstNOde.next=firstNOde.next.next
        firstNOde=None
    '''
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
        '''





    #creating length function
    def get_length_of_cll(self):
        n=self.name
        if self.head is None:
            print("The Length of these {} is Empty or Zero".format(n))
            return
        firstNOde=self.head
        count=0
        while firstNOde and firstNOde.next != self.head:
            firstNOde=firstNOde.next
            count+=1
        return count



    #creating printing cll function
    def print_cll(self):
        n=self.name
        if self.head is None:
            print("{} is Empty CLL".format(n))
            return
        firstNOde=self.head
        string=" "
        while firstNOde and firstNOde.next != self.head:
            string=str(firstNOde.data)+" --> "
            firstNOde=firstNOde.next
            print(string,end=" ")
        print()

#creating objects in main function
def main():
    c1=cll("first Circular linked list")
    #c1.insert_at_end(89)
    #c1.insert_at_end(90)
    c1.prepending_a_node(91)
    #c1.prepending_a_node(1000)
    #c1.insert_at_end(1)
    #c1.insert_at_middle(2,45)
    #c1.print_cll()
    #c1.removing_an_element_at_beg()
    #c1.removing_an_element_at_end()
    c1.print_cll()

if __name__=="__main__":
    main()