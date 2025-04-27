#게시판 페이징하기 

def get_total_page(m,n):
    if m % n ==0:       #나머지가 0일 때 오류발생생
        return m // n
    else:
        return m // n + 1
    
a = int(input("총 게시물 개수를 입력하시오:"))
b = int(input("한 페이지에 보여 줄 게시물 수를 입력하시오:"))

result = get_total_page(m=a,n=b)
print("총 페이지수는 {}p 입니다.".format(result))   #format을 이용하여 f-string 쓰지않기 & 총 페이지수 대답

