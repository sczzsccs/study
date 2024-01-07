# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# def Func_X(X:list):
#     """
#     X: List X
#     """
#     arr_str = "F(x) = "
#     X_len = len(X)
#     sum = 0
#     X_e = X_len-1
    
#     arr_str += (str(X[0]) + "^" + str(X_e))
#     sum += X[0]**X_e
#     for i in range(1, X_len):
#         if X[i] != 0:
#             if (X[i] < 0) : arr_str += " " 
#             else: arr_str += " + "
#             arr_str += (str(X[i]) + "^" + str(X_e-i))
#             sum += X[i]**(X_e-i)
#     return arr_str + " = " + str(sum)
# # end def

# def Func_X(X:list):
#     """
#     X: List X
#     """
#     arr_str = "F(x) = "
#     X_e , X_n = X
#     sum = 0
    
#     arr_str += (str(X_n[0]) + "^" + str(X_e[0]))
#     sum += X_n[0]**X_e[0]
#     for i in range(1, len(X_n)):
#         if X_n[i] != 0:
#             if (X_n[i] < 0) : arr_str += " " 
#             else: arr_str += " + "
#             arr_str += (str(X_n[i]) + "^" + str(X_e[i]))
#             sum += X_n[i]**(X_e[i])
#     return arr_str + " = " + str(sum)


# # end def
# """ X[0]: 항 차수, X [1]: 계수 """
# X=[[300, 250, 133, 50, 1], 
#    [-7 ,   4,   0, -3, 1]]

# print(f"X 항 차수: {X[0]}")
# print(f"X  계수  : {X[1]}")
# print(Func_X(X))

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.link = None
        pass

def print_Nodes(start):
    current = start
    if current != None:
        print(current.data, end=" ")
        while current.link != None:
            current = current.link
            print(current.data, end=" ")
        print()

# 삽입할 위치(find), 삽입할 데이터(data)
def insert_Node2(find, data):
    global head, current, pre
    current = head #head.link가 없을 때 방지
    node = Node(data) #노드에 데이터 생성

    if current.data == find: #첪 번째 데이터가 찾는데이터인지 확인
        node.link = head #노드링크가 첫 번째(head)가 되기 위해 노드링크가 처음 노드(head)를 가리키게(처음 노드는 head만 가리켜야 함)
        head = node #처음노드(head)에 생성한 노드를 가리키게 함으로 써 새롭게 처음노드가 만들어진다.
    else: # 처음이후 삽입인 경우
        pre = current #pre의 값이 없을 때 방지
        while current.data != find: #현재데이터와 찾는데이터(위치) 같은지 확인
            pre = current #다음 노드탐색을 위해 현재노드를 이전노드가 가리키게함
            if current.link == None: #현재노드 다음의 데이터노드가 존재하는지 확인
                current = None #다음노드가 없을 시 노드가 이어지지않게
                break #다음노드가 없으므로 반복문 벗어나기
            current = current.link #현재의 다음을 현재노드가 가리킴으로 써 계속 탐색을 이어나감
            
        node.link = current #다음노드가 있으면 현재노드가 가리킴으로 써 이어짐, 없으면 None
        pre.link = node #이전노드가 가리키게함으로 써 데이터 노드가 이어지게 됨

node = Node(0)
head = node

data_arr = range(1, 5)
for data in data_arr:
    pre = node
    node = Node(data)
    pre.link = node

print("--")
print_Nodes(head)

insert_Node2(5, 1)
print_Nodes(head)