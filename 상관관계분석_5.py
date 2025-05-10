import  pandas as pd

# GDP 성장률과 인구수의 상관관계 분석

data = {'국가' :['미국', '일본', '영국', '프랑스', '독일', '이탈리아', '캐나다',
                '대한민국', '러시아', '중국', '인도', '인도네시아', '아르헨티나',
                '브라질', '멕시코', '호주', '남아프리카공화국', '사우디아라비아',
                '튀르키예', '유럽연합(EU)'],
        'GDP 성장률' :[0.9, 0.6, 0.4, 0.5, 1.1, 1.7, 3.9, 1.4, -3.7, 2.9, 6.3,
                    5.01, 5.9, 3.6, 3.5, 5.9, 4.1, 5.4, 3.9, 1.9],
        '인구수' :[334, 125, 67.53, 67.65, 83.16, 59.24, 38.44, 51.74, 146, 1412,
                1380, 273, 45.81, 213, 126, 25.77, 60.14, 34.11, 84.68, 343]}

df = pd.DataFrame(data)
print(df)


# 아래 코드로 진행 시 문자열 컬럼 때문에 에러 발생 
# pearsonCoef = df.corr(method='pearson')
# print("Pearson Correlation Analysis")
# print(pearsonCoef)

# spearmanCoef = df.corr(method='spearman')
# print("\nSpearman Correlation Analysis")
# print(spearmanCoef)

# kendallCoef = df.corr(method='kendall')
# print("\nKendall Correlation Analysis")
# print(kendallCoef)



# 수치형 컬럼만 추출
numeric_df = df[['GDP 성장률', '인구수']]
# numeric_df = df.select_dtypes(include='number')   문자열 컬럼 자동 제외하는 코드

# 상관계수 추출
pearson_corr = numeric_df.corr(method='pearson')
print("Pearson Correlation Analysis")
print(pearson_corr)
spearman_corr = numeric_df.corr(method='spearman')
print("Pearson Correlation Analysis")
print(spearman_corr)
kendall_corr = numeric_df.corr(method='kendall')
print("Pearson Correlation Analysis")
print(kendall_corr)

#           GDP 성장률       인구수
# GDP 성장률  1.000000  0.198924
# 인구수      0.198924  1.000000
# Pearson Correlation Analysis
#           GDP 성장률       인구수
# GDP 성장률  1.000000 -0.196388
# 인구수     -0.196388  1.000000
# Pearson Correlation Analysis
#           GDP 성장률       인구수
# GDP 성장률  1.000000 -0.137568
# 인구수     -0.137568  1.000000