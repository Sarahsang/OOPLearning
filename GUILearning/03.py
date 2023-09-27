# Listbox 学习
import tkinter as tk

# 建立窗口 名字 和长宽
window = tk.Tk()
window.title('My window')
window.geometry('600x500')


btn = tk.Button(window, text= 'insert point', bg='light green', width= 15, height = 5, command=insert_point) #hit_me是提前做好的函数
btn.pack()
