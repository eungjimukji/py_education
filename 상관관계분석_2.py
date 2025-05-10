import pandas as pd

engListening = [30,60,90,31,32,69,92,99]
engScore = [70,80,90,70,71,85,90,92]
engClass = [60,120,120,60,60,180,120,120]
engReading = [40,45,60,20,15,70,60,80]

data3 = { 'engListening' : engListening , 'engReading' : engReading, 'engClass' : engClass, 'engScore': engScore}
df3 = pd.DataFrame(data3) 

# print(df3)  데이터프레임 확인


# 피어슨 ) 
#           일반적인 상관분석 방법 / 선형관계를 측정 / Outer에 민감하게 반응
pearsonCoef = df3.corr(method='pearson')
print(pearsonCoef)  
print('----------*----------')
# 스피어만 ) 
#           두 변수가 정규성을 보이지 않을 때 사용하기 적합한 방법 / 선형여부 x 변수 간의 단조 연관성을 측정
spearmanCoef = df3.corr(method='spearman')
print(spearmanCoef)
print('----------*----------')

# 켄달 ) 
#           순위로 표현할 수 있는 data or 표본 크기가 작거나 동점!!!이 많을 때 활용
kendallCoef = df3.corr(method='kendall')
print(kendallCoef)


#               engListening  engReading  engClass  engScore
# engListening      1.000000    0.877201  0.703028  0.995829
# engReading        0.877201    1.000000  0.808755  0.894111
# engClass          0.703028    0.808755  1.000000  0.759453
# engScore          0.995829    0.894111  0.759453  1.000000
# ----------*----------
#               engListening  engReading  engClass  engScore
# engListening      1.000000    0.826362  0.717256  0.988024
# engReading        0.826362    1.000000  0.852757  0.848500
# engClass          0.717256    0.852757  1.000000  0.725950
# engScore          0.988024    0.848500  0.725950  1.000000
# ----------*----------
#               engListening  engReading  engClass  engScore
# engListening      1.000000    0.618284  0.563621  0.963624
# engReading        0.618284    1.000000  0.750568  0.679366
# engClass          0.563621    0.750568  1.000000  0.584898
# engScore          0.963624    0.679366  0.584898  1.000000

# 켄달은 두 변수 간의 순위를 비교하여 연관성을 계산함.
# 즉, 한 변수가 증가할 때 다른 변수가 함께 증가하는 횟수와 감소하는 횟수를 측정하여 횟수의 차이를 상관계수로 표현하는 방법
