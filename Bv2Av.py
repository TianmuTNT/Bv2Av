from tkinter import Label, Button, Entry, Tk
from tkinter.messagebox import showinfo
from pyperclip import copy

def bv2av(bv):
    bv = bv[2:]
    value = {"1":13, "2":12, "3":46, "4":31, "5":43, "6":18,
            "7":40, "8":28, "9":5, "A":54, "B":20, "C":15,
            "D":8, "E":39, "F":57, "G":45, "H":36, "J":38,
            "K":51, "L":42, "M":49, "N":52, "P":53, "Q":7,
            "R":4, "S":9, "T":50, "U":10, "V":44, "W":34,
            "X":6, "Y":25, "Z":1, "a":26, "b":29, "c":56,
            "d":3, "e":24, "f":0, "g":47, "h":27, "i":22,
            "j":41, "k":16, "m":11, "n":37, "o":2, "p":35,
            "q":21, "r":17, "s":33, "t":30, "u":48, "v":23,
            "w":55, "x":32, "y":14, "z":19}
    replace = []
    for i in bv:
        replace.append(value[i])
    replace[0] = replace[0] * 58 ** 6
    replace[1] = replace[1] * 58 ** 2
    replace[2] = replace[2] * 58 ** 4
    replace[3] = replace[3] * 58 ** 8
    replace[4] = replace[4] * 58 ** 5
    replace[5] = replace[5] * 58 ** 9
    replace[6] = replace[6] * 58 ** 3
    replace[7] = replace[7] * 58 ** 7
    replace[8] = replace[8] * 58
    add = sum(replace)
    new = add - 100618342136696320
    av = "AV" + str(177451812 ^ new)
    return av

def convert():
    bv = bv_entry.get()
    try:
        av = bv2av(bv)
    except Exception:
        av = "错误"
    finally:
        av_text.config(text=av)

def copy_av():
    text = av_text["text"]
    if text != "错误" and text != "":
        copy(text)
        showinfo("提示", "复制成功！")

root = Tk()
root.title("BV转AV工具")
root.geometry("500x250")

bv_label = Label(root, text="BV号", font=("TkDefaultFont", 20, "bold"))
bv_label.pack(pady=30)

bv_entry = Entry(root, font=("TkDefaultFont", 20, "bold"), bd=3)
bv_entry.pack(pady=(0, 30), padx=50)

av_label = Label(root, text="AV号", font=("TkDefaultFont", 20, "bold"))
av_label.pack(pady=30)

av_text = Label(root, text="", font=("TkDefaultFont", 20, "bold"))
av_text.pack(pady=30)

av_copy = Button(root, text="复制", font=("TkDefaultFont", 20, "bold"), command=copy_av, bd=3)
av_copy.pack(pady=30)

convert_button = Button(root, text="转换", font=("TkDefaultFont", 20, "bold"), command=convert, bd=3)
convert_button.pack(pady=30)

bv_label.place(x=50, y=30)
bv_entry.place(x=150, y=30)
av_label.place(x=50, y=100)
av_text.place(x=200, y=100)
av_copy.place(x=250,y=160)
convert_button.place(x=350, y=160)

root.mainloop()