"""
Python entrypoint scaffold generated from notebook: human resource analysis.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: human resource analysis.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import pandas as pd
# from matplotlib import pyplot as plt
# %matplotlib inline
#
# Cell 2
# df = pd.read_csv("HR_comma_sep.csv")
# df.head()
#
# Cell 3
# left=df[df.left==1]
# left.shape
#
# Cell 4
# retained=df[df.left==0]
# retained.shape
#
# Cell 5
# pd.crosstab(df.salary,df.left).plot(kind='bar')
#
# Cell 6
# plt.barh(df.average_montly_hours,df.left)
#
# Cell 7
# df.groupby('left').mean()
#
# Cell 8
# subdf=df[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]
# subdf
#
# Cell 9
# dummies=pd.get_dummies(df.salary)
# dummies
#
# Cell 10
# dfdum=pd.concat([subdf,dummies],axis='columns')
# dfdum
#
# Cell 11
# dfdum.drop('salary',axis='columns')
#
# Cell 12
# from sklearn.model_selection import train_test_split
# xtrain,xtest,ytrain,ytest=train_test_split(dfdum,df.left,train_size=0.3)
#
# Cell 13
# from sklearn.linear_model import LogisticRegression
# model=LogisticRegression()
#
# Cell 14
# model.fit(xtrain,ytrain)
#
# Cell 15
#
#
