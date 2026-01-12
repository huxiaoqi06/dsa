from collections import deque
class TreeNode:
    def __init__(self,value,degree):
        self.value=value
        self.degree=degree
        self.children=[]

def build_tree(l):
    root=TreeNode(l[0],int(l[1]))
    i=2
    q=deque()
    q.append(root)
    while q:#and i<len(l)可要可不要吧
        node=q.popleft()
        for _ in range(node.degree):
            new_node=TreeNode(l[i],int(l[i+1]))
            node.children.append(new_node)
            i+=2
            q.append(new_node)
    return root

def postorder(root,output):
    for child in root.children:
        postorder(child,output)
    output.append(root.value)

n=int(input().strip())
output=[]
for _ in range(n):
    l=input().strip().split()
    root=build_tree(l)
    postorder(root,output)
print(*output)


