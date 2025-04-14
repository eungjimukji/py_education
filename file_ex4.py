#사용자가 입력하는 파일에 있는 각 문자들이 나타내는 빈도를 계산하는 프로그램을 작성하라. 
char_count = {}

infile = open("D:\\input.txt","r")
for line in infile:
    for ch in line:
        if ch in char_count:
            char_count[ch] += 1     #딕셔너리 안에 있으면 글자 value에 1더하기
        else : 
            char_count[ch] = 1          #딕셔너리 안에 없으면 ch : 1 생성
infile.close()      #닫아주기 !
            

outfile =  open("D:\\output.txt","w")    
for ch,count in char_count.items():
     outfile.write(f"'{ch}': {count}")        #파일에 저장
outfile.close()     #닫아주기 !


#with를 사용하기
# with open("D:\\output.txt","w") as outfile:
#     for ch,count in char_count.items():
#         outfile.write(f"'{ch}':{count}")
#outfile.close() 
    
