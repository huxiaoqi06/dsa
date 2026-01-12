s=input().strip()
class TreeNode:
    def __init__(self,value):
        self.value=value
        self.children=[]
def build_tree(s,i):#不如栈简洁明了
    node=TreeNode(s[i])
    i+=1
    if i<len(s) and s[i]=='(':
        i+=1
        while i<len(s):
            child,i=build_tree(s,i)
            node.children.append(child)
            if i<len(s) and s[i]==')':
                i+=1
                break
            if i<len(s) and s[i]==',':
                i+=1
            
    return node,i

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

root,i=build_tree(s,0)

preorder(root)
postorder(root)

print(pre_output)
print(post_output)
    