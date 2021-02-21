from sklearn.datasets import fetch_california_housing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

# X, y = make_regression(n_samples=100, n_features=2, n_informative=1, noise=0.01)
X, y = fetch_california_housing(return_X_y=True)
# print(X)
# print(y)

from sklearn.linear_model import SGDRegressor

regressor = SGDRegressor()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

regressor.fit(X_train, y_train)
predictions = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error
print(mean_squared_error(predictions, y_test))


