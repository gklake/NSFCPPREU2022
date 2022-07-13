import matplotlib as matplotlib
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.filterwarnings('ignore')

# Reading the data
TicketData = pd.read_csv('../csvFiles/supportTicketData.csv')

# Printing umber of rows and columns
print(TicketData.shape)

# Printing sample rows
print(TicketData.head(10))

# Number of unique values for urgency column
# There are 3 ticket types
print(TicketData.groupby('urgency').size())


# Plotting the bar chart
# %matplotlib inline
# TicketData.groupby('urgency').size().bar().show()

# Ticket Data
corpus = TicketData['body'].values

# Creating the vectorizer
vectorizer = CountVectorizer(stop_words='english')

# Converting the text to numeric data
X = vectorizer.fit_transform(corpus)

# print(vectorizer.get_feature_names())

# Preparing Data frame for machine learning
# priority column acts as a target variable and other columns as predictors
CountVectorizedData = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
CountVectorizedData['Priority'] = TicketData['urgency']
print(CountVectorizedData.shape)
print(CountVectorizedData.head())

