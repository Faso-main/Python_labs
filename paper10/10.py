import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

file_path=os.path.join('paper10','Boston.csv')
data = pd.read_csv(file_path)

X = data['rm']
y = data['medv']


def linear_regression(X, y):
    X_b = np.c_[np.ones((X.shape[0], 1)), X] 
    theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)  
    return theta_best


theta_best = linear_regression(X, y)
intercept, slope = theta_best

y_pred = intercept + slope * X

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='purple', label='Исходные данные')
plt.plot(X, y_pred, color='blue', label='Линия регрессии')
plt.xlabel('Количество комнат (rm)')
plt.ylabel('Цена жилья (medv)')
plt.title('Линейная регрессия на датасете Boston')
plt.legend()
plt.grid()
plt.show()
