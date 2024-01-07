import tkinter as TK
tk=TK.Tk()

tk.title("Main Screen")
tk.geometry("420x250+300+150")

class Label:
    def __init__(self):
        self.label1=TK.Label(tk, text="label1")
        self.label_Image=TK.PhotoImage(file="./images.png")
        self.Image_label=TK.Label(tk, image=self.label_Image)
        return self.label_pack()
    
    def label_pack(self):
        self.label1.pack()
        self.Image_label.pack()
        pass
    pass
    
class Btn(Label):
    def __init__(self):
        super().__init__()
        self.Check_icon=TK.PhotoImage(file="./체크.png")
        self.Check_Btn=TK.Button(tk, image=self.Check_icon, command=self.Btn_Click)
        self.Check_Btn.pack()
        pass

    def Btn_Click(self):
        self.label1.config(text="Bye!")
        self.X_icon=TK.PhotoImage(file="./X.png")
        self.Image_label.config(image=self.X_icon)
        pass
    pass


Ui_btn=Btn()

tk.mainloop()