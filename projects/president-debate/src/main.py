"""
Python entrypoint scaffold generated from notebook: president debate.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: president debate.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# import tweepy as tw
# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
#
# Cell 2
# pip install tweepy
#
# Cell 3
# consumer_key = '9qXTSgG0QqR5s5TkwEGmAEvmf'
# consumer_secret = 'EB97LIVMHlmvoPFFxavaBo9RsAuBE8O537NezZhse1CEixF5Cw'
# access_token = '1525944886696230912-hyCrmnn8BqAcjtcXdySivlPxD36MTC'
# access_token_secret = 'NPSZyBb3ZgUXrz9P9N8yg5wgemOHsWqDb9FHsD5hRkQYd'
#
#
# Cell 4
# auth = tw.OAuthHandler(consumer_key, consumer_secret)
# auth=auth.set_access_token(access_token, access_token_secret)
# # Instantiate API
# api = tw.API(auth, wait_on_rate_limit=True)
#
# Cell 5
# hashtag = "#presidentialdebate"
# querys = tw.Cursor(api.search_tweets, q=hashtag).items(1000)
# tweets = [{'Tweet':tweet.text, 'Timestamp':tweet.created_at} for tweet in querys]
# print(tweets)
#
# Cell 6
# pip install pathlib
#
# Cell 7
# pip install ruamel-yaml
#
# Cell 8
# pip install tweepy
#
# Cell 9
# df=pd.DataFrame(tweets)
# df
#
# Cell 10
# trump = ['DonaldTrump', 'Donald Trump', 'Donald', 'Trump', 'Trump\'s']
# biden = ['JoeBiden', 'Joe Biden', 'Joe', 'Biden', 'Biden\'s']
#
# Cell 11
# def flagging(tweet,refs):
#     flag=0
#     for ref in refs:
#           if tweet.find(ref) !=-1:
#             flag=1
#     return flag
#
# Cell 12
# df['trump']=df['Tweet'].apply(lambda x:flagging(x,trump))
# df['biden']=df['Tweet'].apply(lambda x:flagging(x,biden))
#
#
# Cell 13
#
#
# Cell 14
# import nltk
# from nltk.corpus import stopwords
# from textblob import Word,TextBlob
#
# Cell 15
# nltk.download('stopwords')
# nltk.download('wordnet')
# stop_words = stopwords.words('english')
# custom_stopwords = ['RT', '#PresidentialDebate']
#
# Cell 16
# pip install textblob
#
# Cell 17
# def preprocess(tweet,custom_stop):
#     pre=tweet
#     pre.replace('[^\w\s]', '')
#     pre=''.join(word  for word in pre.split() if  word not in stop_words)
#     pre=''.join(word  for word in pre.split() if  word not in custom_stop)
#     pre=''.join(Word(word)  for word in pre.split())
#     return pre
#
#
# Cell 18
# df['preTweet']=df['Tweet'].apply(lambda x: preprocess(x,custom_stopwords))
# df
#
# Cell 19
# pre=df['Tweet'][80]
# pre
#
# Cell 20
#   pre=''.join(word  for word in pre.split() if  word not in custom_stopwords)
# pre
#
# Cell 21
# dir(api)
#
# Cell 22
# pip install git+https://github.com/tweepy/tweepy.git
#
# Cell 23
# pip install tweepy[async]
#
