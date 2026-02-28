"""
Python entrypoint scaffold generated from notebook: movie recommendation.ipynb
"""

def main() -> None:
    """Run this project entrypoint."""
    print("Run notebook logic from: movie recommendation.ipynb")


if __name__ == "__main__":
    main()

# Notebook code reference:
# Cell 1
#
#
# Cell 2
# !mkdir -/.kaggle
#
# Cell 3
# import pandas as pd
# import numpy as np
# import difflib
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
#
# Cell 4
# df=pd.read_csv('movies.csv')
# sampled=['genres','keywords','tagline','cast','director']
# df.head()
#
# Cell 5
# for feature in sampled:
#     df[feature]=df[feature].fillna(' ')
#
# Cell 6
# combined=df['genres']+''+df['keywords']+''+df['tagline']+''+df['cast']+''+df['director']
# combined
#
# Cell 7
# vectorizer=TfidfVectorizer()
# feature_vect=vectorizer.fit_transform(combined)
#
# Cell 8
# similarity=cosine_similarity(feature_vect)
# list_data=df['title'].tolist()
# similarityilarity
#
# Cell 9
# movie_name=input('give name')
#
# Cell 10
# find_close=difflib.get_close_matches(movie_name,list_data)
# find_close
#
# Cell 11
# close=find_close[0]
#
# Cell 12
# index=df[df.title==close]['index'].values[0]
# index
#
# Cell 13
# similarity_score=list(enumerate(similarity[index]))
# similarity_score
#
# Cell 14
# sorted_similafrf=sorted(similarity_score,key=lambda x:x[1],reverse=True)
# sorted_similafrf
#
# Cell 15
# i=1
# for movie in sorted_similafrf:
#     index=movie[0]
#     titlenow=df[df.index==index]['title'].values[0]
#     if (i<9):
#         print(i,'-',titlenow)
#         i=i+1
#
# Cell 16
#
#
