import codecs
import glob
import os.path
import pickle

import nltk
from bs4 import BeautifulSoup
import re
from nltk import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# stop word removal and lemmatization
stopWords = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()
corpus = []

for filepath in glob.glob(os.path.join(os.getcwd() + r"\downloadedHTMLPages", '*.htm')):
	print(filepath)
	htmlDoc = codecs.open(filepath, encoding='utf-8')

	soup = BeautifulSoup(htmlDoc, 'html.parser')

	# url = input("Enter the URL: ")

	pageText = soup.text

	review = re.sub('[^a-zA-z]', ' ', pageText)
	review = review.lower()
	review = review.split()
	review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopWords)]
	review = ' '.join(review)
	corpus.append(review)

# TODO: Pass the list of clean text to the TF-IDF Vectorizer using either fit_transform() or fit()
tfIdf = TfidfVectorizer()
tfIdf.fit(corpus)

with open('tfIdf_vectorizer.pickle', 'wb') as file:
	pickle.dump(tfIdf, file)


# TODO: Append a y- or n- to the front or end of each .htm file name to distinguish if its related to criminal hacking
# TODO: Use the y-/n- to create the label vector(y)
# TODO: Use method from this link: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
