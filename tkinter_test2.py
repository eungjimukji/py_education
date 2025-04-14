#절대 위치 배치 관리자 place(x,y) 좌표로 직접 배치
from tkinter import *
window = Tk()

w  = Label(window, text="박스 #1", bg="red", fg="white")
w.place(x=0,y=0)
w  = Label(window, text="박스 #2", bg="green", fg="black")
w.place(x=20,y=20)
w  = Label(window, text="박스 #3", bg="blue", fg="white")
w.place(x=40,y=40)

#pack()사용 시 위젯을 위/아래/왼/오른쪽 방향으로 "쌓아올림"의 형태
# w  = Label(window, text="박스 #1", bg="red", fg="white")
# w.pack()
# w  = Label(window, text="박스 #2", bg="green", fg="black")
# w.pack()
# w  = Label(window, text="박스 #3", bg="blue", fg="white")
# w.pack()

window.mainloop()       #윈도우 실행