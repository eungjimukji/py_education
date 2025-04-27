#그룹화 연습과 그래프 그리기
import pandas as pd

df = pd.read_csv('D:/python-workspace/codes/data/gapminder.tsv',sep = '\t')

print(df.groupby('year')['lifeExp'].mean())  #연도별 그룹화, 열 선택, 평균 계산

grouped_year_df = df.groupby('year')
print(type(grouped_year_df))    #그룹화한 객체 DataFrameGroupBy를 반환
print(grouped_year_df)    #df내용이 아닌 저장된 메모리 주소만 출력

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
# print(type(grouped_year_df_lifeExp))

# print(grouped_year_df_lifeExp)

main_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(main_lifeExp_by_year)    #그룹화한 시리즈의 평균 구함. float64이므로 mean()메소드 사용 가능

#2개 이상 열 그룹화하기
multi_group_var = df.groupby(['year','continent'])[['lifeExp','gdpPercap']].mean() 
print(multi_group_var)

flat = multi_group_var.reset_index()    #기존 df구조와 같이 계층 구조를 없애고 df를 평탄화 하는 reset_index()메소드


print(df.groupby('continent')['country'].nunique())    # ~별 ~을 / 그룹화한 데이터 개수 구하기 .nunique()

print(df.groupby('continent')['country'].value_counts())    #지정한 열이나 행의 개수를 구함  .value_count()

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
global_yearly_life_expectancy.plot()    #df을 대상으로 plot()메소드 호출하여 그래프로 나타냄

