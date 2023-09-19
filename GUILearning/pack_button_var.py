import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('500x400')

#
var=tk.StringVar()
var.set("Click to Enter")

button_clicked = False

def hit_me():
    global button_clicked
    if button_clicked == False:
        var.set("You clicked me!")
        button_clicked = True
    else:
        var.set("HaHa")
        button_clicked= False

'''在Tkinter中，控件（如按钮、标签等）需要通过几何管理器（如 pack(), grid() 或 place()）来安排其在窗口或其他父容器中的位置。如果你创建了一个控件但没有使用几何管理器来安排它，那么这个控件就不会显示。

btn.pack() 是使用 pack 几何管理器来安排 btn（即按钮）的方法。这个方法告诉Tkinter将按钮放置在其父容器（在这个例子中是 window）里，并自动为它分配合适的大小和位置。

简单来说，pack() 是让控件在界面上可见的方式之一。如果你不调用 btn.pack()，按钮 btn 就不会出现在窗口中。'''

Title.pack()

btn = tk.Button(window, textvariable=var, bg='light green', width= 15, height = 5, command=hit_me) #hit_me是提前做好的函数
btn.pack()

window.mainloop()