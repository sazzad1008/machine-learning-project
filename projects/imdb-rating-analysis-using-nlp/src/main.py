"""
Python entrypoint scaffold generated from notebook: imdb rating analysis using nlp.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: imdb rating analysis using nlp.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import numpy as np
# import pandas as pd
#
# Cell 2
# df = pd.read_csv('IMDB Dataset.csv')
# df.head()
#
# Cell 3
# df['review']=df['review'].str.lower()
#
# Cell 4
#
# import re
# def removal_html(text):
#     pattern=re.compile('<.*?>')
#     return pattern.sub(r'',text)
#
#
# Cell 5
# df['review']=df['review'].apply(lambda x:removal_html(x))
#
# Cell 6
# def remove_url(text):
#     pattern = re.compile(r'https?://\S+|www\.\S+')
#     return pattern.sub(r'', text)
#
# Cell 7
# df['review']=df['review'].apply(lambda x:remove_url(x))
#
# Cell 8
# import string,time
# string.punctuation
#
# Cell 9
# exclude=string.punctuation
#
# Cell 10
# def remove_punctuation(text):
#     for char in exclude:
#         text=text.replace(char,'')
#         return text
#
# Cell 11
# df['review']=df['review'].apply(lambda x:remove_punctuation(x))
#
# Cell 12
# def chat_conversion(text):
#     new_text = []
#     for w in text.split():
#         if w.upper() in chat_words:
#             new_text.append(chat_words[w.upper()])
#         else:
#             new_text.append(w)
#     return " ".join(new_text)
#
# Cell 13
# chat_conversion('IMHO he is the best')
#
# Cell 14
# string.chat_words
#
# Cell 15
# from textblob import TextBlob
#
# Cell 16
# incorrect_text = 'ceertain conditionas duriing seveal ggenerations aree moodified in the saame maner.'
# text=TextBlob(incorrect_text)
#
# Cell 17
# text.correct().string
#
# Cell 18
# from nltk.corpus import stopwords
#
# Cell 19
# def remove_stopwords(text):
#     new_text = []
#
#     for word in text.split():
#         if word in stopwords.words('english'):
#             new_text.append('')
#         else:
#             new_text.append(word)
#     return ' '.join(new_text)
#
# Cell 20
# remove_stopwords('probably my all-time favorite movie, a story of selflessness, sacrifice and dedication to a noble cause, but it\'s not preachy or boring. it just never gets old, despite my having seen it some 15 or more times')
#
# Cell 21
# import re
# def remove_emoji(text):
#     emoji_pattern = re.compile("["
#                            u"\U0001F600-\U0001F64F"  # emoticons
#                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
#                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                            u"\U00002702-\U000027B0"
#                            u"\U000024C2-\U0001F251"
#                            "]+", flags=re.UNICODE)
#     return emoji_pattern.sub(r'', text)
#
# Cell 22
# remove_emoji("Loved the movie. It was 😘😘")
#
# Cell 23
# import re
# text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry?
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book."""
# token=re.compile("[.!?]").split(text)
#
# Cell 24
# token
#
# Cell 25
# from nltk.tokenize import word_tokenize,sent_tokenize
#
# Cell 26
# sent_tokenize(text)
#
# Cell 27
# nltk.download('punkt')
#
# Cell 28
# import nltk
#
# Cell 29
# word_tokenize(text)
#
# Cell 30
# import spacy
#
# Cell 31
# from nltk.stem.porter import PorterStemmer
#
# Cell 32
# ps=PorterStemmer()
# def stemming(text):
#     return ' '.join([ps.stem(word) for word in text.split()])
#
# Cell 33
# stemming(text)
#
# Cell 34
# sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."
# punctuations="?:!.,;"
# token=nltk.word_tokenize(sentence)
# for word in token:
#     if word in punctuations:
#         token.remove(word)
# ' '.join(word for word in token)
#
# Cell 35
# x=df.iloc[:,0:1]
# y=df['sentiment']
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=1)
#
# Cell 36
# from sklearn.feature_extraction.text import CountVectorizer\]'[p;li8htrwqaserdtfgyhujnkolp;         ]'
#
# Cell 37
# cv=CountVectorizer()
# x_train_bow=cv.fit_transform(x_train['review'])
#
# Cell 38
#
#
