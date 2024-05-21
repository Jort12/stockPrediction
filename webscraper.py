import bs4 as bs
import urllib.request
import nltk
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')