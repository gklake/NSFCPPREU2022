import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

text = ["kolkata big city india trade",
        "mumbai financial capital india",
        "delhi capital india",
        "kolkata capital colonial times",
        "bangalore tech hub india software",
        "mumbai hub trade commerce stock exchange",
        "kolkata victoria memorial",
        "delhi india gate",
        "mumbai gate way india trade business",
        "delhi red fort india",
        "kolkata metro oldest india",
        "delhi metro largest metro network india"]

# using the count vectorizer
count = CountVectorizer()
wordCount = count.fit_transform(text)
print("Word Count: \n" + str(wordCount))

print("Word Shape: \n" + str(wordCount.shape))  # 12 sentences and 29 unique words

print("Word Count Array: \n" + str(wordCount.toarray()))

tfidfTransformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfidfTransformer.fit(wordCount)
dfIdf = pd.DataFrame(tfidfTransformer.idf_, index=count.get_feature_names_out(), columns=["IDF Weights"])

# inverse document frequency
print("Words by IDF Weights: ")
print(dfIdf.sort_values(by=["IDF Weights"]))

#tf-idf
tfidfVector = tfidfTransformer.transform(wordCount)
featureNames = count.get_feature_names_out()

firstDocumentVector = tfidfVector[1]
dfTfIdf = pd.DataFrame(firstDocumentVector.T.todense(), index=featureNames, columns=["TF-IDF"])
print("Words by TF-IDF: ")
print(dfTfIdf.sort_values(by=["TF-IDF"], ascending=False))
