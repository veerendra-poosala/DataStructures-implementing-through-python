#creating linked list 
from __future__ import print_function
#creating class node
class Node():
    def __init__ (self,data=None,next=None):
        self.data=data
        self.next=next
#creating class linked list 
class linkedList():
    def __init__(self,name="Unknown linked list",head=None):
        self.head=head
        self.name=name

    #inserting elements
    #inserting at beg:
    def insert_at_beginning(self,new_data):
        if self.head is None:
            new_node=Node(new_data)
            new_node.next=self.head
            self.head=new_node
            return
        first_node=self.head
        new_node=Node(new_data)
        new_node.next=first_node
        self.head=new_node
    
    #insert at end
    def insert_at_end(self,new_data):
        if self.head is None:
            new_node=Node(new_data)
            self.head=new_node
            new_node.next=None
            return
        new_node=Node(new_data)
        first_node=self.head
        while first_node.next:
            first_node=first_node.next
        first_node.next=new_node
        new_node.next=None

    #insert at middle
    def insert_at_middle(self,index,new_data):
        if index<0 and index>self.get_length():
            raise Exception("INVALID INDEX")
            return
        if self.head is None and index==0:
            self.insert_at_beginning(new_data)
            return
        if index==0:
            self.insert_at_beginning(new_data)
            return
        first_node=self.head
        #new_node=Node(new_data)
        count=0
        while first_node.next:
            if count==index-1:
                new_node=Node(new_data)
                new_node.next=first_node.next
                first_node.next=new_node
            first_node=first_node.next
            count+=1
    
    #removing_an_element_at_beg
    def removing_an_element_at_beg(self):
        n=self.head
        if self.head is None:
            print("Removing from {} EMPTY LINKED LIST is not Possible".format(n))
            return
        first_node=self.head
        self.head=self.head.next
        first_node=None
        return

    
    #removing_an_element_at_end
    def removing_an_element_at_end(self):
        n=self.head
        length1=self.get_length()
        if self.head is None:
            print("Removing from {} EMPTY LINKED LIST is not Possible".format(n))
            return
        if length1 == 1:
            self.removing_an_element_at_beg()
            return
        first_node=self.head
        length2=length1-2
        count=0
        while first_node:
            if count==length2:
                first_node.next=first_node.next.next
                return
            first_node=first_node.next
            count+=1

        
    #removing an element at middle
    def removing_an_element_at_middle(self,index):
        n=self.name
        if index<0 and index>self.get_length():
            raise Exception("INVALID INDEX")
            return
        if self.head is None:
            print("Removing from {} EMPTY LINKED LIST is not Possible".format(n))
            return
        if index==0:
            self.removing_an_element_at_beg()
            return
        first_node=self.head
        count=0
        while first_node:
            if count==index-1:
                first_node.next=first_node.next.next
            first_node=first_node.next
            count+=1
            return

    #finding length of ll
    def get_length(self):
        n=self.name
        if self.head is None:
            print("LENGTH OF THE {0} IS 0 ".format(n))
            return
        first_node=self.head
        count=0
        while first_node:
            first_node=first_node.next
            count+=1
        #print("LENGTH OF THE {0} IS {1} ".format(n,count))
        return count




    #printing linkedlist
    def print_ll(self):
        n=self.name
        if self.head is None:
            print("{0} is EMPTY LINKED LIST".format(n) )
            return
        first_node=self.head
        string=" "
        while first_node:
            string=str(first_node.data)+" ---> "
            first_node=first_node.next
            print(string,end=" ")
        print()

if __name__=="__main__":
    l1=linkedList("linked list one")
    l1.insert_at_beginning(25)
    l1.insert_at_beginning(45)
    l1.insert_at_beginning(65)
    l1.insert_at_middle(0,75)
    l1.insert_at_beginning(85)
    l1.insert_at_middle(3,55)
    l1.print_ll()
    l1.removing_an_element_at_beg()
    l1.print_ll()
    l1.insert_at_beginning(85)
    l1.print_ll()
    l1.removing_an_element_at_end()
    l1.removing_an_element_at_end()
    l1.removing_an_element_at_end()
    l1.removing_an_element_at_end()
    l1.removing_an_element_at_end()
    l1.removing_an_element_at_end()
    l1.removing_an_element_at_end()
    l1.removing_an_element_at_end()
    l1.print_ll()

    l2=linkedList("linked list two")
    l2.insert_at_end(1)
    l2.insert_at_end(2)
    l2.insert_at_end(3)
    l2.insert_at_end(4)
    l2.print_ll()
    l2.removing_an_element_at_end()
    l2.print_ll()
    l2.removing_an_element_at_end()
    l2.print_ll()
    l2.removing_an_element_at_end()
    l2.print_ll()
    l2.removing_an_element_at_end()
    l2.print_ll()
    
