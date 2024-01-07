class TreeNode() :
    def __init__(this, left=None, data=None, right=None) :
        this.left = left
        this.data = data
        this.right = right
    pass

def findName(findData, node:TreeNode):
    if(findData == node.data):
        print(f"{node.data} 를(을) 찾았습니다.")
    elif(findData < node.data and node.left!=None):
        findName(findData, node.left)
    elif(findData > node.data and node.right!=None):
        findName(findData, node.right)
    else:
        print(f"{findData} 를(을) 찾지 못하였습니다.")
        return
    pass

name_ary = [
    "블랙핑크",
    "레드벨벳",
    "마마무",
    "에이핑크",
    "걸스데이",
    "트와이스"
    ]

root = TreeNode(data=name_ary[0])

for name in name_ary[1:]:
    node = TreeNode(data=name)
    current = root
    
    while(True):
        if(name < current.data):
            if(current.left == None):
                current.left = node
                break
            current = current.left
        else:
            if(current.right == None):
                current.right = node
                break
            current = current.right
    pass

findName("에이핑크", root)