"""
Python entrypoint scaffold generated from notebook: creditcard fraud uing deep .ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: creditcard fraud uing deep .ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import pandas as pd
# import numpy as np
# import sklearn as sk
# from sklearn.preprocessing import scale
# from sklearn.model_selection import train_test_split
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
# from sklearn.cluster import KMeans
#
# Cell 2
# df=pd.read_csv('creditcard.csv')
# df.head(7)
#
# Cell 3
# x=df.iloc[:,:-1]
# y=df['Class']
# x_scaled=scale(x)
# pca=PCA(n_components=2)
# x_reduced=pca.fit_transform(x_scaled)
# x_train,x_test,y_train,y_test=train_test_split(x_reduced,y,test_size=0.33,random_state=500)
#
# Cell 4
# kmeans=KMeans(n_clusters=2,n_init=10)
# kmeans.fit(x_train)
#
# Cell 5
# ypredicted=kmeans.fit_predict(x_reduced,y)
# ypredicted
#
# Cell 6
# df['cluster']=ypredicted
# df
#
# Cell 7
# plt.plot(x_reduced[:, 0], x_reduced[:, 1], 'k.', markersize=2)
# center=kmeans.cluster_centers_
# plt.scatter(center[:,0],center[:,1],marker='*',color='w',s=169, linewidths=3)
#
# Cell 8
# plt.plot(df.iloc[:,:],'k.' )
#
# Cell 9
# df.iloc[:,8]
#
# Cell 10
# predictions=kmeans.predict(x_test)
# predictions
#
# Cell 11
#
# frauds=df.loc[df['Class']==1]
# frauds.plot.scatter(x='Amount',y='Class')
# non_frauds=df.loc[df['Class']==0]
# non_frauds.plot.scatter(x='Amount',y='Class')
# plt.show()
#
# Cell 12
# from sklearn import linear_model
#
# Cell 13
# reg=linear_model.LogisticRegression()
# reg.fit(x_train,y_train)
#
# Cell 14
# ypredict=np.array(reg.predict(x_test))
# ypredict
#
# Cell 15
# yright=np.array(y_test)
#
# Cell 16
# len(x_train)
#
# Cell 17
# y_train.value_counts()
#
# Cell 18
# pip install imbalanced-learn
#
# Cell 19
# pip install imbalanced-learn
#
# Cell 20
# from imblearn.over_sampling import SMOTE
#
# Cell 21
# smote=SMOTE(sampling_strategy='minority')
# x_sm,y_sm=smote.fit_resample(x,y)
# y_sm.value_counts()
#
# Cell 22
# x_train,x_test,y_train,y_test=train_test_split(x_sm,y_sm,test_size=0.33,random_state=500)
#
# Cell 23
# log
#
