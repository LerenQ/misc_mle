import numpy as np
from numpy.linalg.linalg import eigvals
import pandas as pd 
import statsmodels.api as sm
from functools import reduce

'''
statsmodel:
https://www.statsmodels.org/dev/_modules/statsmodels/regression/linear_model.html#OLS.fit_regularized
'''

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
        self.Ybar = np.dot(X, self.beta)
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


class LASSO(OLS):

    def __init__(self, X: 'list(list())', Y: list(), lamda, random_seed: int = None) -> None:
        super().__init__(X, Y, random_seed)
        self.lamda = lamda
        self.x_0 = np.random.rand(len(X[0]),1)

    def fit(self):
        eps = 0.01
        maxiter = 200000
        self.beta, self.sse, self.sse_l = self.admm(self.x_0,self.X,self.Y,self.lamda, eps, maxiter)
        
    def lasso_val(self, A, b, x):
        return np.dot((np.dot(A,x)-b).T,(np.dot(A,x)-b))

    def admm(self, x_k, A, b, lambd, eps, maxiter=None):
        value_l = []
        eigval, _ = np.linalg.eig(np.dot(A.T, A))
        l = np.max(eigval)
        z_k = x_k
        w_k = np.random.rand(A.shape[1], 1)
        for i in range(1,maxiter+1):
            value_old = self.lasso_val(A, b, x_k)
            pho_i = np.identity(A.shape[1])*l
            x_k = np.dot(np.linalg.inv(np.dot(A.T,A)+pho_i),(np.dot(A.T,b)+l*(z_k-w_k)))
            temp = np.zeros(z_k.shape)
            temp = np.concatenate((np.abs(x_k+w_k)-lambd/l,temp),axis=1)
            z_k = np.sign(x_k+w_k) * np.max(temp,axis=1).reshape(z_k.shape)
            w_k = w_k + x_k - z_k
            value_new = self.lasso_val(A,b,x_k)

            # print("lasso value step %d = %f" %(i, value_new[0][0]))

            value_l.append(value_new)
            if (abs(value_old[0][0]-value_new[0][0]))<=eps:
                return x_k,value_new,value_l

        return x_k,value_new,value_l


class Ridge(OLS):
    def __init__(self, X: 'list(list())', Y: list(), lamda, random_seed: int = None) -> None:
        super().__init__(X, Y, random_seed)
        self.lamda = lamda
    
    def fit(self):
        exog_dot = np.dot(self.X.T, self.X)
        self.beta = np.linalg.multi_dot([np.linalg.inv(exog_dot + np.identity(exog_dot.shape[0])*self.lamda), self.X.T, self.Y])


# read data
data = pd.read_csv('../data/Mall_Customers.csv',index_col='CustomerID')
data.drop_duplicates(inplace=True)
X0 = data.iloc[:, [2, 3]].values
X = np.concatenate((X0, np.ones((len(X0),1))),axis=1) # add 1 for constant
Y = np.squeeze(data.iloc[:, [1]].values)[:,np.newaxis]
# print(X)
# print(Y)

# # test OLS
# obj = OLS(X, Y)
# obj.fit()
# ans = obj.predict(X)
# print(ans)
# print(obj.beta)
# print(obj.rsquare())
# print(obj.rsquare_adj())
# print(sum((obj.Y-obj.Ybar)**2))

# compare with statmodel
X1 = sm.add_constant(X0)
mod = sm.OLS(Y, X1)
res = mod.fit()
# print(res.summary())
# print(res.params)
# print(res.predict())

# # test Lasso
# # issue: the result diff from statmodel, check;
# import matplotlib.pyplot as plt
# obj = LASSO(X, Y,lamda=0)
# obj.fit()
# print(obj.sse)
# print(obj.predict(X))
# print(obj.beta)
# plt.plot(range(len(value_l)), np.squeeze(value_l))
# plt.show()

# # compare lasso in statmodel
# X1 = sm.add_constant(X0)
# mod = sm.OLS(Y, X1)
# res = mod.fit_regularized(method='sqrt_lasso', alpha=0.0, L1_wt=1.0,)
# # print(res.summary())
# print(res.params)
# print(res.predict())

# # test Ridge
# obj = Ridge(X, Y,lamda=0)
# obj.fit()
# print(obj.predict(X))