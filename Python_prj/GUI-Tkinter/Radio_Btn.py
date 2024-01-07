import tkinter as TK
tk=TK.Tk()
tk.title("Radio Button")
tk.geometry("200x280+500+300")

label1=TK.Label(tk, text="메뉴판").pack()
Burger_Var=TK.IntVar()
Radio_Burger1=TK.Radiobutton(tk, text="햄버거", value=5900, variable=Burger_Var)
Radio_Burger1.select()
Radio_Burger1.pack()
Radio_Burger2=TK.Radiobutton(tk, text="치즈버거", value=6300, variable=Burger_Var).pack()
Radio_Burger3=TK.Radiobutton(tk, text="치킨버거", value=6500, variable=Burger_Var).pack()


label2=TK.Label(tk, text="음료").pack()
Drink_Var=TK.IntVar()
Radio_Drink1=TK.Radiobutton(tk, text="콜라 1.25L", value=2000, variable=Drink_Var)
Radio_Drink1.select()
Radio_Drink1.pack()
Radio_Drink2=TK.Radiobutton(tk, text="사이다", value=1700, variable=Drink_Var).pack()
Radio_Drink3=TK.Radiobutton(tk, text="환타", value=1900, variable=Drink_Var).pack()
Radio_Drink4=TK.Radiobutton(tk, text="콜라 0.5L", value=1500, variable=Drink_Var).pack()


def Select_Burger1():
    global Burger_Ent
    Burger_Ent.delete(0, "end")
    Value=Burger_Var.get()+Drink_Var.get()
    Burger_Ent.insert(0, "   "+str(Value)+"   원")
    pass

Select_btn=TK.Button(tk, text="선택완료", command=Select_Burger1).pack()

Burger_Ent=TK.Entry(0, width=10)
Burger_Ent.pack()

tk.mainloop()