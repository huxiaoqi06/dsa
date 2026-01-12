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
    return root#构造树必须返回根节点，不然找不着树了

def postorder(root,output):#递归在于每一个单元都是一致的因此只返回当前节点，其余交给其他单元
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


