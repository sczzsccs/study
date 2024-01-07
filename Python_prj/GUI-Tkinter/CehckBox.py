import tkinter as TK
tk=TK.Tk()
tk.title("Check Box")
tk.geometry("420x240+500+300")

Chek_txt=""
def Check_Btn():
    global Chek_txt
    if Chek_var.get() == TK.TRUE:
        Chek_txt="Check1 Check!"
        pass
    else: Chek_txt="Check1 Uncheck!"

    print(Chek_txt)
    Chek_ent.delete(0, "end")
    Chek_ent.insert(0, Chek_txt)
    pass

Chek_var=TK.IntVar()
Chek=TK.Checkbutton(tk, text="Check1", variable=Chek_var, command=Check_Btn)
Chek.pack()

Chek_ent=TK.Entry(tk, width=15)
Chek_ent.pack()

tk.mainloop() 