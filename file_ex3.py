#사용자가 입력한 텍스트 파일을 열어서 파일 안에 글자가 몇 개나 있는지를 계산하는 프로그램을 작성하라. 
count = 0

filename = input("파일 이름을 입력하세요: ")   
infile = open(filename,"r")        
for line in infile:
    count += len(line)      #글자수 len
    
print(f"파일 안에는 총 {count}개의 글자가 있습니다.")