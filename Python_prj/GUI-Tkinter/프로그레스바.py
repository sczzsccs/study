import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tf
import time as ti
Window=tk.Tk()
Window.title("Progress bar")
Window.geometry("1180x700+300+100")

font=tf.Font(size=15, weight="bold")

top_label2=tk.Label(Window, text="        ", font=font)
top_label2.grid(row=0, column=3)

Title_label=tk.Label(Window, text="모터 이동 설정", font=font)
Title_label.grid(row=1, column=5)

top_label1=tk.Label(Window, text="Top Motor", font=font)
top_label1.grid(row=2, column=5)
top_prog_Val=tk.DoubleVar()
top_prog=ttk.Progressbar(Window, maximum=100, length=600, mode="indeterminate", variable=top_prog_Val)
top_prog.grid(row=3, column=5)

top_label2=tk.Label(Window, text="        ", font=font)
top_label2.grid(row=4, column=3)

top_P_Ent=tk.Entry(Window, width=5)
top_P_Ent.insert(0, "+LM")
top_P_Ent.grid(row=3, column=4)

top_N_Ent=tk.Entry(Window, width=5)
top_N_Ent.insert(0, "-LM")
top_N_Ent.grid(row=3, column=6)

top_Current=tk.Entry(Window, width=10)
top_Current.insert(0, "top Current")
top_Current.grid(row=4, column=5)

{# top_Start_btn=tk.Button(Window, text="Top_Start", command=top_prog_Start)
# top_Start_btn.pack(side="top")

# top_Stop_btn=tk.Button(Window, text="Top_Stop", command=top_prog_Stop)
# top_Stop_btn.pack(side="top")
}


#---------------left-------------------

label_left1=tk.Label(Window, text="   ", font=font)
label_left1.grid(row=7, column=0)

label_left2=tk.Label(Window, text="Left Motor", font=font)
label_left2.grid(row=7, column=1)

left_prog_Val=tk.DoubleVar()
left_prog=ttk.Progressbar(Window, maximum=100, length=400,orient="vertical", mode="indeterminate", variable=left_prog_Val)
left_prog.grid(row=7, column=2)

def left_prog_Stop():
    left_prog.stop()
    print(left_prog_Val.get())

def left_prog_Start():
    left_prog.start(100)
    return
    global n
    for i in range(n):
        pass
    pass

left_P_Ent=tk.Entry(Window, width=5)
left_P_Ent.insert(0, "+LM")
left_P_Ent.grid(row=5, column=2)

left_N_Ent=tk.Entry(Window, width=5)
left_N_Ent.insert(0, "-LM")
left_N_Ent.grid(row=8, column=2)

left_Current=tk.Entry(Window, width=10)
left_Current.insert(0, "left Current")
left_Current.grid(row=7, column=3)

{# left_Start_btn=tk.Button(Window, text="left_Start", command=left_prog_Start)
# #left_Start_btn.pack(side="left", anchor="w")

# left_Stop_btn=tk.Button(Window, text="left_Stop", command=left_prog_Stop)
# #left_Stop_btn.pack(side="left",anchor="w")
}

#---------------Bottom-------------------

label_bottom=tk.Label(Window, text="Bottom Motor", font=font)
label_bottom.grid(row=10, column=5)

bottom_prog_Val=tk.DoubleVar()
bottom_prog=ttk.Progressbar(Window, maximum=100, length=600, mode="indeterminate", variable=bottom_prog_Val)
bottom_prog.grid(row=11, column=5)

bottom_P_Ent=tk.Entry(Window, width=5)
bottom_P_Ent.insert(0, "+LM")
bottom_P_Ent.grid(row=11, column=6)

bottom_N_Ent=tk.Entry(Window, width=5)
bottom_N_Ent.insert(0, "-LM")
bottom_N_Ent.grid(row=11, column=4)

bottom_Current=tk.Entry(Window, width=10)
bottom_Current.insert(0, "bottom Current")
bottom_Current.grid(row=9, column=5)

#---------------Right-------------------

label_right2=tk.Label(Window, text="Right Motor", font=font)
label_right2.grid(row=7, column=10)

right_prog_Val=tk.DoubleVar()
right_prog=ttk.Progressbar(Window, maximum=100, length=400,orient="vertical", mode="indeterminate", variable=right_prog_Val)
right_prog.grid(row=7, column=9)

right_P_Ent=tk.Entry(Window, width=5)
right_P_Ent.insert(0, "+LM")
right_P_Ent.grid(row=5, column=9)

right_N_Ent=tk.Entry(Window, width=5)
right_N_Ent.insert(0, "-LM")
right_N_Ent.grid(row=8, column=9)

right_Current=tk.Entry(Window, width=10)
right_Current.insert(0, "right Current")
right_Current.grid(row=7, column=7)


Window.mainloop()