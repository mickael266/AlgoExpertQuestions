

def calculateDepth(root, sum=0):
    if root == None:
        return 0

    return sum + calculateDepth(root.left,sum+1) + calculateDepth(root.right,sum+1)
    
   
    

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def main():
    root1 = BinaryTree(1)
    root1.left = BinaryTree(2)
    root1.right = BinaryTree(3)
    root1.left.left = BinaryTree(4)
    root1.left.right = BinaryTree(5)
    root1.right.left = BinaryTree(6)
    root1.right.right = BinaryTree(7)
    root1.left.left.left = BinaryTree(8)
    root1.left.left.right = BinaryTree(9)
    root2 = BinaryTree(1)
    root2.right = BinaryTree(3)
    root2.left = BinaryTree(2)

    print("experct 16 --->",calculateDepth(root1))
    print("experct 2 --->",calculateDepth(root2))

# Driver Code
if __name__ == '__main__':
    main()