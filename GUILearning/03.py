# Listbox 学习
import tkinter as tk

# 建立窗口 名字 和长宽
window = tk.Tk()
window.title('My window')
window.geometry('600x500')

ver1 = tk.StringVar()
l = tk.Label(window, bg= 'yellow', width= 20, textvariable= ver1)
l.pack()

def print_selection():
    var = e.get()
    t.insert('insert', var)
    
btn = tk.Button(window, text= 'print selection', bg='light green', width= 15, height = 5, command = print_selection) #hit_me是提前做好的函数
btn.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44)) #为什么要加两个括号？ 因为这是一个tuple
lb = tk.Listbox(window, listvariable= var2) #listvariable是Listbox的一个参数
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end', item) #end是插入到最后一个位置
lb.insert(1, 'first') #插入到第一个位置
lb.insert(2, 'second')
lb.delete(2) #删除第二个位置
lb.pack()

lb = tk.Listbox(window, )