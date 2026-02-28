"""
Python entrypoint scaffold generated from notebook: gradient descent.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: gradient descent.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import pandas as pd
# import matplotlib as plt
# import numpy as np
# import math
# from sklearn import linear_model
#
# Cell 2
# %matplotlib inline
# def gradient(x,y):
#     mc = bc = 0
#     rate = 0.00002
#     costprev=0
#     for i in range(1000):
#      yp=mc*x+bc
#      n=len(x)
#      cost=(1/n)*sum([val**2 for val in (y-yp)])
#      md=-(2/n)*sum([x*(y-yp)])
#      bp=-(2/n)*sum([y-yp])
#      mc=mc-rate*md
#      bp=bp-rate*bp
#      if math.isclose(cost,costprev,rel_tol=1e-20):
#         break
#      costprev=cost
#      print('mc{},bc{},cost{},i{}'.format(mc,bp,cost,i))
#
#
# Cell 3
# x = np.array([1,2,3,4,5])
# y = np.array([5,7,9,11,13])
#
# Cell 4
# gradient(x,y)
#
# Cell 5
# df=pd.read_csv('test_scores.csv')
# df
# p=np.array(df.math)
# p
# q=np.array(df.cs)
# q
# df
#
# Cell 6
# gradient(p,q)
#
# Cell 7
#
#     reg=linear_model.LinearRegression()
#     reg.fit(df[[math]],df.cs)
#
#
# Cell 8
#
#
# Cell 9
#
#
