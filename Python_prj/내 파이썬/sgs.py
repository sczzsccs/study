from My_Lib import My_Class

MyClass = My_Class()
MyClass.M_Funtion("함수 호출")

class MyClass2(My_Class) :
    def __init__(self) -> None:
        self.M_Str = "상속받은 클래스 생성"
        return print(self.M_Str, "했습니다.")
    
    def M_fun2(self) :
        self.M_Str = "상속받은 클래스 함수 호출"
        return print(self.M_Str)
    
    def M_fun3(self, str1, str2, N1, N2, N3) :
        print(self.M_Str, end=" ")
        print(str1, end=" ")
        print(str2, end=" ")
        print(N1, end=" ")
        print(N2, end=" ")
        print(N3, end=" ")

My_class2 = MyClass2()
My_class2.M_fun2()

M_Class3 = My_Class()
print(M_Class3.M_Str)
M_Class3.M_Str = "클래스 멤버 변수 변경"
print(M_Class3.M_Str)

My_class2.M_fun3("str1", "str2", 1, 2, 3)