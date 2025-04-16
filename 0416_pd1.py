import os           #미리 불러놓기
import pandas as pd 

os.getcwd()         #현재 파일 위치
df = pd.read_csv('D:/python-workspace/codes/data/gapminder.tsv',sep = '\t')

print(df.shape)     #구조 보기  행과 열 개수 확인
df.shape[0]    
df.shape[1]


print("*    *   *   *   *  \n*  *   *   *   *")
df.columns
print(df.dtypes)    #타입만 보여줌 int64 = 8바이트
print(df.info())    #자료형 뿐 아니라 전부 보여줌
print(df.head())    #따로 입력 안할 경우 5개의 행만

year_df = df['year']
year_df 

print(df.tail())     #뒤에서 5개의 행

print("*    *   *   *   *  \n*  *   *   *   *")

country_df = df['country']
print(country_df)

##리스트로 열 데이터 추출
subset = df[['country','continent','year']]  #이중으로 써야됨!
colums_ls = df[['country','continent','year']] #리스트쓰는 다른 방법
subset = colums_ls
print(subset)


print("*    *   *   *   *  \n*  *   *   *   *")

df.loc[0]   #0번째 행
df.loc[99]  #99를 사용하여 100번째 행을 출력

print(df.loc[[0,99,999]])  #첫번째, 100번째, 1000번째 행 데이터 추출 / 리스트 이중 꼭 확인!

print("*    *   *   *   *  \n*  *   *   *   *")

number_of_rows = df.shape[0]  #행 개수를 먼저 구함
last_row_index = number_of_rows -1 #전체 행 개수에서 -1하여 마지막 행의 인덱스 구함
print(df.loc[last_row_index])  #마지막 행 데이터 추출 / 세로로 뜨며 행번호는 뜨지 않음

print(df.tail(n=1))    #tail메소드로 마지막 행 데이터 추출 가능 / 가로로 뜨며 행번호와 함께 보여줌
