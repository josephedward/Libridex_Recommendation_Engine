from flask import Flask, render_template, redirect, request, jsonify
import pandas as pd
import urllib
import os
from bs4 import BeautifulSoup
import time 
from splinter import Browser
# from textblob import TextBlob
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
nltk.download('stopwords')

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
from book_scripts import initialize_book_data, get_recommendations
# import jsonify

app = Flask(__name__)


@app.route("/test_csv/",methods=['GET'])
def test_csv():
    test_csv_path="./resources/book_obj_list_v1.csv"
    test_df=pd.read_csv(test_csv_path)
    return test_df.to_csv(index=True)


test_df= initialize_book_data.initialize()

@app.route("/recommend/<book>/")
def get_recommendation(book):
    print('app.py -> book: ', book)
    recommended = get_recommendations.get_rec(test_df,book)
    print('app.py -> recommended: ', recommended)
    return jsonify({"data": recommended})




if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

