import nltk
import numpy as np
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('stopwords')

# important words that occur a few times will be assigned high weights

# Example text corpus for our tutorial
text = ['Topic sentences are similar to mini thesis statements.\
        Like a thesis statement, a topic sentence has a specific \
        main point. Whereas the thesis is the main point of the essay',
        'the topic sentence is the main point of the paragraph.\
        Like the thesis statement, a topic sentence has a unifying function. \
        But a thesis statement or topic sentence alone doesnt guarantee unity.',
        'An essay is unified if all the paragraphs relate to the thesis,\
        whereas a paragraph is unified if all the sentences relate to the topic sentence.']

text2 = ['Topic sentences are similar to mini thesis statements.\
        Like a thesis statement, a topic sentence has a specific \
        main point. Whereas the thesis is the main point of the essay']

stopWords = stopwords.words('english')

sentences = []
wordSet = []

for sent in text:
    x = [i.lower() for i in word_tokenize(sent) if i.isalpha() and i not in stopWords]
    sentences.append(x)
    for word in x:
        if word not in wordSet:
            wordSet.append(word)

wordSet = set(wordSet)
print("wordSet:" + str(wordSet))
totalDocuments = len(sentences)
print("Total Documents: " + str(totalDocuments))

indexDict = {}
i = 0
for word in wordSet:
    indexDict[word] = i
    i += 1

print("indexDict: " + str(indexDict))


def countDict(textSentence):
    totalWordCount = {}
    for w in wordSet:
        totalWordCount[w] = 0
        for s in textSentence:
            if w in s:
                totalWordCount[w] += 1
    return totalWordCount


wordCount = countDict(sentences)
print("wordCount: " + str(wordCount))


def termFreq(document, targetWord):
    N = len(document)
    print(document)
    occurrence = len([token for token in document if token == targetWord])
    return occurrence / N


def inverseDocFreq(targetWord2):
    try:
        wordOccurrence = wordCount[targetWord2] + 1
    except:
        wordOccurrence = 1
    return np.log(totalDocuments / wordOccurrence)


def tfIdf(sentence):
    tfIdfVector = np.zeros((len(wordSet),))
    for w in sentence:
        tf = termFreq(sentence, w)
        idf = inverseDocFreq(w)
        print("Word: " + w)
        print("TF: " + str(tf))
        print("IDF: " + str(idf))

        value = tf * idf
        print("TF*IDF: " + str(value))
        tfIdfVector[indexDict[w]] = value
    return tfIdfVector


vectors = []
for sent in sentences:
    vec = tfIdf(sent)
    vectors.append(vec)
    print("Vector: " + str(vec))

print("vectors[0]: " + str(vectors[0]) + " Size: " + str(vectors[0].size) + " Sum: " + str(sum(vectors[0])))
print("vectors[1]: " + str(vectors[1]) + " Size: " + str(vectors[1].size) + " Sum: " + str(sum(vectors[1])))
print("vectors[2]: " + str(vectors[2]) + " Size: " + str(vectors[2].size) + " Sum: " + str(sum(vectors[2])))
