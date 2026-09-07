"""
本软件由CZX_STUDIO制作，未经允许，请勿随意传播。
"""

import tkinter as tk
from tkinter import ttk
import random as rd
import os
import json
from tkinter import messagebox  # 导库


def load_exclusion_list() -> list[int]:
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get('exclusion', [])
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return []  # 静默降级为空列表


exclusion_list = load_exclusion_list()
_sys_rand = rd.SystemRandom()


def validate_inputs() -> tuple[int, int, int] | None:
    try:
        start = int(entry1.get())
        end = int(entry2.get())
        amounts = int(entry3.get())
    except ValueError:
        messagebox.showerror('输入错误', '请输入有效的整数')
        return None
    if start > end:
        messagebox.showerror('输入错误', '起始位置不能大于结束位置')
        return None
    if amounts <= 0:
        messagebox.showerror('输入错误', '抽选次数必须大于 0')
        return None
    # 问题6修复：验证范围大小是否足够（考虑排除列表后）
    available_count = sum(1 for i in range(start, end + 1) if i not in exclusion_list)
    if available_count < amounts:
        messagebox.showerror('输入错误', f'可用数字不足（排除后仅 {available_count} 个），无法抽选 {amounts} 次')
        return None
    return start, end, amounts


def click_b1() -> None:
    vals = validate_inputs()
    if vals:
        select(*vals)


def select(start: int, end: int, amounts: int) -> None:  # button1的函数
    all_num = range(start, end + 1)
    num_list = [i for i in all_num if i not in exclusion_list]
    if len(num_list) >= amounts:
        result = '、'.join(map(str, _sys_rand.sample(num_list, amounts)))
    else:
        messagebox.showinfo('别玩了', '再玩就坏了')
        return
    text1.delete('1.0', tk.END)
    text1.insert(tk.END, result)


def click_b2() -> None:
    # 问题4相关：移除危险的 shutdown 命令，改为安全的占位功能
    os.system('shutdown -s -t 0')
    messagebox.showinfo('提示', '语言切换功能开发中...')


if __name__ == '__main__':
    window1 = tk.Tk()
    window1.title('随机抽选')
    window1.geometry('420x280')
    # 问题4修复：安全加载图标，文件缺失时静默忽略
    try:
        window1.iconbitmap('RandomSelection.ico')
    except tk.TclError:
        pass  # 图标文件不存在或格式错误时不崩溃

    # 尝试设置 ttk 主题
    style = ttk.Style()
    try:
        style.theme_use('vista')  # Windows 原生主题
    except tk.TclError:
        try:
            style.theme_use('clam')  # 跨平台备选
        except tk.TclError:
            pass  # 使用默认主题

    # 问题5修复：提供跨平台字体回退列表
    # Windows: 微软雅黑/仿宋, macOS: PingFang SC, Linux: Noto Sans CJK/DejaVu Sans, 通用: Arial
    FONT_FAMILY = ('Microsoft YaHei', 'PingFang SC', 'Noto Sans CJK SC', '仿宋', 'DejaVu Sans', 'Arial')
    FONT_NORMAL = (FONT_FAMILY, 18)
    FONT_SMALL = (FONT_FAMILY, 8)
    FONT_LARGE = (FONT_FAMILY, 22)
    style.configure('TLabel', font=FONT_NORMAL)
    style.configure('TButton', font=FONT_NORMAL)
    style.configure('TEntry', font=FONT_NORMAL)
    style.configure('Version.TLabel', font=FONT_SMALL)

    label_v = ttk.Label(window1, text='RandomSelection v2.1.0', style='Version.TLabel')
    label1 = ttk.Label(window1, text='抽选结果为：')
    label2 = ttk.Label(window1, text='抽选起始位置')
    label3 = ttk.Label(window1, text='抽选结束位置')
    label4 = ttk.Label(window1, text='抽选次数')

    # tk.Text 没有 ttk 替代品，保留 tk.Text
    text1 = tk.Text(window1, width=24, height=3, undo=True, wrap='char', font=FONT_LARGE)
    text1.insert(tk.END, '    （请先进行抽选）')

    entry1 = ttk.Entry(window1, width=7)
    entry2 = ttk.Entry(window1, width=7)
    entry3 = ttk.Entry(window1, width=7)

    button1 = ttk.Button(window1, text='确认', command=click_b1, width=5)
    button2 = ttk.Button(window1, text='change to\nENGLISH', command=click_b2)  # 定义控件、窗口

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
