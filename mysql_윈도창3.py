from tkinter import *
from tkinter import messagebox

def clickbutton():
    messagebox.showinfo('버튼 클릭', '버튼을 클릭했습니다.')



window = Tk()
window.geometry("200x200")

button1 = Button(window, text='요기 눌러요', fg='red', bg='yellow', command=clickbutton)

button1.pack(expand =1)

window.mainloop()
