# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []
    calculateSums(root, 0, sums)
    return sums

def calculateSums(node, run_sum, sums):
    if node is None: 
        return
    run_sum = node.value + run_sum

    if node.left == None and node.right ==None:
        sums.append(run_sum)
        return 
    calculateSums(node.left, run_sum, sums)
    calculateSums(node.right, run_sum, sums)
    

def main():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    root.right.left.right = BinaryTree(8)
    print(branchSums(root))

# Driver Code
if __name__ == '__main__':
    main()
    