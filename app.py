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
# import jsonify
from book_scripts import scrape_to_pg
# initialize_book_data, get_recommendations, get_static_rec,
 

app = Flask(__name__)

@app.route("/", methods=['GET'])
def default():
    scrape_to_pg
    return ("<h1>Default Route Works</h1>")







if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
    app.config['TEMPLATES_AUTO_RELOAD'] = True

