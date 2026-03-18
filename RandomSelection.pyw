"""
本软件由CZX_STUDIO制作，未经允许，请勿随意传播。
"""

import tkinter as tk
import random as rd
from tkinter import messagebox  # 导库


def click_b1():  # button1的函数
    i = 0
    num_list = []  # 函数初始化
    while i < int(entry2.get()):
        r_num = rd.randint(1, int(entry1.get()))
        if r_num not in num_list:
            num_list.append(r_num)
        else:
            continue
        i += 1  # 循环抽取学号
    result = '、'.join(map(str, num_list))
    messagebox.showinfo('抽选结果', result)  # 输出结果
    label4['text'] = result
    label4.update()


window1 = tk.Tk()
window1.title('随机抽选')
window1.geometry('500x300')
window1.iconbitmap('RandomSelection.ico')
label1 = tk.Label(window1, text='请输入抽选样本总数（上）与抽选次数（下）', font=('仿宋', 14))
label2 = tk.Label(window1, text='RandomSelection v1.0.1', font=('仿宋', 8))
label3 = tk.Label(window1, text='上一次的抽选结果为：', font=('仿宋', 14))
label4 = tk.Label(window1, text='（请先进行抽选）', font=('仿宋', 20))
entry1 = tk.Entry(window1, font=('仿宋', 14))
entry2 = tk.Entry(window1, font=('仿宋', 14))
button1 = tk.Button(window1, text='确认', command=click_b1, font=('仿宋', 14))  # 定义控件、窗口
label1.pack()
entry1.pack()
entry2.pack()
button1.pack()
label3.pack()
label4.pack()
label2.pack(anchor='e', side='bottom')
window1.mainloop()  # 放置控件

"""
\u0049\u0020\u006c\u006f\u0076\u0065\u0020\u9648\u7430\u6c50
"""
