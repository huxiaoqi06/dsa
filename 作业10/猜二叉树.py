from collections import deque
n=int(input().strip())
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def f(inorder,postorder):
    if not inorder:
        return None
    
    root=TreeNode(postorder[-1])
    i=inorder.index(root.val)

    left_inorder=inorder[:i]
    right_inorder=inorder[i+1:]

    left_postorder=postorder[:i]
    right_postorder=postorder[i:len(postorder)-1]

    root.left=f(left_inorder,left_postorder)
    root.right=f(right_inorder,right_postorder)
    return root


for _ in range(n):
    inorder=input().strip()
    postorder=input().strip()
    root=f(inorder,postorder)
    q=deque()
    q.append(root)
    output=''
    while q:
        num=len(q)
        for i in range(num):
            root=q.popleft()
            if root:
                output+=root.val
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
    print(output)
