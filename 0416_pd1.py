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

df.loc[:,['year']]      #'year'열의 : 모든 행 데이터 / iloc속성에 열 이름을 사용하면 오류 발생
print("*    *   *   *   *  \n*  *   *   *   *")

small_range = list(range(5))    #0이상 5미만 정수 반환
print(small_range)
subset1 = df.iloc[:, small_range]   #범위에 맞는 열을 df에서 추출
print(subset1)                  #하지만 range를 쓸 경우 리스트로 변환해야하기 때문에 번거로움

print("*    *   *   *   *  \n*  *   *   *   *")

#슬라이싱 구문 활용
subset2 = df.iloc[:, :5]        #간편하게 range(5)똑같이 출력 가능
subset3 = df.iloc[:, 0:6:2]     #0이상 6미만 2간격으로 0,2,4 열 추출

df.iloc[[0,99,999], [0,3,5]]   #1,4,6 열의 1,100,1000번째 행 데이터 추출 iloc이라 정수 쓰기
df.loc[[0,99,999], ['country', 'lifeExp','gdpPercap']]  #위와 동일하게 추출 loc를 썼기 때문에 문자열 입력


