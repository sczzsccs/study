numbers=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
Counter={}

for number in numbers:
    if number in Counter.keys():
        Counter[number]+=1
    else : Counter[number]=1

print("Counter: ",Counter)

# 또 다른 풀이
numbers2=[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
Counter2={}

for number in range(1,10):
    Counter2[number]=numbers2.count(number)

print("Counter2:",Counter2)