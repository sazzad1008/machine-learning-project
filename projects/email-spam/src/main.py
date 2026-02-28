"""
Python entrypoint scaffold generated from notebook: email spam.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: email spam.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import numpy as np
# import pandas as pd
#
# Cell 2
# df=pd.read_csv('Spam5.csv',engine='python',encoding='ISO-8859-1')
# df
#
# Cell 3
# df.drop(columns=['Unnamed: 2','Unnamed: 3','Unnamed: 4'],inplace=True)
#
# Cell 4
# df.rename(columns={'v1':'Class','v2':'Text'},inplace=True)
#
# Cell 5
# from sklearn.preprocessing import LabelEncoder
# encode=LabelEncoder()
#
# Cell 6
# df['Class']=encode.fit_transform(df.Class)
#
# Cell 7
# df.head()
#
# Cell 8
# df=df.drop_duplicates(keep='first')
# df.head()
#
# Cell 9
# import nltk
#
# Cell 10
# nltk.download('punkt')
#
# Cell 11
# df['num_character']=df['Text'].apply(len)
#
# Cell 12
# df['num_word']=df['Text'].apply(lambda x:len(nltk.word_tokenize(x)))
#
# Cell 13
# df['sentence']=df['Text'].apply(lambda x:len(nltk.sent_tokenize(x)))
#
# Cell 14
# df.sample()
#
# Cell 15
# import seaborn as sns
#
# Cell 16
# sns.pairplot(df,hue='Class')
#
# Cell 17
# sns.heatmap(df.corr(),annot=True)
#
# Cell 18
# from nltk.stem.porter import PorterStemmer
# p=PorterStemmer()
# from nltk.corpus import stopwords
# import string
#
# Cell 19
# def Processing(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)
#
#
#     t= []
#     for i in text:
#         if i.isalnum():
#             t.append(i)
#
#     text = t[:]
#     t.clear()
#
#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             t.append(i)
#
#     text = t[:]
#     t.clear()
#
#     for i in text:
#         t.append(p.stem(i))
#
#
#     return " ".join(t)
#
# Cell 20
# df['new_text']=df.Text.apply(Processing)
#
# Cell 21
# from wordcloud import WordCloud
# wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
#
# Cell 22
# !pip install wordcloud
#
# Cell 23
# spams=wc.generate(df[df.Class==1]['new_text'].str.cat(sep=" "))
#
# Cell 24
# plt.figure(figsize=(15,6))
# plt.imshow(spams)
#
# Cell 25
# import matplotlib.pyplot as plt
#
# Cell 26
# spams=[]
# for token in df[df.Class==1]['new_text'].tolist():
#         for word in token.split():
#             spams.append(word)
#
# Cell 27
#
#
# Cell 28
# from collections import Counter
#
# Cell 29
# import seaborn as sns
# sns.barplot(pd.DataFrame(Counter(spams).most_common(30))[0],pd.DataFrame(Counter(spams).most_common(30))[1])
# plt.show()
# plt.xticks(rotation='vertical')
#
# Cell 30
# from sklearn.feature_extraction.text import TfidfVectorizer
#
# Cell 31
# tf=TfidfVectorizer(max_features=3000)
#
# Cell 32
# x=tf.fit_transform(df.new_text).toarray()
#
# Cell 33
# x.shape
# y=df.Class.values
# y
#
# Cell 34
# from sklearn.model_selection import train_test_split
# xtrain,xtest,ytrain,ytest=train_test_split(x,y,train_size=0.8)
#
# Cell 35
# from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
# from sklearn.metrics import precision_score,confusion_matrix,accuracy_score
#
# Cell 36
# MB=MultinomialNB()
#
# Cell 37
# MB.fit(xtrain,ytrain)
# ypred = MB.predict(xtest)
# print(accuracy_score(ytest,ypred))
# print(confusion_matrix(ytest,ypred))
# print(precision_score(ytest,ypred))
#
# Cell 38
# import pickle
# pickle.dump(tf,open('vector.pkl','wb'))
# pickle.dump(MB,open('model.pkl','wb'))
#
# Cell 39
# import streamlit as st
# import pickle
# import string
# from nltk.corpus import stopwords
# import nltk
# from nltk.stem.porter import PorterStemmer
#
# ps = PorterStemmer()
#
#
# def transform_text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)
#
#     y = []
#     for i in text:
#         if i.isalnum():
#             y.append(i)
#
#     text = y[:]
#     y.clear()
#
#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)
#
#     text = y[:]
#     y.clear()
#
#     for i in text:
#         y.append(ps.stem(i))
#
#     return " ".join(y)
#
# tfidf = pickle.load(open('vector.pkl','rb'))
# model = pickle.load(open('model.pkl','rb'))
#
# st.title("Email/SMS Spam Classifier")
#
# input_sms = st.text_area("Enter the message")
#
# if st.button('Predict'):
#
#     # 1. preprocess
#     transformed_sms = transform_text(input_sms)
#     # 2. vectorize
#     vector_input = tfidf.transform([transformed_sms])
#     # 3. predict
#     result = model.predict(vector_input)[0]
#     # 4. Display
#     if result == 1:
#         st.header("Spam")
#     else:
#         st.header("Not Spam")
#
# Cell 40
# pip install streamlit
#
# Cell 41
#
#
