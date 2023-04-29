# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:21:42 2023

@author: monji
"""

import tkinter

def skip():
    print("test")

tki = tkinter.Tk()

tki.geometry("800x600")

tki.title("ゴミカスクトゥルフ")

lbl_title = tkinter.Label(
    text="たのしいたのしいゴミみてぇなクトゥルフ神話TRPG", 
    font=("HGｺﾞｼｯｸE", "20", "bold"), 
    bg=("#c8bfe7")
    )
lbl_title.pack(side="top")

lbl_Me = tkinter.Label(text="目星成功率：６０％", font=("HGｺﾞｼｯｸE", "15"))
lbl_Me.place(x=70, y=70)
lbl_Ki = tkinter.Label(text="聞き耳成功率：４０％", font=("HGｺﾞｼｯｸE", "15"))
lbl_Ki.place(x=70, y=100)

lbl_text = tkinter.Label(text="test", font=("Myrica M", "15", "bold"))
lbl_text.place(x=70, y=250)

btn_skp = tkinter.Button(text="▽", command=skip())
btn_skp.place(x=500, y=300)

tki.mainloop()