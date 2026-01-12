#本题用栈和递归应该都可以，核心思想是递归的
s=input().strip()

class TreeNode:
    def __init__(self,value):
        self.value=value
        self.children=[]
def build_tree(s):
    stack=[]
    node=None
    for a in s:
        if a==',':
            continue
        elif a=='(':
            #if node:按规则这里不可能是None因此不需要这个判断
                stack.append(node)
                #node=None应该可以不要
        elif a==')':
            node=stack.pop()#作用应该只是最后可以把根节点赋值上去
        else:
            node=TreeNode(a)
            if stack:#这个应该也只是对一开始根节点有用
                stack[-1].children.append(node)
    return node
#注意：字母用a.isalpha()判断会更安全
pre_output=post_output=''

def preorder(node):
    global pre_output
    pre_output+=node.value
    for child in node.children:
        preorder(child)

def postorder(node):
    global post_output
    for child in node.children:
        postorder(child)
    post_output+=node.value

root=build_tree(s)

preorder(root)
postorder(root)

print(pre_output)
print(post_output)