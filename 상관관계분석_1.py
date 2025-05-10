import pandas as pd

# 두 변수 사이 관계의 강도와 방향을 파악하는 통게 기법
# 양의 상관관계 : x가 커질수록 y도 커짐
# 음의 상관관계 : x가 커질수록 y는 작아짐
# 상관관계 없음 : x가 커길 때 y는 커질 수도, 작아질 수도 있음




# 리스트에 데이터 삽입
engListening = [30,60,90]
engScore = [70,80,90]

# 리스트를 df로 변환하기
data = { 'engListening' : engListening , 'engScore': engScore}
df = pd.DataFrame(data)






# 상관분석 수행
# 피어슨 상관분석 : 일반적인 상관분석 방법. 데이터가 많지 않을 경우 엑셀에서도 실행 가능
coef = df.corr(method= 'pearson')
print(coef)

#              engListening  engScore      양의 상관관계
#engListening           1.0       1.0
#engScore               1.0       1.0







# 데이터 양이 적어 데이터 추가 후 산포도 확인

import matplotlib.pyplot as plt

engListening = [30,60,90,31,32,69,92,99]
engScore = [70,80,90,70,71,85,90,92]
data2 = { 'engListening' : engListening , 'engScore': engScore}
df2 = pd.DataFrame(data2)

# 산점도 그래프 x,y좌표 설정
plt.scatter(df2['engListening'], df2['engScore'])
#plt.show()  #완벽한 선형 상관관계가 아니라 모든 점을 직선 한개로 이을 수 없음




# 상관분석 2
coef= df2.corr(method='pearson')
print(coef)  

#              engListening  engScore   완벽한 선형 상관관계x but 0.5보다 크므로 매우 강한 선형 상관성이 있다고 해석
#engListening      1.000000  0.995829
#engScore          0.995829  1.000000