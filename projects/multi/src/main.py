"""
Python entrypoint scaffold generated from notebook: multi.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: multi.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import pandas as pd
# import numpy as np
# from sklearn import linear_model
# from word2number import w2n
#
# Cell 2
# pip install word2number
#
# Cell 3
# df=pd.read_csv('hirings.csv')
# df
#
# Cell 4
# df.experience=df.experience.fillna('zero')
# df
#
# Cell 5
# df.experience
#
# Cell 6
# import math
# median=math.floor(df['test_score(out of 10)'].mean())
#
# Cell 7
# df['test_score(out of 10)']=df['test_score(out of 10)'].fillna(median)
# df
#
# Cell 8
# df.experience=df.experience.apply(w2n.word_to_num)
# df
#
# Cell 9
# reg=
#
