"""
Python entrypoint scaffold generated from notebook: home price.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: home price.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import pandas as pd
# import numpy as np
# from matplotlib import pyplot as plt
# %matplotlib inline
# import matplotlib
#
# Cell 2
# df5=pd.read_csv('bengaluru.csv')
# df5.head(5)
#
# Cell 3
# df5=df5.drop(['area_type','availability','society'],axis='columns')
# df5.head(5)
#
# Cell 4
# df5['size'].unique()
#
# Cell 5
# def is_float(x):
#     try:
#         float(x)
#     except:
#          return False
#     return True
#
# Cell 6
# df5[~df5['total_sqft'].apply(is_float)]
#
# Cell 7
#
#
#
# Cell 8
# df5['total_sqft']=df5['total_sqft'].apply(convert_to)
#
# Cell 9
# convert_to(2830 - 2882)
#
# Cell 10
# df5['bath'].fillna(df5.bath.mean())
#
# Cell 11
# df5['size'].astype('str').str
#
# Cell 12
# def convert_sqft_to_num(x):
#     tokens = x.split('-')
#     if len(tokens) == 2:
#         return (float(tokens[0])+float(tokens[1]))/2
#     try:
#         return float(x)
#     except:
#         return None
#
#
# Cell 13
# df6=df5.copy()
# df6['total_sqft']=df6['total_sqft'].apply(convert_sqft_to_num).astype(float)
#
# Cell 14
# df6
#
# Cell 15
# df6['size'].apply(lambda x: str(x))
#
# Cell 16
# df6['size'].apply(lambda x: x.split())
#
# Cell 17
# df6['bhk']=df6['size'].replace('[^\d.]','',regex=True)
# df6
#
# Cell 18
#
#
# Cell 19
# df7 = df6.copy()
# df7['price_per_sqft'] = df7['price']*100000/df7['total_sqft']
# df7.head()
#
# Cell 20
# df7.size
#
# Cell 21
# df7.location.str.strip('')
#
# Cell 22
# df7['bhk']=df7['size'].replace('[^\d.]','',regex=True)
# df7
#
# Cell 23
# df7.dtypes
#
# Cell 24
# df7.size
#
# Cell 25
# df7.location.apply(lambda x: str(x))
#
# Cell 26
# df7.location.dropna()
#
# Cell 27
# df7['location']=df7['location'].apply(lambda x: str(x))
#
# Cell 28
# df7['location'].apply(lambda x: x.strip())
#
# Cell 29
# locstat=df7.location.value_counts(ascending=False)
# locstat
#
# Cell 30
# locstat.values.sum()
#
# Cell 31
# locstat_less=locstat[locstat<10]
# locstat_less
#
# Cell 32
# locstat_more=locstat[locstat>=10]
# locstat_more
#
# Cell 33
# df7['location']=df7['location'].apply(lambda x: 'other' if  x in locstat_less else x)
# df7
#
# Cell 34
# df7['bhk']=df7['bhk'].apply(lambda x: float(x))
# df8=df7[~(df7.total_sqft/df7.bhk<300)]
# df8
#
# Cell 35
# def plot_chart(df,location):
#     bhk5=df[(df.location==location) & (df.bhk==2)]
#     bhk6=df[(df.location==location) & (df.bhk==3)]
#     matplotlib.rcParams['figure.figsize'] = (15,10)
#     plt.scatter(bhk5.total_sqft,bhk5.price,color='blue',s=50)
#     plt.scatter(bhk6.total_sqft,bhk6.price,color='green',marker='+',s=50)
#
# plot_chart(df8,"Hebbal")
#
# Cell 36
# np.array([])
#
# Cell 37
# df8.shape[0]
#
# Cell 38
# def remove_bhk_outliers(df):
#     exclude_indices = np.array([])
#     for location, location_df in df.groupby('location'):
#         bhk_stats = {}
#         for bhk, bhk_df in location_df.groupby('bhk'):
#             bhk_stats[bhk] = {
#                 'mean': np.mean(bhk_df.price_per_sqft),
#                 'std': np.std(bhk_df.price_per_sqft),
#                 'count': bhk_df.shape[0]
#             }
#         for bhk, bhk_df in location_df.groupby('bhk'):
#             stats = bhk_stats.get(bhk-1)
#             if stats and stats['count']>5:
#                 exclude_indices = np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft<(stats['mean'])].index.values)
#     return df.drop(exclude_indices,axis='index')
# df9 = remove_bhk_outliers(df8)
#
# Cell 39
# df9.shape
#
# Cell 40
# plot_chart(df9,"Hebbal")
#
# Cell 41
# df99=df9[df9.bath<df9.bhk+2]
# df99
#
# Cell 42
# df10 = df99.drop(['size','price_per_sqft'],axis='columns')
# df10.head(3)
#
# Cell 43
# dummies5=pd.get_dummies(df10.location)
# dummies5
#
# Cell 44
# df77=pd.concat([df10,dummies5.drop('other',axis='columns')],axis='columns')
# df77.balcony.fillna(method='ffill',inplace=True)
#
# Cell 45
# df66=df77.drop('location',axis='columns')
# df88=df66.drop(['price'],axis='columns')
# df88.head()
#
# Cell 46
# x=df88.fillna(method='ffill')
# x.shape
#
# Cell 47
# y=df77.price
# len(y)
#
# Cell 48
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=8)
#
# Cell 49
# from sklearn.model_selection import ShuffleSplit
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import cross_val_score
# linear=LinearRegression()
# linear.fit(X_train,y_train)
# linear.score(X_test,y_test)
#
# Cell 50
# df88.fillna
#
# df77.fillna
#
# Cell 51
# x.shape
#
# Cell 52
# y.shape
#
# Cell 53
# y
#
# Cell 54
# from sklearn.model_selection import GridSearchCV
#
# from sklearn.linear_model import Lasso
# from sklearn.tree import DecisionTreeRegressor
#
# def find_best_model_using_gridsearchcv(x,y):
#     algos = {
#         'linear_regression' : {
#             'model': LinearRegression(),
#             'params': {
#                 'normalize': [True, False]
#             }
#         },
#         'lasso': {
#             'model': Lasso(),
#             'params': {
#                 'alpha': [1,2],
#                 'selection': ['random', 'cyclic']
#             }
#         },
#         'decision_tree': {
#             'model': DecisionTreeRegressor(),
#             'params': {
#                 'criterion' : ['mse','friedman_mse'],
#                 'splitter': ['best','random']
#             }
#         }
#     }
#     scores = []
#     cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
#     for algo_name, config in algos.items():
#         gs =  GridSearchCV(config['model'], config['params'], cv=cv, return_train_score=False)
#         gs.fit(X,y)
#         scores.append({
#             'model': algo_name,
#             'best_score': gs.best_score_,
#             'best_params': gs.best_params_
#
# Cell 55
#
#
# Cell 56
# dum=pd.get_dummies(df77.location)
# dum
#
# Cell 57
# df88.info()
#
# Cell 58
# np.all(np.isinfinte(df88))
#
# Cell 59
#
#
