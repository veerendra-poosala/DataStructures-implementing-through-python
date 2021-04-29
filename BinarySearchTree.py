#creating binary search tree
from __future__ import print_function
#creating class node
class Node(object):
    def __init__ (self,key):
        self.key=key
        self.left=None
        self.right=None
class bst(object):
    #creating element insertion function
    def inserting_element(self,root,key):
        if root is None:
            return Node(key)
        if root.key > key:
            root.left=self.inserting_element(root.left,key)
        elif root.key < key:
            root.right=self.inserting_element(root.right,key)
        return root

    def get_height(self,root):
        if not root:
            return -1
        height=1+max(self.get_height(root.left),self.get_height(root.right))
        #print(height)
        return height

    def pre_order(self,root):
        if not root:
            return
        print("{0} ".format(root.key), end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)
        
         
    def post_order(self,root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print("{0} ".format(root.key), end=" ")
        
    def deleting_a_node(self,root,key):
        if not root:
            return root
        elif key < root.key:
            root.left=self.deleting_a_node(root.left,key)
        elif key > root.key:
            root.right=self.deleting_a_node(root.right,key)
        else:
            if root.left is None:
                temp=root.right
                root.right=None
                return temp
            elif root.right is None:
                temp=root.left
                root.left=None
                return temp
            temp=self.getMinValueNode(root.right)
            root.key=temp.key
            root.right=self.deleting_a_node(root.right,temp.key)
        return root



    def getMinValueNode(self,root):
        if not root:
            return root
        return self.getMinValueNode(root.left)




    

def main():
    root=None
    mytree=bst()
    root=mytree.inserting_element(root,6)
    root=mytree.inserting_element(root,46)
    root=mytree.inserting_element(root,56)
    root=mytree.inserting_element(root,3)
    mytree.pre_order(root)
    print()
    #root=mytree.deleting_a_node(root,46)
    mytree.pre_order(root)
    print()
    mytree.post_order(root)
    print()
    mytree.get_height(root)

    boot=None
    mytree1=bst()
    b=[6,46,56,3]
    for i in b:
        boot=mytree1.inserting_element(boot,i)
        #mytree1.pre_order(boot)
    print()
    mytree1.pre_order(boot)

if __name__=="__main__":
    main()