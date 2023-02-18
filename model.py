import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def evaluate_score(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print(f'mse- {mse:.3f}')
    print(f'rmse- {rmse:.3f}')
    print(f'r2- {r2:.3f}')
    
    return

# 데이터 불러오기
train = pd.read_csv('./data/train5.csv')

# X(독립변수), Y(종속변수) 분할
X = train.drop('match', axis=1)
y = train['match']

# 학습용 데이터와 평가용 데이터로 분할하기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 파이프라인 정의
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('ridge', Ridge())
])

# 탐색할 하이퍼파라미터 값 지정
param_grid = {
    'ridge__alpha': [0.01, 0.1, 1, 10, 150]
}

# 그리드 서치 객체 생성
grid_search = GridSearchCV(pipeline, param_grid, cv=5)

# 모델 학습
grid_search.fit(X_train, y_train)

# 최적의 모델 선택
best_model = grid_search.best_estimator_

# 최적의 하이퍼파라미터 출력
print("Best Parameters: ", grid_search.best_params_)

# 릿지 선형회귀 모델 평가
y_pred = best_model.predict(X_test)
y_pred[y_pred < 0] = 0.

evaluate_score(y_test, y_pred)

# model 저장
joblib.dump(best_model, 'best_model.joblib')

