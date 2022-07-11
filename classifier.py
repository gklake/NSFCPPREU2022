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

testCSV = pd.read_csv('csvFiles/sentences.csv')
trainCSV = pd.read_csv('csvFiles/sentencesTrain.csv')

# stop word removal and lemmatization
stopWords = nltk.corpus.stopwords.words('english')
lemmatizer = WordNetLemmatizer()

# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# print(trainCSV.head())
# print(testCSV.head())

trainXNon = trainCSV['sentence']
trainY = trainCSV['label']

testXNon = testCSV['sentence']
testY = testCSV['label']

trainX = []
testX = []

# text pre-processing
for i in range(0, len(trainXNon)):
    review = re.sub('[^a-zA-Z]', ' ', trainXNon[i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopWords)]
    review = ' '.join(review)
    trainX.append(review)

# text pre-processing
for i in range(0, len(testXNon)):
    review = re.sub('[^a-zA-Z]', ' ', testXNon[i])
    review = review.lower()
    review = review.split()
    review = [lemmatizer.lemmatize(word) for word in review if word not in set(stopWords)]
    review = ' '.join(review)
    testX.append(review)

print("trainX[0]: " + str(trainX[0]))
print("testX[0]: " + str(testX[0]))
print("***********************************************************************")

tfIdf = TfidfVectorizer()

# applying tf idf to training data
xTrainTf = tfIdf.fit_transform(trainX)

# applying tf-idf to training data
xTrainTf = tfIdf.transform(trainX)

print("Train: n_samples: %d, n_features: %d" % xTrainTf.shape)

xTestTf = tfIdf.transform(testX)
print("Test: n_samples: %d, n_features: %d" % xTestTf.shape)
print("***********************************************************************")

# Model Creation

# naive bayes
print("Naive Bayes: ")
naiveBayesClassifier = MultinomialNB()
naiveBayesClassifier.fit(xTrainTf, trainY)

yPred = naiveBayesClassifier.predict(xTestTf)
print(metrics.classification_report(testY, yPred, target_names=['Hacking Related', 'Not Hacking Related']))

print("Confusion Matrix:")
print(metrics.confusion_matrix(testY, yPred))
print("***********************************************************************")

# random forest
print("Random Forest: ")
randomForestClassifier = RandomForestClassifier()
randomForestClassifier.fit(xTrainTf, trainY)

yPred = randomForestClassifier.predict(xTestTf)
print(metrics.classification_report(testY, yPred, target_names=['Hacking Related', 'Not Hacking Related']))

print("Confusion Matrix:")
print(metrics.confusion_matrix(testY, yPred))
print("***********************************************************************")

# logistic regression
print("Logistic Regression: ")
logisticRegressionClassifier = LogisticRegression()
logisticRegressionClassifier.fit(xTrainTf, trainY)

yPred = logisticRegressionClassifier.predict(xTestTf)
print(metrics.classification_report(testY, yPred, target_names=['Hacking Related', 'Not Hacking Related']))

print("Confusion Matrix:")
print(metrics.confusion_matrix(testY, yPred))
print("***********************************************************************")

# Linear SVC
print("Linear SVC: ")
linearSVCClassifier = LinearSVC()
linearSVCClassifier.fit(xTrainTf, trainY)

yPred = linearSVCClassifier.predict(xTestTf)
print(metrics.classification_report(testY, yPred, target_names=['Hacking Related', 'Not Hacking Related']))

print("Confusion Matrix:")
print(metrics.confusion_matrix(testY, yPred))
print("***********************************************************************")


# Testing model with different strings
def calculatePredictionAndConfidence(text):
    # global review, testProcessed, testInput, res, prob
    textReview = re.sub('[^a-zA-Z]', ' ', text[0])
    textReview = textReview.lower()
    textReview = textReview.split()
    textReview = [lemmatizer.lemmatize(word) for word in textReview if word not in set(stopWords)]
    testProcessed = [' '.join(textReview)]
    print("testProcessed: ")
    print(testProcessed)
    testInput = tfIdf.transform(testProcessed)
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


calculatePredictionAndConfidence(
    ["A hacker is a person skilled in information technology who uses their technical knowledge to achieve a goal or"
     " overcome an obstacle, within a computerized system by non-standard means."])

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
    ["A snow leopard conservation project was hailed a success, Britain was found to be ‘surprisingly’ united, "
     "and an electric plane took to the skies, plus more."])
