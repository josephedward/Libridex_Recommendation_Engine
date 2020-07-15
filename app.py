from flask import Flask, render_template, redirect
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