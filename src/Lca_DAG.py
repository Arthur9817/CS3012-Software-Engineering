class Node:

    def __init__(self, key):
        self.key =  key
        self.parent = []
        self.child = []

def findLCA(root, n1, n2):

    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root.key

    lca = []

    i = 0
    while(i<len(n1.parent)):
        j = 0
        while(j<len(n2.parent)):
            if(n1.parent[i].key == n2.parent[j].key):
                lca.append(n1.parent[i].key)
                j+=1
            else:
                j+=1
        i+=1
        
        if lca:
            return max(lca)

    return root.key

root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

root.child = [n2, n3]
n2.child = [n5]
n2.parent = [root, n4, n7]
n3.child = [n4, n6]
n3.parent = [root, n5]
n4.child = [n2, n6]
n4.parent = [n3]
n5.child = [n3]
n5.parent = [n2]
n6.child = [n7]
n6.parent = [n3, n4]
n7.parent = [n2, n6]
