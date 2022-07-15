import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn import metrics
import nltk
import re
from nltk.stem import WordNetLemmatizer
import pickle

# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

stopWords = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()

with open('tfIdf_vectorizer.pickle', 'rb') as file:
	tfIdfVectorizedData = pickle.load(file)
