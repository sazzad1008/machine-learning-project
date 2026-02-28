"""
Python entrypoint scaffold generated from notebook: Income prediction.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: Income prediction.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# from sklearn.cluster import KMeans
# from sklearn.cluster import KMeans
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from matplotlib import pyplot as plt
# %matplotlib inline
#
# Cell 2
# df=pd.read_csv('income.csv')
# df.head()
#
# Cell 3
# plt.scatter(df.Age,df['Income($)'])
#
# Cell 4
# km=KMeans(n_clusters=5)
# y_predict=km.fit_predict(df[['Age','Income($)']])
# y_predict
#
# Cell 5
# from sklearn.preprocessing import MinMaxScaler
#
# Cell 6
# scalar=MinMaxScaler()
# scalar.fit(df[['Income($)']])
# df['Income($)']=scalar.transform(df[['Income($)']])
# df
# df.drop('cluster',axis='columns')
#
# Cell 7
# scalar.fit(df[['Age']])
# df['Age']=scalar.transform(df[['Age']])
# df
#
# Cell 8
# y_predict=km.fit_predict(df[['Age','Income($)']])
# y_predict
#
# Cell 9
# df['cluster']=y_predict
# df.head()
#
# Cell 10
# df5=df[df.cluster==2]
# df6=df[df.cluster==3]
# df7=df[df.cluster==1]
# plt.scatter(df5.Age,df1['Income($)'],color='green')
# plt.scatter(df6.Age,df2['Income($)'],color='red')
# plt.scatter(df7.Age,df3['Income($)'],color='black')
#
# Cell 11
#
#
