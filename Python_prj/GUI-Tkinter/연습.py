class A:
    def __init__(self):
        self.A=1
        pass
    pass

class B(A):
    def __init__(self):
        self.B=1
        pass
    
    def A2(self, A):
        self.B+=1
        print(A)
        pass
    pass

A1=A()
B1=B()
B1.A2(A1.A)