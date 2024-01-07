import tkinter as tk
import tkinter.ttk as ttk
TK=tk.Tk()
TK.title("Combo Box")
TK.geometry("420x320+500+300")

label=tk.Label(TK, text="카드 결제일").pack()

n=int(input("n: "))+1
combo_Val=[str(i) + "일" for i in range(1, n)]
com_box=ttk.Combobox(TK, height=5, values=combo_Val, state="readonly")
com_box.current(0)
com_box.pack()

def btn_com():
    Ent.delete(0, 'end')
    Ent.insert(0, com_box.get())
    global n, combo_Val
    n=int(input("n: "))+1

    combo_Val=[str(i) + "일" for i in range(1, n)]
    com_box['values']=combo_Val
    pass

Btn=tk.Button(TK, text="확인", command=btn_com).pack()

Ent=tk.Entry(0, width=5)
Ent.pack()

TK.mainloop()