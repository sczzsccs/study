def 조건(조건식, *실행문):
    if 조건식:
        실행문
        pass

def 출력(*n):
    print(*n)

def 입력(*n:str):
    return input(*n)
    
def 정수변환(n):
    return int(n)

def 실수변환(n):
    return float(n)

def 문자변환(n):
    return str(n)

def 이진변환(n):
    return bool(n)

A=정수변환(입력("A:"))

def B조건():
    B=정수변환(입력("B:"))
    조건(B<=1,
      출력(B))

조건(A<1,
    출력("A:",A),
    B조건(),
    )