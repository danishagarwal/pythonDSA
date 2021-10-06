class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printTree(root):
    #Plan A for base case is : if root is leaf then left not there right not there.
    # what if root is None ? Problem 1 with Plan A
    #Instead use base case : if root is None
    if root == None:
        return

    print(root.data)
    printTree(root.left)
    printTree(root.right)

def printTreeDetails(root):
    if root == None:
        return

    print(root.data, end = " : ")
    if root.left != None:
        print(root.left.data, end = ',')
    if root.right != None: 
        print(root.right.data, end = " ")
    print()
    printTreeDetails(root.left)   
    printTreeDetails(root.right)
    
b1 = Node(1)
b2 = Node(2)
b3 = Node(3)
b4 = Node(4)
b5 = Node(5)
b1.left = b2
b1.right = b3
b2.left = b4
b2.right = b5

printTreeDetails(b1)