class Node:

    def __init__(self, key):
        self.key =  key
        self.parent = []
        self.child = []

def findLCA(root, n1, n2):

    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    lca = []

    i=0
    while(i<len(n1.parent)):
        j=0
        while(j<len(n2.parent)):
            if(n1.parent[i].key == n2.parent[j].key):
                lca.append(n1.parent[i].key)
                j+=1
            else:
                j+=1
        i+=1
        return max(lca)
