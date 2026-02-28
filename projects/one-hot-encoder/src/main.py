"""
Python entrypoint scaffold generated from notebook: one hot encoder.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: one hot encoder.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import pandas as pd
# import numpy as np
#
# Cell 2
# df=pd.read_csv('homepricesn.csv')
# df
#
# Cell 3
# dum=pd.get_dummies(df.town)
# dum
#
# Cell 4
# merge=pd.concat([df,dum],axis='columns')
# merge
#
# Cell 5
# dfe=merge.drop(['town','west windsor'],axis='columns')
# dfe
#
# Cell 6
# x=dfe.drop(['price'],axis='columns')
# x.values
#
# Cell 7
# y=dfe.price
# y.values
#
# Cell 8
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
#
# Cell 9
# model.fit(x,y)
#
# Cell 10
# model.predict(x)
#
# Cell 11
# from sklearn.preprocessing import LabelEncoder
# le=LabelEncoder()
#
# Cell 12
# dfe=df
# dfe.town=le.fit_transform(dfe.town)
# dfe
#
# Cell 13
# p=dfe[['town','area']]
# p.values
#
# Cell 14
# y=dfe.price
# y
#
# Cell 15
# from sklear.preprocessing import OneHotEncoder
# ohe=
#
