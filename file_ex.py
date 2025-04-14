#연설문 데이터 분석 / 특수문자 삭제와 소문자 변환 후 단어별로 분리하여 단어 별 빈도수 
import string

#파일 열기(읽기 모드)
infile = open('D:\\input1.txt','r')
#소문자로 변환
data = infile.read().lower()
#구두점 제거
translator = str.maketrans("",'',string.punctuation)
data = data.translate(translator)
#단어별로 분리
words = data.split()


word_count = {}
#결과출력

for word in words:
    if word in word_count:
        word_count[word] += 1 #이미 존재하면 +1
    else :
        word_count[word] = 1 #없으면 1로 시작

#결과 출력
# outfile = open('D:\\input2.txt','w')   <오름차순 정리 안됨 
# for word, count in word_count.items():
#     outfile.write(f"{word}:{count}\n")

outfile = open('D:\\input2.txt','w')     
for word in sorted(word_count.keys()):    #sorted로 오름차순 정리
    count = word_count[word]
    outfile.write(f"{word}:{count}\n")


#등장 횟수 기준으로 정렬 시 
# outfile = open('D:\\input2.txt','w')     
# for word,count in sorted(word_count.items(), key=lambda x:x[1],reverse=True):   
#     count = word_count[word]
#     outfile.write(f"{word}:{count}\n")


outfile.close()