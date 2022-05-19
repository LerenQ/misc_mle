import numpy as np
import pandas as pd 
import statsmodels.api as sm
from functools import reduce


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
        self.Ybar = np.dot(self.beta.T, X.T)
        return self.Ybar

    def rsquare(self):
        ss_residual = sum((self.Y-self.Ybar)**2)
        ss_total = sum((self.Y-np.average(self.Y))**2)
        ans = 1 - ss_residual/ss_total
        return ans
    
    def rsquare_adj(self):
        numerator = sum((self.Y-self.Ybar)**2)/(len(self.X)-len(self.X[0]-1))
        demoninator = sum((self.Y-np.average(self.Y))**2)/(len(self.X)-1)
        ans = 1 - numerator/demoninator
        return ans

data = pd.read_csv('../data/Mall_Customers.csv',index_col='CustomerID')
data.drop_duplicates(inplace=True)
X0 = data.iloc[:, [2, 3]].values
X = np.concatenate((X0, np.ones((len(X0),1))),axis=1)
Y = np.squeeze(data.iloc[:, [1]].values)
# print(X)
# print(Y)
obj = OLS(X, Y)
obj.fit()
ans = obj.predict(X)
print(ans)
print(obj.beta)
print(obj.rsquare())
print(obj.rsquare_adj())

X = sm.add_constant(X0)
mod = sm.OLS(Y, X)
res = mod.fit()
print(res.summary())
print(res.params)
print(res.predict())