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