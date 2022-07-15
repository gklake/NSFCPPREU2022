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
'''
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
'''

with open('tfIdf_vectorizer.pickle', 'rb') as file:
	tfIdf = pickle.load(file)

sentence = "usually yes, also there is waf bypass tools on hackbar. In general, you can hack unsafe sites but also you " + \
					 "can find a vulnerability in 'government' sites or bet sites. Anyway I will open new topics for advanced level"
testInput = tfIdf.transform([sentence])
print(testInput)

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
