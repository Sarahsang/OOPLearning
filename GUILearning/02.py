# entry & text 学习
import tkinter as tk

# 建立窗口 名字 和长宽
window = tk.Tk()
window.title('My window')
window.geometry('600x500')

#输入框输入值
e = tk.Entry(window, show=None) # 如果想要像密码一样隐藏则 show ='*' 或者随便什么字符 show= '^'都可以
e.pack()

#函数定义按钮拿到输入的值
def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var) #insert还可以设置具体位置比如 t.insert(2.1, var) 即第二行的第二个（从零开始1就是第二个）

btn1 = tk.Button(window, text= 'insert point', bg='light green', width= 15, height = 5, command=insert_point) #hit_me是提前做好的函数
btn1.pack()

btn2 = tk.Button(window, text= 'insert end', bg='light green', width= 15, height = 5, command=insert_end) #hit_me是提前做好的函数
btn2.pack()

#文本框
t = tk.Text(window, height=2)
t.pack()

window.mainloop() # 一个循环