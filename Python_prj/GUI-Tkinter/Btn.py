import tkinter as TK
tk=TK.Tk()

class btn:
    def __init__(self):
        self.btn1 = TK.Button(tk, text="버튼1", command=self.Btn_Click)
        self.btn2 = TK.Button(tk, padx=5, pady=10, text="버튼2")
        self.btn3 = TK.Button(tk, padx=10, pady=5, text="버튼3")

        self.Check_icon=TK.PhotoImage(file="./체크.png")
        self.Check_Btn=TK.Button(tk, image=self.Check_icon, command=self.Btn_Click)
                
        self.X_icon=TK.PhotoImage(file="./X.png")
        self.X_Btn=TK.Button(tk, image=self.X_icon)

        return self.Btn_pack()

    def Btn_pack(self):
        self.btn1.pack()
        self.btn2.pack()
        self.btn3.pack()
        self.Check_Btn.pack()
        self.X_Btn.pack()
        pass

    def Btn_Click(self):
        print("버튼 클릭")
        pass
    pass


tk.title("Main Screen")
tk.geometry("1280x720+300+150")

UI_btn=btn()

tk.mainloop()