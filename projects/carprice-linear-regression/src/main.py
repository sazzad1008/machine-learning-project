"""
Python entrypoint scaffold generated from notebook: carprice linear regression.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: carprice linear regression.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import pandas as pd
# import matplotlib as plt
# %matplotlib inline
#
# Cell 2
# df=pd.read_csv('carprices.csv')
# df
#
# Cell 3
# x=df[['Mileage','Age(yrs)']]
# x
#
# Cell 4
# y=df['Sell Price($)']
#
# Cell 5
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.3)
#
#
# Cell 6
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
#
# Cell 7
# from sklearn.linear_model import LinearRegression
# clf = LinearRegression()
# clf.fit(x_train, y_train)
#
# Cell 8
# clf.predict(x_test)
#
# Cell 9
#
#
