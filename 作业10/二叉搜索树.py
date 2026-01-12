n=int(input().strip())
preorder=list(map(int,input().strip().split()))
inorder=[i+1 for i in range(n)]
def f(preorder,inorder):
    if len(preorder)==0:
        return []
    root = preorder[0]
    i=inorder.index(root)
    left_inorder=inorder[:i]
    right_inorder=inorder[i+1:]
    left_preorder=preorder[1:i+1]
    right_preorder=preorder[i+1:]
    left=f(left_preorder,left_inorder)
    right=f(right_preorder,right_inorder)
    return left+ right+[root]
print(*f(preorder,inorder))