"""
Python entrypoint scaffold generated from notebook: setiment analysis using nlp.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: setiment analysis using nlp.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
# pip install transformers requests beautifulsoup4
#
# Cell 2
# import torch
# import numpy as np
# import pandas as pd
#
# Cell 3
# from transformers import AutoTokenizer,AutoModelForTokenClassification,AutoModelForSequenceClassification
# import re
# import requests
# from bs4 import BeautifulSoup
#
# Cell 4
# tokenizer=AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
# model=AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
#
# Cell 5
# tokens=tokenizer.encode('fuck you',return_tensors='pt')
#
# Cell 6
# tokens[0]
#
# Cell 7
# resul=model(tokens)
#
# Cell 8
# int(torch.argmax(resul.logits))
#
# Cell 9
# model(tokens)
#
# Cell 10
# print(torch.__version__)
#
# Cell 11
# r=requests.get('https://www.yelp.com/biz/social-brew-cafe-pyrmont')
# soup=BeautifulSoup(r.text,'html.parser')
# regex=re.compile('.*comment.*')
# result=soup.find_all('p',{'class':regex})
# reviews=[results.text for results in result]
#
# Cell 12
# reviews[0]
#
# Cell 13
# df=pd.DataFrame(np.array(reviews),columns=['review'])
#
# Cell 14
# df
#
# Cell 15
# def sentiment_score(review):
#     tokens=tokenizer.encode(review,return_tensors='pt')
#     result=model(tokens)
#     return int(torch.argmax(result.logits))
#
# Cell 16
# sentiment_score(df['review'].iloc[8])
#
# Cell 17
# df['sentiment']=df['review'].apply(lambda x: sentiment_score(x[:512]))
#
# Cell 18
# df
#
# Cell 19
#
#
