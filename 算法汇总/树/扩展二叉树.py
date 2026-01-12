class TreeNode:
    def __init__(self,val):
        self.val=val
        self.num=0
        self.left=None
        self.right=None   
def build_tree(s):
    node=TreeNode(s[0])
    stack=[node]
    for a in s[1:]:
        if a=='.':
            stack[-1].num+=1
            while stack:
                if stack[-1].num==2:
                    node=stack.pop()
                else:
                    break
        else:
            parent=stack[-1]
            node=TreeNode(a)
            if parent.num==0:
                parent.left=node
            else:
                parent.right=node
            parent.num+=1
            stack.append(node)
    return node
#def build_tree(s, index):这个美妙多了
    # 如果当前字符为'.'，表示空结点，返回None，并将索引后移一位
    if s[index] == '.':
        return None, index + 1
    # 否则创建一个结点
    node = Node(s[index])
    index += 1
    # 递归构造左子树
    node.left, index = build_tree(s, index)
    # 递归构造右子树
    node.right, index = build_tree(s, index)
    return node, index
def inorder(node):
    if node is None:
        return []
    return inorder(node.left)+[node.val]+inorder(node.right)
def postorder(node):
    if node is None:
        return []
    return postorder(node.left)+postorder(node.right)+[node.val]
s=input().strip()
root=build_tree(s)
l1=inorder(root)
l2=postorder(root)
print(''.join(l1))
print(''.join(l2))
