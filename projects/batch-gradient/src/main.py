"""
Python entrypoint scaffold generated from notebook: batch gradient.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: batch gradient.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt
# %matplotlib inline
# import random
#
# Cell 2
# df=pd.read_csv('homeprices_banglore.csv')
# df
#
# Cell 3
# from sklearn import preprocessing
# sx=preprocessing.MinMaxScaler()
# sy=preprocessing.MinMaxScaler()
#
# Cell 4
# xscale=sx.fit_transform(df.drop('price',axis='columns'))
# yscale=sy.fit_transform(df.price.values.reshape(df.shape[0],1))
#
# Cell 5
# xscale
#
# Cell 6
# def batchgradient(x,ytrue,epoch,r):
#     w=np.ones(shape=x.shape[1])
#     b=0
#     total_sample=x.shape[0]
#     costlist=[]
#     epochlist=[]
#     for i in range(epoch):
#         ramdom_index=random.randint(0,total_sample-1)
#         samplex=x[ramdom_index]
#         sampley=ytrue[ramdom_index]
#         ypredict=np.dot(w,samplex.T)+b
#         w_grad = -(2/total_sample)*(samplex.T.dot(sampley-ypredict))
#         b_grad = -(2/total_sample)*np.sum(sampley-ypredict)
#
#         w = w - r* w_grad
#         b = b - r* b_grad
#
#         cost= np.mean(np.square(sampley-ypredict))
#
#         if i%50==0:
#             costlist.append(cost)
#             epochlist.append(i)
#
#     return w,b,costlist,epochlist
#
#
# Cell 7
# w,b,costlist,epochlist=batchgradient(xscale,yscale.reshape(yscale.shape[0],),1100,0.1)
# w,b,costlist,epochlist
#
# Cell 8
# plt.plot(epochlist,costlist)
#
# Cell 9
#
#
