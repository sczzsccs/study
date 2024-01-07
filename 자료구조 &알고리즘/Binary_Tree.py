class TreeNode() :
    def __init__(this, left=None, data=None, right=None) :
        this.left = left
        this.data = data
        this.right = right
    pass

def preOrder(node:TreeNode):
    if(node!=None):
        print(node.data, end='->')
        preOrder(node.left)
        preOrder(node.right)
    pass

def inOrder(node:TreeNode):
    if(node!=None):
        preOrder(node.left)
        print(node.data, end='->')
        preOrder(node.right)
    pass

def postOrder(node:TreeNode):
    if(node!=None):
        preOrder(node.left)
        preOrder(node.right)
        print(node.data, end='->')
    pass

node1 = TreeNode(data="화사")

node2 = TreeNode(data="솔라")
node1.left = node2

node3 = TreeNode(data="문별")
node1.right = node3

node4 = TreeNode(data="휘인")
node2.left = node4

node5 = TreeNode(data="쯔위")
node2.right = node5

node6 = TreeNode(data="선미")
node3.left = node6

print("--- 전위 ---")
preOrder(node1)
print()

print("--- 중위 ---")
inOrder(node1)
print()

print("--- 후위 ---")
postOrder(node1)
print()