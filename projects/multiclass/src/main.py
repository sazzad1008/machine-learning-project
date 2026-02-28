"""
Python entrypoint scaffold generated from notebook: multiclass.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: multiclass.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import pandas as pd
#
# Cell 2
# from sklearn.datasets import load_digits
# %matplotlib inline
# import matplotlib.pyplot as plt
#
# Cell 3
# digits=load_digits()
# digits
#
# Cell 4
# for i in range(5):
#  plt.matshow(digits.images[i])
#
# Cell 5
# from sklearn.linear_model import LogisticRegression
# model=LogisticRegression()
#
# Cell 6
# from sklearn.model_selection import train_test_split
# xtrain,xtest,ytrain,ytest=train_test_split(digits.data,digits.target,test_size=0.5)
#
# Cell 7
# model.fit(xtrain,ytrain)
#
# Cell 8
# model.predict(xtest)
#
# Cell 9
# model.predict(digits.data[0:5])
#
# Cell 10
#
#
