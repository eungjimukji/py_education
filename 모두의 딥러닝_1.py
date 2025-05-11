from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from matplotlib import pyplot
from sklearn.preprocessing import StandardScaler

import pandas as pd
import matplotlib.pyplot as plt


# 피마 인디언 당뇨병

df = pd.read_csv('./pima-indians-diabetes3.csv')
# print(df.head())      #768행/9컬럼
# print(df.info())      #pregnant,plasma,pressure,thickness,insulin,bmi,pedigree,age,diabetes
# print(df.describe())

# 세부 정보 X로 지정 / 모든 행, 0~7번 열까지
X = df.iloc[:,0:8]  

# 당뇨병 여부 y로 지정 / 모든 행, 8번 열만
y = df.iloc[:,8]

# 표준화 전/후 데이터의 분포 변화 시각 비교 : 모든 피처가 평균 0, 분산 1로 정규화되었는지 KDE 그래프로 보는 것.
ss = StandardScaler()
scaled_X = pd.DataFrame(ss.fit_transform(X), columns=X.columns)
fig, ax = plt.subplots(1, 2, figsize=(12,4))
X.plot(kind='kde', title='Raw data', ax=ax[0])
scaled_X.plot(kind='kde', title='StandardScaler', ax=ax[1])
# plt.show() # < 확인 코드


# 데이터 스케일링을 마치고 학습셋과 데이터셋 75:25
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# 사이킷런 라이브러리에서 적절한 알고리즘 불러옴
# fit() 학습
# predict() 예측

from sklearn.tree import DecisionTreeClassifier

# 학습 환경 설정
# classifier = DecisionTreeClassifier()
# classifier.fit(X_train, y_train)

# # 테스트셋 적용
# y_pred = classifier.predict(X_test)

# # 계층별 교차 검증 환경 설정
# skf = StratifiedKFold(n_splits=10, shuffle=True)
# # 교차 검증을 통한 정확도 계산
# accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=skf)
            # 교차 검증을 통해 모델의 성능 평가하는 함수

# 정확도와 표준편차 출력
# print("Accuacy: {:.2f}%".format(accuracies.mean()*100))
# print("Standard Deviation: {:.2f}%".format(accuracies.std()*100))

# # random_state 100인 경우
# # Accuacy: 72.41% / Standard Deviation: 5.75%

# # random_state 0인 경우
# # Accuacy: 68.56% / Standard Deviation: 5.39%



# 랜덤 포레스트 분류기로 학습 ->모델을 50개의 트리 사용하여 훈련하고 데이터를 10개의 부분으로 나눔

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=50)  # 랜덤 포레스트 분류기 초기화 , 트리 개수 50
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

skf = StratifiedKFold(n_splits=10, shuffle=True)

accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=skf)
print("Accuacy: {:.2f}%".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f}%".format(accuracies.std()*100))
# Accuacy: 73.96%
# Standard Deviation: 5.46%


