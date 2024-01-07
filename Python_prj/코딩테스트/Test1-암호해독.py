n = int(input("한 변의 길이:"))
arr1 = list(map(int, input("arr1: ").split()))
arr2 = list(map(int, input("arr2: ").split()))

arr = []
for i in range(len(arr1)):
    arr.append(bin(arr1[i] | arr2[i]))
    pass

for arr_idx in range(len(arr)):
    num = str(arr[arr_idx])[2:]
    arr_str=""
    arr[arr_idx] = ''.join([arr_str+"#" if bool(int(i)) else arr_str+" " for i in num])
    pass

print(arr)