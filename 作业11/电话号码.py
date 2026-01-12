class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

def check_consistency(phone_numbers):
    """
    检查电话号码是否一致（无前缀关系）
    """
    root = TrieNode()
    
    for number in phone_numbers:
        current = root
        is_prefix_of_existing = False
        
        # 遍历当前号码的每一位数字
        for digit in number:
            # 情况1：在遍历过程中遇到已结束的节点
            # 说明当前号码包含了之前某个号码作为前缀
            if current.is_end:
                is_prefix_of_existing = True
                break
            
            if digit not in current.children:
                current.children[digit] = TrieNode()
            
            current = current.children[digit]
        
        # 检查冲突情况
        if is_prefix_of_existing:
            # 当前号码是之前某个号码的前缀
            return False
        
        if current.is_end:
            # 当前号码与之前某个号码完全相同（或之前号码是当前的前缀）
            # 这种情况在题目中也应该返回False
            return False
        
        if current.children:
            # 当前路径已经有更长的号码，说明之前插入的号码是当前号码的前缀
            return False
        
        # 标记当前路径为完整号码
        current.is_end = True
    
    return True


t = int(input().strip())
    
for _ in range(t):
    n = int(input().strip())
    phone_numbers = []
    for _ in range(n):
        phone_numbers.append(input().strip())
        
    if check_consistency(phone_numbers):
        print("YES")
    else:
        print("NO")