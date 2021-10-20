class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTreeDetails(root):
    if root == None:
        return

    print(root.data, end = " : ")
    if root.left != None:
        print("L ", root.left.data, end = ',')
    if root.right != None: 
        print("R ", root.right.data, end = " ")
    print()
    printTreeDetails(root.left)   
    printTreeDetails(root.right)

    
def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right= rightTree
    return root

def height(root):
    if root == None:
        return 0
    leftheight = height(root.left)
    rightheight = height(root.right)
    if leftheight > rightheight:
        return leftheight+1
    else:
        return rightheight+1
    
root = treeInput()

printTreeDetails(root)

print("Height", height(root))

    