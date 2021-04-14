from __future__ import print_function
class node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class linkedlist():
    def __init__(self,name="unknown",head=None):
        self.head=head
        self.name=name
    def insert_at_beginning(self,new_data):
        if self.head is None:

            new_node=node(new_data)
            new_node.next=self.head
            self.head=new_node
            return
        new_node=node(new_data)
        new_node.next=self.head
        self.head=new_node
        return
    def insert_at_end(self,new_data):
        new_node=node(new_data)
        if self.head is None:
            #new_node=node(new_data)
            self.head=new_node
            new_node.next=None
            return
        else:
            itr = self.head
            while itr.next:
                itr=itr.next
            #itr.next=new_node    
            #new_node=node(new_data,None)
            itr.next=new_node
            new_node.next=None
            


    def print_ll(self):
        n=self.name
        if self.head is None:
            print("linked list {} is empty".format(n))
            return
        firstnode=self.head
        string=" "
        while firstnode:
            string=str(firstnode.data)+" -->"
            firstnode=firstnode.next
            print(string,end=" ")
        print()

    def get_length(self):
        n=self.name
        if self.head is None:
            print("The length of the {} list is empty".format(n))
        first_node=self.head
        count=0
        while first_node:
            first_node=first_node.next
            count+=1
        print("count of {0} is {1}".format(n,count))
        return count
            



    def insert_at_middle(self,index,new_data):
        if index < 0 and index >= self.get_length():
            raise Exception("Invalid Index")
            return
        #new_node=new_node(new_data)
        if self.head is None:
            new_node=node(new_data)
            new_node.next=self.head
            self.head=new_node
        first_node=self.head
        count=0
        #new_node=new_node(new_data)
        while first_node:
            if count == index-1:
                new_node=node(new_data)
                new_node.next=first_node.next
                first_node.next=new_node
                break
            first_node=first_node.next
            count+=1

    def removing_an_element(self,index):
        if index<0 and index>=self.get_length():
            raise Exception("Invalid syntax")
        if index==0:
            self.head=self.head.next
            return
        first_node=self.head
        count=0
        while first_node:
            if count==index-1:
                first_node.next=first_node.next.next
                break

            first_node=first_node.next
            count+=1
    def insertings_values(self,*data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)








one=linkedlist("first")
one.insert_at_beginning(5)
one.print_ll()
one.insert_at_beginning(6)
one.print_ll()
one.insert_at_end(9)
one.print_ll()
one.insert_at_end(10)
one.print_ll()
one.insert_at_end(12)
one.print_ll()
one.insert_at_beginning(8)
one.print_ll()
one.insert_at_end(13)
one.insert_at_beginning(7)
one.print_ll()
two=linkedlist("two")
two.insert_at_beginning(5)
two.insert_at_beginning(4)
two.print_ll()
one.get_length()
two.get_length()
three=linkedlist("three")
three.get_length()
three.insert_at_middle(0,11)
one.insert_at_middle(6,11)
one.print_ll()
#three.print_ll()
one.removing_an_element(0)
one.removing_an_element(6)
one.print_ll()
fourth=linkedlist("list")
fourth.insertings_values("mango","apple","tomato")
fourth.print_ll()
fourth.removing_an_element(0)
fourth.print_ll()
fourth.insert_at_end("grape")
fourth.print_ll()
