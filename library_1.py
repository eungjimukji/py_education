import datetime as dt
import time as tm
import random

day1 = dt.date(2025, 4, 15)
day2 = dt.date(1997, 8, 29)

day1.weekday()

#날짜 계산
dyff = day1 - day2
print(dyff)


#time 라이브러리 표현
tm.time()
tm.strftime('%x', tm.localtime(tm.time()))   #현재 설정된 지역의 날짜 출력
tm.strftime('%c')   #Tue Apr 15 12:19:38 2025 날짜와 시간 출력 

tm.strftime('%yy-%mm-%dd', tm.localtime(tm.time()))  #25y-04m-15d

tm.strftime('%Y-%m-%d', tm.localtime(tm.time()))     #2025-04-15

for i in range (10):
    print(i)
    tm.sleep(1)   #1초씩 멈춰가며 반복문 실행
