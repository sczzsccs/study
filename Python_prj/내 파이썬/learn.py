def array(a,b,c,d,*e):
    for i in a,b,c,d,e:
        print(i)
    pass

Num_array=[1,2,3,4,5,6,7]
array(*Num_array)

def My_Func(N1):
    N1+=1
    print(N1)
    #return N1
    pass

print(My_Func(5))
My_Func(5)

list =['gs','d']
a=list.append([2,4])
print(a) #None
print(list)

a=list.extend((2,3,4))
print(a) #None
print(list)

a=list[2:4]=(1,2,3)
print(a) #(1,2,3)
print(list)

a=list.insert(1,(1,2,3))
print(a) #None
print(list)

a=list.pop(4)
print(a) #2 index4
print(list)

tr=int(input("열 입력:"))

for i in range(1,tr+1):
    for j in range(tr-(tr-1)):
        print(' '*(tr-i), end="")
    print('*'*i) if i<=1 else print(('*'*i)+('*'*(i-1)))