#구구단 2단 프로그램 만들기

def gugu(n):        #1~9까지 곱한 값
    result = []     #저장할 리스트 만들기
    
    # result.append(n*1)    append()가 9까지 반복됨
    # result.append(n*2)
    # result.append(n*3)
    # result.append(n*4)
    # result.append(n*5)
    # result.append(n*6)
    # result.append(n*7)
    # result.append(n*8)
    # result.append(n*9)
    i = 1
    while i < 10:       #i가 9일때까지 반복하고 반복할 때마다 i에 1씩 더함
        result.append(n*i)
        i += 1
    return result

print(gugu(2))