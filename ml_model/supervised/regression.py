import numpy as np
import pandas as pd 
import statsmodels.api as sm


class OLS:

    def __init__(self, X: 'list(list())', Y: list(), random_seed:int = None) -> None:
        self.X = np.array(X)
        self.Y = np.array(Y)
        self.random_seed = random_seed
        self.beta = None

    def measure(self, d):
        return 

    def fit(self):
        self.beta = np.linalg.multi_dot([np.linalg.inv(np.dot(self.X.T, self.X)), self.X.T, self.Y])

    def predict(self, X):
        return np.dot(self.beta.T, X.T)


data = pd.read_csv('../data/Mall_Customers.csv',index_col='CustomerID')
data.drop_duplicates(inplace=True)
X0 = data.iloc[:5, [2, 3]].values
X = np.concatenate((X0, np.ones((5,1))),axis=1)
Y = np.squeeze(data.iloc[:5, [1]].values)
print(X)
print(Y)
obj = OLS(X, Y)
obj.fit()
ans = obj.predict(X)
print(ans)
print(obj.beta)

X = sm.add_constant(X0)
mod = sm.OLS(Y, X)
res = mod.fit()
print(res.summary())
print(res.params)
print(res.predict())