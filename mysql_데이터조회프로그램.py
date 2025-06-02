import pymysql

# 전역변수 선언부
con, cur = None, None

data1, data2, data3, data4 = "","","",""

row=None

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='0000', db = 'madang', charset='utf8')

cur = conn.cursor()

cur.execute("SELECT * FROM book")

print("책id                  책이름                        출판사          가격")
print("----------------------------------------------------------------------")

while(True):
    row=cur.fetchone()
    if row == None : 
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s      %15s    %20s    %d" %(data1, data2, data3, data4))
    
conn.close()

