import numpy as np
import statsmodels.api as sm


X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([3, 4, 5, 6, 7])  


X = sm.add_constant(X)


model = sm.OLS(y, X).fit()


print(model.summary())

