#빈 윈도우 창
from tkinter import *
window = Tk()

# window.mainloop()
#버튼 추가

button = Button(window,text = "클릭하슈!")
button.pack()           #버튼을 윈도우에 배치

window.mainloop()       #윈도우 실행