from __future__ import print_function
#creating avl tree node

class treenode(object):
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        self.height=1

#creating avl tree class
class avltree(object):
    def get_height(self,root):
        if not root:
            return 0
        return root.height

    def get_balance(self,root):
        if not root:
            return 0
        return self.get_height(root.left)-self.get_height(root.right)

    def insert(self,root,key):
        #perform normal bst
        if not root:
            return treenode(key)
        elif key<root.key:
            root.left=self.insert(root.left,key)
        else:
            root.right=self.insert(root.right,key)
        #step 2- update the height of the ancestor node
        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        #3.get the balance factor
        balance=self.get_balance(root)
        #4.if the node is unbalanced ,then try out 4 cases
        #LL
        if balance >1 and key < root.left.key:
            return self.righrrotate(root)
        #RR
        if balance < -1 and key>root.right.key:
            return self.leftrotate(root)
        #LR
        if balance >1 and key > root.left.key:
            return self.righrrotate(root)
        #RL
        if balance <-1 and key<root.right.key:
            return self.leftrotate(root)
        return root

    # Recursive function to delete a node with
    # given key from subtree with given root.
    # It returns root of the modified subtree.
    def delete(self, root, key):
  
        # Step 1 - Perform standard BST delete
        if not root:
            return root
  
        elif key < root.key:
            root.left = self.delete(root.left, key)
  
        elif key > root.key:
            root.right = self.delete(root.right, key)
  
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
  
            elif root.right is None:
                temp = root.left
                root = None
                return temp
  
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right,
                                      temp.key)
  
        # If the tree has only one node,
        # simply return it
        if root is None:
            return root
  
        # Step 2 - Update the height of the 
        # ancestor node
        root.height = 1 + max(self.get_height(root.left),
                            self.get_height(root.right))
  
        # Step 3 - Get the balance factor
        balance = self.get_balance(root)
  
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.righrrotate(root)
  
        # Case 2 - Right Right
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.leftrotate(root)
  
        # Case 3 - Left Right
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.righrrotate(root)
  
        # Case 4 - Right Left
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftrotate(root)
  
        return root
    
    def leftrotate(self,z):
        y=z.right
        t2=y.left
        #perform rotation
        y.left=z
        z.right=t2
        #upadate heights
        z.height=1+max(self.get_height(z.left),self.get_height(z.right))
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))
        return y

    def righrrotate(self,z):
        y=z.left
        t2=y.right
        #perform rotation
        y.right=z
        z.left=t2
        #upadate heights
        z.height=1+max(self.get_height(z.left),self.get_height(z.right))
        y.height=1+max(self.get_height(y.left),self.get_height(y.right))
        return y
    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
  
        return self.getMinValueNode(root.left)
  
 


root=None
myroot=avltree()
root=myroot.insert(root,8)
root=myroot.insert(root,10)
root=myroot.insert(root,1)
root=myroot.insert(root,6)
root=myroot.insert(root,0)
root=myroot.insert(root,11)
# Preorder Traversal
print("Preorder traversal of the",
      "constructed AVL tree is")
myroot.preOrder(root)
print()
root=myroot.insert(root,9)
print("Preorder traversal of the",
      "constructed AVL tree is")
myroot.preOrder(root)
print()
root=myroot.insert(root,14)
print("Preorder traversal of the",
      "constructed AVL tree is")
myroot.preOrder(root)
print()

myTree =avltree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
  
for num in nums:
    root = myTree.insert(root, num)
print("Preorder traversal of the",
      "constructed AVL my tree is")
myTree.preOrder(root)
print() 
#Delete
key = 10
root = myTree.delete(root, key)
  
# Preorder Traversal
print("Preorder Traversal after deletion -")
myTree.preOrder(root)
print()