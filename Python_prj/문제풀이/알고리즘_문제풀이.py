{# class Mode:
#     Code=[]
#     Mode=0
#     ret=[]

#     def Code_Input(self):
#         self.Code=input("Code(1<=CodeLen<=100,000(단, 'code'는 알파벳소문자 또는 '1')): ")
#         return
    
#     def code_read(self):
#         idx=-1
#         for i in self.Code:
#             idx+=1
#             if i=='1':
#                 self.Mode_Convert()
#                 continue
#             if idx%2==0+self.Mode:
#                 self.ret.append(i)
#         return
    
#     def Mode_Convert(self):
#         if self.Mode==1:
#             self.Mode=0
#         else: self.Mode=1
#         return

#     def Print_Out(slef):
#         print("ret:", slef.ret)
#         return
#         pass


# MyMode=Mode()
# MyMode.Code_Input()
# MyMode.code_read()
# MyMode.Print_Out()
}

#########################################################

{# class Str:
#     my_string=""
#     k=None

#     def __init__(self) -> None:
#         self.k=int(input("(1 ≤ k ≤ 100)k: "))
#         self.my_string=input("(1 ≤ my_string의 길이 ≤ 100)my_string: ")
#         self.for_Str()
#         return
    
#     def for_Str(self):
#         print(self.my_string*self.k)
#         return
#     pass

# My_Str=Str()
}

############################################################

{# def solution():
#     if is_prefix in my_string:
#         return 1
#     else: return 0

# my_string=input("my_string:")
# is_prefix=input("is_prefix:")

# print("solution:", solution())
}

#################################################################

n=int(input('n: '))

#렌터카 회사 자동차
CAR_RENTAL_COMPANY_CAR = {
    'CAR_ID':[],
    'CAR_TYPE':[],
    'DAILY_FEE':[],
    'OPTIONS':[],
}

for i in range(n):
    print()
    CAR_RENTAL_COMPANY_CAR['CAR_ID'].append(i)
    CAR_RENTAL_COMPANY_CAR['CAR_TYPE'].append(input('CAR_TYPE[세단, SUV, 승합차, 트럭, 리무진]: '))
    CAR_RENTAL_COMPANY_CAR['DAILY_FEE'].append(input('DAILY_FEE: '))
    CAR_RENTAL_COMPANY_CAR['OPTIONS'].append(input('OPTIONS[열선시트, 스마트키, 주차감지센서]: '))
    pass

for i in range(n):
    print()
    print('CAR_ID:', CAR_RENTAL_COMPANY_CAR['CAR_ID'][i])
    print('CAR_TYPE:', CAR_RENTAL_COMPANY_CAR['CAR_TYPE'][i])
    print('DAILY_FEE:', CAR_RENTAL_COMPANY_CAR['DAILY_FEE'][i])
    print('OPTIONS:', CAR_RENTAL_COMPANY_CAR['OPTIONS'][i])
    print('_'*45)
    pass


#자동차 렌탈 회사 렌탈 이력
CAR_RENTAL_COMPANY_RENTAL_HISTORY = {
    'HISTORY_ID':None,
    'CAR_ID':None,
    'START_DATE':None,
    'END_DATE':None
}


#렌터카 회사 할인 플랜
CAR_RENTAL_COMPANY_DISCOUNT_PLAN = {
    'PLAN_ID':None,
    'CAR_TYPE':None,
    'DURATION_TYPE':None,
    'DISCOUNT_RATE':None
}

#####################################################################################