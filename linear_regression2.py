#linear regression multivariate


import numpy as np
from sklearn import linear_model

x=[[2600,20,3,560000],[3000,15,4,565000],[3200,18,3,610000],[3600,30,3,595000],[4000,8,5,760000]]
y=[560000,565000,610000,595000,760000]
reg=linear_model.LinearRegression()
x=np.array(x)
y=np.array(y).reshape(-1,1)

reg.fit(x,y)



"""
to predict
reg.predict(x1)---> x1 to be same format as x
"



