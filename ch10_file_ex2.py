#파일 "input.txt"의 모든 줄을 읽어서 리스트에 저장하는 프로그램을 작성하라.
lines = []

with open("D:\\input.txt", "r") as file:    #오픈된 파일을 별칭 사용하여 file이라 정의
    for line in file:
        lines.append(line)      #lines 리스트에 line을 항목 추가

#결과 출력(확인용)
print(lines)

    
    