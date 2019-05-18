# univariate linear regression
import numpy as np
from sklearn import linear_model
x=[20,14,5,7,9]
y=[3,7,8,0,1]
x=np.array(x).reshape(-1,1)
y=np.array(y).reshape(-1,1)

reg=linear_model.LinearRegression()
reg.fit(x,y)


"""
to predict
"""
x1=[100,200,300]
x1=np.array(x1).reshape(-1,1)
reg.predict(x1)



