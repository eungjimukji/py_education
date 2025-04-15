#격자 배치 관리자  grid()표 형태로 배치 - 복잡한 레이아웃의 경우
from tkinter import *

def process():          #이벤트 처리
    e2.insert(0,"100")  #삽입 위치, 삽입 텍스트 내용 2,"100"인 경우 0,1,2 자리에 100을 넣어라 가 됨


window = Tk()

l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")
l1.grid(row=0,column=0) #행,렬 지정 해줘야함 항상 0부터 시작
l2.grid(row=1,column=0)

e1 = Entry(window)      #텍스트 입력칸 
e2 = Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b1 = Button(window, text="화씨->섭씨", command=process)  #버튼 생성 / 버튼 클릭 시 실행 함수 지정 *함수이지만 ()붙이지 않음
b2 = Button(window, text="섭씨->화씨")
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)

window.mainloop()       #윈도우 실행