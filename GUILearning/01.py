import tkinter as tk

window = tk.Tk()
window.title('My window')
window.geometry('500x400')

#

Title = tk.Lable(window, text='Welcome!',bg='light blue', font=('Arial', 12), width=12, height=2)

Title.pack()

btn = tk.Button(window, text='Click to Enter', width= 10, height = 3, command=hit_me) #hit_me是提前做好的函数


window.mainloop()