import pandas as pd
from bs4 import BeautifulSoup
import time 
from splinter import Browser
# from textblob import TextBlob
import nltk
nltk.download('averaged_perceptron_tagger')
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import re
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import random
from tqdm import tqdm
from gensim.models import Word2Vec 
import matplotlib.pyplot as plt
# %matplotlib inline
import warnings;
warnings.filterwarnings('ignore')


def get_rec(data_df,book):
    language="English"
    print("Test DataFrame Columns: ", data_df.columns)
    test_book_df=data_df

    title=book
    print("Title: ", book)
    # Matching the language with the dataset and reset the index
    try:
        data = test_book_df.loc[test_book_df['language'] == language]  
        data.reset_index(level = 0, inplace = True) 
        # Convert the index into series
        indices = pd.Series(data.index, index = data['title'])
        # print(indices)
        #Converting the book title into vectors and used bigram
        tf = TfidfVectorizer(analyzer='word', ngram_range=(2, 2), min_df = 1, stop_words='english')
        tfidf_matrix = tf.fit_transform(data['cleaned_desc'])
        # print(tfidf_matrix)
        # Calculating the similarity measures based on Cosine Similarity
        sg = cosine_similarity(tfidf_matrix, tfidf_matrix)
        # print(indices)    
        # Get the index corresponding to original_title       
        idx = indices[title]
        # Get the pairwsie similarity scores 
        sig = list(enumerate(sg[idx]))
        # print(sig)
        # Sort the books
        sig = sorted(sig, key=lambda x: x[1], reverse=True)
        # Scores of the 5 most similar books 
        sig = sig[1:6]
        # Book indicies
        movie_indices = [i[0] for i in sig]
        #   Top 5 book recommendation
        rec = data[['title']].iloc[movie_indices]   
        print(rec)
        # It reads the top 5 recommend book url and print the images
        # rec_whole_df= pd.DataFrame()
        rec_whole_df = data_df[data_df['title'].isin(rec['title'])]
        print(rec_whole_df)
        return rec_whole_df.to_json(orient="records")
    except:
        print("exception in running analysis for: ", book)
        # print("Recommendations: ")
        # for i in rec['title']:
        #     print(data_df[data_df['title']==i])

        # rec_whole_df[i]=data_df[data_df['title']==i]
    #         response = requests.get(i)
    #         img = Image.open(BytesIO(response.content))
    #         plt.figure()
    #         print(plt.imshow(img))
    # return rec