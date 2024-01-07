class My_Class() :
    def __init__(self):
        self.M_Str = "클래스가 생성됐어요."
        print(self.M_Str)
        pass
    
    def M_Funtion(self, str): 
        self.M_Str = str  
        return print(self.M_Str), print("함수가 호출됐습니다.")