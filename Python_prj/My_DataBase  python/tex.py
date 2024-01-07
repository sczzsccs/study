# Block=[
#     [0,1,0,
#     1,1,1],

#     [2,2,2,2]
# ]

# Color=(
#   'red',
#   'bule',
#   'green'
# )

# Block1=Block[0][:3]
# Block2=Block[0][3:]

# Block3=Block[1][:]

# print(Block1)
# print(Block2)
# print(Block3)

# Block_Color=[]
# for val_list in Block:
#   for val in val_list:
#     Block_Color.append(Color[val])
# print(Block)
# print(Block_Color)

# Block1=Block_Color[:3]
# print(Block1) 
# Block1=Block_Color[3:6]
# print(Block1)  
# Block1=Block_Color[6:]
# print(Block1)    

# red, blue, red  
# blue,blue,blue

# dic={}
# dic['h']='4fsfs'
# dic['a']='a'
# dic['d']='s'
# dic['c']='c'

# print("Key: ",list(dic.keys()))

# if 'D' in dic.keys():
#     print("'D'key가 있습니다.")
# else: print("'D'key가 없습니다.")
# print("values: ",list(dic.values()))
# print("'b' in dic.values()':", 'b' in dic.values())

# if 'a' in dic.keys():
#     print("'a'key가 있습니다.")
# else: print("'a'key가 없습니다.")    
# print("'a' in dic.keys()':", 'a' in dic.keys())

# a=[a for a in range(0,10,2)]
# print(a)

My_List=[
    [1,2,66],
    ["sd",11],
    [545,45,5],
    [22]
]

List2=[]
for List1 in My_List:
    List2+=List1
print(List2.count(2))
print(List2)