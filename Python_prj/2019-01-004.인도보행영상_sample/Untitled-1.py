# 회문 문제
'''
def palindrome(STR):
    for i in range(len(STR)):
        if STR[i]==' ':
            i+=1
            continue
    for i in range(int(len(STR)/2)):
        return (False if STR[-i]!=STR[i-1] else True)
    
            # print(STR[(-i)],STR[i-1],i)
    #         return False
    # return True 
      
print(palindrome(input("문자 입력: ").lower())) '''

# 각 자리 숫자의 합을 구하는 함수(리스트를 이용)
'''
def SumOfDigits(NumStr):
    Sum = 0
    for Num in NumStr:
        # print(Num)
        Sum += int(Num)
        # print(Sum)
    return Sum

print(SumOfDigits((input())))
'''

# 줄기와 잎 그림
''''''
stem_leaf=[]
score = [0, 0, 2, 4, 7, 7, 9]
stem_leaf.append(score)
score = [1, 1, 3, 8]
stem_leaf.append(score)
score = [0]
stem_leaf.append(score)

print(stem_leaf)
print("0: ", stem_leaf[0])
print("1: ", stem_leaf[1])
print("2: ", stem_leaf[2])

score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]
print(score)

stem_leaf={}
