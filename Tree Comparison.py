class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.data = val
    
    def __str__(self):
        return str(self.data)

def add(root,  x):
    if root==None:
        root = Node(x)
        return root
    if x>root.data:
        if root.right==None:
            root.right = Node(x)
        else:
            root.right = add(root.right, x)
    else:                                           #for x<root.data
        if root.left == None:
            root.left = Node(x)
        else:
            root.left = add(root.left, x)
    return root


def compare(a, b):

    #if both are None
    if a==b==None:
        return True
    
    #if both are not-empty
    if a is not None and b is not None:
        return compare(a.right, b.right) and compare(a.left, b.left)

    #one is empty and one is not
    else:
        return False

t1 = Node(3)
add(t1, 7)
add(t1, 0)
t2 = Node(6)
add(t2, 10)
add(t2,1)

print(compare(t1, t2))
    
