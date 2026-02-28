"""
Python entrypoint scaffold generated from notebook: joe biden twitt.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: joe biden twitt.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import pandas as pd
# import numpy as np
#
# Cell 2
# df=pd.read_csv('JoeBidenTweets.csv')
# df.head()
#
# Cell 3
# import nltk
# import re
# import string
# from string import punctuation
# from nltk.corpus import stopwords
# def remove_punc(text):
#     text=text.lower()
#     text=re.sub('\[.*?\]','',text)
#     text=re.sub('https?://\S+|www\.\S+', '', text)
#     text=re.sub('[%s]' %re.escape(string.punctuation),'',text)
#     text = re.sub('\n', '', text)
#     text = re.sub('\w*\d\w*', '', text)
#     return text
#
# Cell 4
# remove_punc('csjck sdjdwld/sakcsmclskk.ijk&')
#
# Cell 5
# def punctuationn_stopwords(gtext):
#     removed=[ch for ch in gtext if ch not in punctuation]
#     joining="".join(removed).split()
#     final=[ch.lower() for ch in joining if ch not in stopwords.words('english')]
#     return final
#
# Cell 6
# df['tweet']=df['tweet'].apply(lambda x:remove_punc(x))
# #df['tweet']=df['tweet'].apply(lambda x:punctuationn_stopwords(x))
#
# Cell 7
# df.drop(['url','id'],axis=1,inplce=True)
#
# Cell 8
# import matplotlib.pyplot as plt
# from collections import Counter
# def common_terms(df):
#     word_list=[]
#     for i,j in df.iterrows():
#         for word in j['tweet']:
#             word_list.append(word)
#     count=Counter(word_list)
#     most_common=pd.DataFrame(count.most_common(9),columns=['word','count'])
#
#     return most_common
#
# Cell 9
# common_terms(df)
#
# Cell 10
# df['tweet']
#
# Cell 11
# for i,j in df.iterrows():
#     for  word in j['tweet']:
#         print(word)
#
# Cell 12
#
#
