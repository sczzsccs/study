numbers=[105, 52, 273, 32, 77]

sum=0
min=numbers[0]
max=min

# 가장 쉬운 방법 #흔한 방법
# for n in range(len(numbers)-1):
#     if numbers[n] > numbers[int(n)+1]:
#         if max < numbers[n]:
#             max= numbers[n]
#         elif min > numbers[n+1]:
#             min= numbers[n+1]
#     elif numbers[n] < numbers[n+1]:
#         if max < numbers[n+1]:
#             max= numbers[n+1]
#         elif min > numbers[n]:
#             min= numbers[n]
#     sum+=numbers[n]
# sum+=numbers[-1]

#리스트 활용
#리스트 컴프리헨션 이용 *파이썬만 가능
max= [i for i in numbers if i>max]
for i in numbers:
    #if max<i:
      #max=i
    if min>i:
        min=i
    sum+= i

print("max: ", max)
print("min: ", min)
print("sum: ", sum)