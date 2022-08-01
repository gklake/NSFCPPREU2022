import sklearn
import gensim
from sklearn.feature_extraction.text import CountVectorizer
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
x = []  # contains clean text
y = []  # contains the value for cleaned text(1 or 0)

# with open('tfIdf_vectorizer.pickle', 'rb') as file:
# 	tfIdfVectorizedData = pickle.load(file)

# Looping through each line of txt files and adding a label

positiveFile = open('positiveSurroundingContent.txt', 'r')
for line in positiveFile:
	review = re.sub('[^a-zA-Z]', ' ', line)
	review = review.lower()
	review = review.split()
	review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopWords)]
	review = ' '.join(review)
	# Appending the text to the x list and appending a 1(true) to the y list
	x.append(review)
	y.append(1)
positiveFile.close()

# Negative Txt:
negativeFile = open('negativeSurroundingContent.txt', 'r')
for line in negativeFile:
	review = re.sub('[^a-zA-Z]', ' ', line)
	review = review.lower()
	review = review.split()
	review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopWords)]
	review = ' '.join(review)
	# Appending the text to the x list and appending a 0(false) to the y list
	x.append(review)
	y.append(0)
negativeFile.close()

# used for verifying the text was extracted correctly
# for i in range(len(y)):
#  print("X: " + x[i])
#  print("Y: " + str(y[i]))

# Creating the word2Vec object
word2Vec = CountVectorizer()
# Fitting tfIdf to the x list
word2Vec.fit(x)
# TODO: dump tfIdf to a pickle file
# splitting the x and y lists into training and testing lists
xTrain, xTest, yTrain, yTest = sklearn.model_selection.train_test_split(x, y, test_size=0.20, random_state=42)

# transforming xTrain and xTest
xTrainTf = word2Vec.transform(xTrain)
xTestTf = word2Vec.transform(xTest)

# Training classifiers:
# Model Creation

# Naive Bayes
print("Naive Bayes: ")
naiveBayesClassifier = MultinomialNB()
naiveBayesClassifier.fit(xTrainTf, yTrain)

yPred = naiveBayesClassifier.predict(xTestTf)
print(metrics.classification_report(yTest, yPred, target_names=['Hacking Related', 'Not Hacking Related']))

print("Confusion Matrix:")
print(metrics.confusion_matrix(yTest, yPred))
print("***********************************************************************")

# Random Forest
print("Random Forest: ")
randomForestClassifier = RandomForestClassifier()
randomForestClassifier.fit(xTrainTf, yTrain)

yPred = randomForestClassifier.predict(xTestTf)
print(metrics.classification_report(yTest, yPred, target_names=['Hacking Related', 'Not Hacking Related']))

print("Confusion Matrix:")
print(metrics.confusion_matrix(yTest, yPred))
print("***********************************************************************")

# Logistic Regression
print("Logistic Regression: ")
logisticRegressionClassifier = LogisticRegression()
logisticRegressionClassifier.fit(xTrainTf, yTrain)

yPred = logisticRegressionClassifier.predict(xTestTf)
print(metrics.classification_report(yTest, yPred, target_names=['Hacking Related', 'Not Hacking Related']))

print("Confusion Matrix:")
print(metrics.confusion_matrix(yTest, yPred))
print("***********************************************************************")

# Linear SVC
print("Linear SVC: ")
linearSVCClassifier = LinearSVC()
linearSVCClassifier.fit(xTrainTf, yTrain)

yPred = linearSVCClassifier.predict(xTestTf)
print(metrics.classification_report(yTest, yPred, target_names=['Hacking Related', 'Not Hacking Related']))

print("Confusion Matrix:")
print(metrics.confusion_matrix(yTest, yPred))
print("***********************************************************************")


# Method used for testing the model with different strings
def calculatePredictionAndConfidence(text):
	textReview = re.sub('[^a-zA-Z]', ' ', text[0])
	textReview = textReview.lower()
	textReview = textReview.split()
	textReview = [lemmatizer.lemmatize(word) for word in textReview if word not in set(stopWords)]
	testProcessed = [' '.join(textReview)]
	print("testProcessed: ")
	print(testProcessed)
	testInput = word2Vec.transform(testProcessed)
	print("testInput: ")
	print(testInput)
	print("testInput.shape: ")
	print(testInput.shape)
	# Naive Bayes Classifier Predict & Confidence
	print("Naive Bayes: ")
	res = naiveBayesClassifier.predict(testInput)[0]
	prob = naiveBayesClassifier.predict_proba(testInput)[0]
	if res == 1:
		print("Hacking Related")
		# confidence
		print(prob[1])
	elif res == 0:
		print("Not Hacking Related")
		print(prob[0])
	print("***********************************************************************")
	# Random Forest Predict & Confidence
	print("Random Forest: ")
	res = randomForestClassifier.predict(testInput)[0]
	prob = randomForestClassifier.predict_proba(testInput)[0]
	if res == 1:
		print("Hacking Related")
		# confidence
		print(prob[1])
	elif res == 0:
		print("Not Hacking Related")
		print(prob[0])
	print("***********************************************************************")
	# Logistic Regression Classifier Predict & Confidence
	print("Logistic Regression: ")
	res = logisticRegressionClassifier.predict(testInput)[0]
	prob = logisticRegressionClassifier.predict_proba(testInput)[0]
	if res == 1:
		print("Hacking Related")
		# confidence
		print(prob[1])
	elif res == 0:
		print("Not Hacking Related")
		print(prob[0])
	print("***********************************************************************")
	# Linear SVC Classifier Predict & Confidence
	print("Linear SVC: ")
	res = linearSVCClassifier.predict(testInput)[0]
	prob = linearSVCClassifier._predict_proba_lr(testInput)[0]
	if res == 1:
		print("Hacking Related")
		# confidence
		print(prob[1])
	elif res == 0:
		print("Not Hacking Related")
		print(prob[0])
	print("***********************************************************************")


# Testing Classifiers:
calculatePredictionAndConfidence(
	["Kirby and the Forgotten Land is a 2022 platform video game developed by HAL Laboratory and published by Nintendo "
	 "for the Nintendo Switch"])

calculatePredictionAndConfidence(
	["Tennis is a racket sport that can be played individually against a single opponent (singles) or between two "
	 "teams of two players each (doubles)."])

calculatePredictionAndConfidence(
	["usually yes, also there is waf bypass tools on hackbar. In general, you can hack unsafe sites but also you "
	 "can find a vulnerability in 'government' sites or bet sites. Anyway I will open new topics for advanced "
	 "level"])

calculatePredictionAndConfidence(
	["Dolly (5 July 1996 – 14 February 2003) was a female Finnish Dorset sheep and the first mammal cloned from an "
	 "adult somatic cell."])

calculatePredictionAndConfidence(
	["I am trying to understand if it is really possible to hack these days into a gmail account or any other mail "
	 "account knowing how good are the security ? and if there is someone capable of doing it ?"])

calculatePredictionAndConfidence(
	["Goodmorning I was wondering how to hack someone's security cameras i would appreciate any help. Ps : His "
	 "cameras are not wirelles"])

calculatePredictionAndConfidence(
	["A snow leopard conservation project was hailed a success, Britain was found to be 'surprisingly' united, "
	 "and an electric plane took to the skies, plus more."])

# TODO: dump best working classifier to pickle file
