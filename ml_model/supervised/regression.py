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


class LogisticRegr(OLS):
    '''file:///Users/qianleren/Google%20Drive/82.0_Computer%20Vision/assignment_1.html
    issue: not comply with statmodel and sklearn
    '''

    def __init__(self, X: 'list(list())', Y: list(), random_seed: int = None) -> None:
        '''take X without constant'''
        super().__init__(X, Y, random_seed)
        self.w = np.random.rand(X.shape[1],1)*0.01
        self.b = 0

    def fit(self, learning_rate=0.001, num_iterations=2000, print_cost=False):
        params,grads,losses = self._optimize(self.w,self.b,self.X,self.Y,num_iterations,learning_rate,print_cost)
        self.w = params['w']
        self.b = params['b']

    def predict(self, X):
        n = X.shape[0]
        Y_prediction = np.zeros((n,1))
        A = self._sigmoid(np.dot(X, self.w)+self.b)
        for i in range(n):
            if A[i, 0]>0.5:
                Y_prediction[i,0] = 1
            else:
                Y_prediction[i,0] = 0
        return Y_prediction

    def pseudoR2(self):
        '''McFadden R2'''
        return

    def _sigmoid(self, z):
        return 1/(1+ np.exp(-z))

    def _logistic_loss(self, A, Y):
        m = A.shape[0]
        return (-1/m) * np.sum(Y*np.log(A)+ (1-Y)*np.log(1-A))

    def _propagate(self, w, b, X, Y):
        # w:(d,1), b(1), X(n,d), Y(n,1), A(n,1)
        n = X.shape[0]
        # forward, loss function derived from MLE, refer: https://blog.csdn.net/mengjizhiyou/article/details/103117274
        A = self._sigmoid(np.dot(X, w)+b)
        loss = self._logistic_loss(A,Y)

        # backprop：dZ(n,1), dw(d,1), db(1)
        dZ = (A - Y)
        dw = (np.dot(X.T,dZ))/n
        db = (np.sum(dZ))/n

        grads = {"dw": dw,"db": db}
        return grads, loss
    
    def _optimize(self, w, b, X, Y, num_iterations, learning_rate, print_cost = False):
        losses = []
        for i in range(num_iterations):
            grads, loss = self._propagate(w,b,X,Y)
            dw = grads["dw"]
            db = grads["db"]
            # update params：
            w = w - learning_rate*dw
            b = b - learning_rate*db

            # view loss every 100 iters
            if i % 100 == 0:
                losses.append(loss)
            if print_cost and i % 100 == 0:
                print ("loss after iteration %i: %f" %(i, loss))
        
        # put in history
        params = {"w": w, "b": b}
        grads = {"dw": dw, "db": db}
        return params, grads, losses

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

# # compare with statmodel
# X1 = sm.add_constant(X0)
# mod = sm.OLS(Y, X1)
# res = mod.fit()
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

# # test Logistic regression
# from sklearn.datasets import load_boston
# data = load_boston()
# X_lr = data.data[:, [0,5,6,12]]
# Y_lr = data.data[:, [3]]
# obj = LogisticRegr(X_lr, Y_lr)
# obj.fit(learning_rate=0.001, num_iterations=2000, print_cost=True)
# print(obj.w, obj.b)
# # print(obj.predict(X_lr))
# # print(len([i[0] for i in obj.predict(X_lr) if i[0] == 0.]))

# # compare Logistic regression with statmodel, and sklearn
# X_lr1 = sm.add_constant(X_lr)
# log_reg = sm.Logit(Y_lr, X_lr1).fit()
# print(log_reg.summary())
# # print(log_reg.predict())
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(random_state=0, penalty='none',C=1e9, solver='lbfgs').fit(X_lr, Y_lr)
# print(model.coef_)