
def f(preorder,inorder):
    if not preorder or not inorder:
        return ''
    root=preorder[0]
    root_index=inorder.index(root)
    left_inorder=inorder[:root_index]
    right_inorder=inorder[root_index+1:]
    left_preorder=preorder[1:len(left_inorder)+1]
    right_preorder=preorder[len(left_inorder)+1:]
    l=f(left_preorder,left_inorder)
    r=f(right_preorder,right_inorder)
    return l+r+root

try:
    while True:
        line = input().strip()
        preorder, inorder = line.split()
        print(f(preorder, inorder))
except EOFError:
    pass