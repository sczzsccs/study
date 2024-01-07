import tkinter as TK
tk=TK.Tk()

tk.title("Main")
tk.geometry("420x240+350+300")

ent=TK.Entry(tk, width=20)
ent.pack()

def lstbox_Add():
    ent_txt=ent.get()
    listbox.insert(listbox.curselection(), ent_txt)
    listbox.pack()

add_btn=TK.Button(tk, text="추가", command=lstbox_Add)
add_btn.pack()

listbox = TK.Listbox(tk, selectmode=TK.SINGLE, height=0)
listbox.insert(0, "1번")
listbox.insert(1, "2번")
listbox.insert(2, "3번")
listbox.insert(3, "4번")
listbox.insert(4, "5번")
listbox.pack()

def Lstbox_Del():
    listbox.delete(listbox.curselection())
    
btn=TK.Button(tk, text="삭제", command=Lstbox_Del)
btn.pack()

tk.mainloop()