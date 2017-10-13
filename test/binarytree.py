
#Binary Tree Node class
class BTNode:

    #Constructor for a node
     def __init__(self, key):
         self.key = key
         self.right = None
         self.left = None



def traverse(root, path, k):

    #base case
    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if ((root.left != None and traverse(root.left, path, k)) or (root.right != None and traverse(root.right, path, k))):
        return True

    path.pop()
    return False

def findLCA (root, n1, n2):

    path1 = []
    path2 = []


    if (not traverse(root, path1, n1) or not traverse(root, path2, n2)):
        return -1

        # Compare the paths to get the first different value
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]

# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
root =  BTNode(1)
root.left = BTNode(2)
root.right = BTNode(3)
root.left.left = BTNode(4)
root.left.right = BTNode(5)
root.right.left = BTNode(6)
root.right.right = BTNode(7)

print("LCA(4, 5) = %d" % (findLCA(root, 4, 5, )))
print("LCA(4, 6) = %d" % (findLCA(root, 4, 6)))
print("LCA(3, 4) = %d" % (findLCA(root, 3, 4)))
print("LCA(2, 4) = %d" % (findLCA(root, 2, 4)))
