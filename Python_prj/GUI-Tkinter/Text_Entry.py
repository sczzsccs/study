import tkinter as TK
tk=TK.Tk()

tk.title("Main Screen")
tk.geometry("420x250+300+150")

{# txt= TK.Text(tk, width=30, height=2) 
# txt.pack()
# txt.insert("end", "Text is Input..")
}

Label=TK.Label(tk, text="Motor 속도 설정")
Label.pack()

entry=TK.Entry(tk, width=30)
entry.pack()
entry.insert(0, "Motor 속도 입력 : ")

txt= TK.Text(tk, width=30, height=2) 
txt.pack()

txet2=""

def Txet_Input():
    global text2 
    text2=entry.get()
    if ':' in text2:
        text2=text2[text2.index(':')+2:]
    if "mm/min" not in text2:
        text2+="mm/min"
    entry.delete(0, "end")
    entry.insert(0, "Motor 속도 입력 : "+text2)
    txt.delete("1.0", "end")
    txt.insert("end", "Motor 속도 : "+text2)    

txt_btn=TK.Button(tk, padx=3, pady=5 ,text="입력", command=Txet_Input)
txt_btn.pack()

def Txet_Save():
    global text2
    File=open("Text.txt", "a")
    File.write("입력된 Motor 속도 : "+text2+"\n")
    File.close()

Save_btn=TK.Button(tk, padx=3, pady=5 ,text="저장", command=Txet_Save)
Save_btn.pack()

def Txet_Load():
    File=open("Text.txt", "r")
    text2=File.readlines()[-1]
    text2=str(text2)[2:-2]
    print(text2)
    text2=text2[text2.index(':')+2:]
    txt.delete("1.0", "end")
    txt.insert("end", "Motor 속도 : "+text2)  
    
Load_btn=TK.Button(tk, padx=3, pady=5 ,text="설정 값 불러오기", command=Txet_Load)
Load_btn.pack()

tk.mainloop()