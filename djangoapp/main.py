input()
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class Tree:
    def createNode(self,data):
        return Node(data)

    def insert(self,node,data):
        if node is None:
            self.createNode(data)
        if data < node.data :
            self.insert(node.left,data)
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node

    def traverse_Inorder(self,root):
        if root is not None:
            self.traverse_Inorder(root.left)
            print(root.data)
            self.traverse_Inorder(root.right)


#Driver Code
tree=Tree()
root=tree.createNode(5)
print(root.data)
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,20)
tree.insert(root,22)
tree.insert(root,8)
tree.insert(root,16)
print('Inorder---->')
tree.traverse_Inorder(root)

class Node:
    def __init__(self, info):
        self.info = info
        self.right = None
        self.left = None
        self.level = None

    def __str__(self):
        return str(self.info)

def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

class BinarySearchTree:
    def __init__(self):
        self.root = None

#Node is defined as
#self.left (the left child of Node)
#self.right (the right child of Node)
#self.infor (the value of Node)

    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
            return
        root=self.root
        while 1:
            if value<root.info:
                if root.left is not None:
                    root=root.left
                else:
                    root.left=Node(value)
                    break
            elif value >= root.info:
                if root.right is not None:
                    root=root.right
                else:
                    root.right=Node(value)
                    break

