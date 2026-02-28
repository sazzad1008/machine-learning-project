"""
Python entrypoint scaffold generated from notebook: insurance price using gradient.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: insurance price using gradient.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import numpy as np
# import tensorflow as tf
# from tensorflow import keras
# import pandas as pd
# from matplotlib import pyplot as plt
# %matplotlib inline
#
# Cell 2
# df = pd.read_csv("insurance66.csv")
# df.head()
#
# Cell 3
# from sklearn.model_selection import train_test_split
# xtrain,xtest,ytrain,ytest=train_test_split(df[['age','affordibility']],df.bought_insurance,test_size=0.2)
# xtrains=xtrain.copy()
# xtrains['age']=xtrains['age']/100
# ytrains=ytrain.copy()
# ytrains['age']=ytrains['age']/100
#
# Cell 4
# model=keras.Sequential([
#     keras.layers.Dense(1,input_shape=(2,),activation='sigmoid',kernel_initializer='ones',bias_initializer='zeros')
# ])
# model.compile(
#     optimizer='adam',
#     loss='binary_crossentropy',
#     metrics=['accuracy']
# )
# model.fit(xtrains,ytrains,epochs=7)
#
# Cell 5
# def sigmoid(x):
#     import math
#     return 1/(1+np.exp(-x))
#
# Cell 6
# def log_loss(ytrue,ypredict):
#     epsilon=1e-15
#     ypredictnew=[max(i,epsilon) for i in ypredict]
#     ypredictnew=[min(i,1-epsilon) for i in ypredictnew]
#     ypredictnew=np.array(ypredictnew)
#     return -np.mean(ytrue*np.log(ypredictnew)+(1-ytrue)*np.log(1-ypredictnew))
#
#
# Cell 7
# def gradient(age,affordibility,ytrue,epochs,loss_thresh):
#     w5=w6=1
#     bias=0
#     n=len(age)
#     r=0.5
#     for i in range(epochs):
#         weightsum=w5*age+w6*affordibility+bias
#         ypredict=sigmoid(weightsum)
#         loss=log_loss(ytrue,ypredict)
#
#         w5d=(1/n)*np.dot(np.transpose(age),(ypredict-ytrue))
#         w6d=(1/n)*np.dot(np.transpose(affordibility),(ypredict-ytrue))
#         biasd = np.mean(ypredict-ytrue)
#
#         w5=w5-r*w5d
#         w6=w6-r*w6d
#         bias=bias-r*biasd
#         print(f'epoch:{i},w5:{w5},w6:{w6},loss:{loss}')
#
# Cell 8
# gradient(xtrains['age'],xtrains['affordibility'],ytrain,1000,0.50)
#
# Cell 9
# xtrainss=xtrain.copy()
#
# Cell 10
# xtrains=xtrain.copy()
# xtrains['age']=xtrains['age']/100
#
# Cell 11
# xtrains
#
# Cell 12
# np.ones(5
#        )
#
# Cell 13
#
#
