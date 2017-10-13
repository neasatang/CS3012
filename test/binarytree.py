from Python.CS3012.node import BTNode

def insert(root, node):
    if root is None:
        root = node

    else:
        if root.key < node.key:
            if root.right is None:
                root.right = node

            else:
                insert(root.right, node)

        else:
            if root.left is None:
                root.left = node

            else:
                insert(root.left ,node)

def traverse(root, path, k):
    #hi
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

def findLCA (root, node1, node2):

    path1 = []
    path2 = []

    if (not traverse(root, path1, node1) or not traverse(root, path2, node2)):
        return -1

    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]

def printBST(root):
    if root:
        printBST(root.left)
        print(root.key)
        printBST(root.right)

root = BTNode(50)
insert(root, BTNode(30))
insert(root, BTNode(20))
insert(root, BTNode(40))
insert(root, BTNode(70))
insert(root, BTNode(60))
insert(root, BTNode(80))

printBST(root)

print("LCA(LCA (20,40) = %d" % (findLCA(root,20,40)))
