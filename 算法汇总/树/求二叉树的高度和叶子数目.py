n=int(input().strip())
class TreeNode:
    def __init__(self,left=None,right=None):
        self.right=right
        self.left=left
find=[1]*n
nodes=[TreeNode() for _ in range(n)]

for i in range(n):
    left,right=map(int,input().strip().split())
    if left!=-1:
        find[left]=0
        nodes[i].left=nodes[left]
    if right!=-1:
        find[right]=0
        nodes[i].right=nodes[right]

for i in range(n):
    if find[i]:
        root=nodes[i]
def height(node):
    if node==None:
        return -1
    return max(height(node.left),height(node.right))+1

def count(node):
    if node==None:
        return 0
    if node.left==None and node.right==None:
        return 1
    return count(node.left)+count(node.right)

print(height(root),count(root))

    