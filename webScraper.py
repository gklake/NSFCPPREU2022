import codecs
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

htmlDoc = codecs.open(r"downloadedHTMLPages/CryptBB - Beginner Hacking.htm")
# html = urlopen('')

soup = BeautifulSoup(htmlDoc, 'html.parser')
# print(soup.prettify())

url = input("Enter the URL: ")

pageText = soup.text
cleanPageText = []
review = re.sub('[^a-zA-z]', ' ', pageText)
review = review.lower()
review = review.split()
review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopWords)]
review = ' '.join(review)
cleanPageText.append(review)

unique_words = set(cleanPageText)
print(unique_words)


# TODO: Find more HTML pages
# TODO: Loop through all HTML pages and clean text
# TODO: Pass the list of clean text to the TF-IDF Vectorizer using either fit_transform() or fit()
# tfIdf = TfidfVectorizer()
#
# # applying tf idf to training data
# xTrainTf = tfIdf.fit_transform(trainX)
