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

# TODO: create two separate directories, one for positive HTML files and one for negative HTML files
# TODO: Use a for loop to loop through the HTML files and extract & clean text from them
# TODO: append the text to the X list and append a 1/0 to the Y list
# TODO: tfIdf = Transformer()
# TODO: tfIdf.fit(X)
# TODO: dump tfIdf to a pickle file
# TODO: xTrain, xTest, yTrain, yTest = sklearn.split(x, y)
# TODO: tfIdg.transform(xTrain)
# TODO: tfIdg.transform(xTest)
# TODO: train classifier(s)
# TODO: test classifier(s)
# TODO: dump best working classifier to pickle file