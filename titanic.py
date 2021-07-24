# linear algebra
import numpy as np

# data processing
import pandas as pd

# data visualization
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import style

# Algorithms
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import GaussianNB

testData = pd.read_csv("data/test.csv")
trainData = pd.read_csv("data/train.csv");

trainData.info()
trainData.describe()
trainData.head(8)

total = trainData.isnull().sum().sort_values(ascending=False)
percent_1 = trainData.isnull().sum()/trainData.isnull().count()*100
percent_2 = (round(percent_1, 1)).sort_values(ascending=False)
missing_data = pd.concat([total, percent_2], axis=1, keys=['Total', '%'])
missing_data.head(5)

trainData.columns.values


trainData = trainData.drop(['PassengerId'], axis=1)

import re
deck = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "U": 8}
data = [trainData, testData]

for dataset in data:
    dataset['Cabin'] = dataset['Cabin'].fillna("U0")
    dataset['Deck'] = dataset['Cabin'].map(lambda x: re.compile("([a-zA-Z]+)").search(x).group())
    dataset['Deck'] = dataset['Deck'].map(deck)
    dataset['Deck'] = dataset['Deck'].fillna(0)
    dataset['Deck'] = dataset['Deck'].astype(int)
# we can now drop the cabin feature
trainData= trainData.drop(['Cabin'], axis=1)
testData = testData.drop(['Cabin'], axis=1)


data = [trainData, testData]

for dataset in data:
    mean = trainData["Age"].mean()
    std = testData["Age"].std()
    is_null = dataset["Age"].isnull().sum()

    rand_age = np.random.randint(mean - std, mean + std, size = is_null)
    age_slice = dataset["Age"].copy()
    age_slice[np.isnan(age_slice)] = rand_age
    dataset["Age"] = age_slice
    dataset["Age"] = trainData["Age"].astype(int)

trainData["Age"].isnull().sum()

common_value = 'S'
data = [trainData, testData]

for dataset in data:
    dataset['Embarked'] = dataset['Embarked'].fillna(common_value)

trainData.info()

data = [trainData, testData]

for dataset in data:
    dataset['Fare'] = dataset['Fare'].fillna(0)
    dataset['Fare'] = dataset['Fare'].astype(int)

genders = {"male": 0, "female": 1}
data = [trainData, testData]

for dataset in data:
    dataset['Sex'] = dataset['Sex'].map(genders)

trainData = trainData.drop(['Ticket'], axis=1)
testData = testData.drop(['Ticket'], axis=1)

ports = {"S": 0, "C": 1, "Q": 2}
data = [trainData, testData]

for dataset in data:
    dataset['Embarked'] = dataset['Embarked'].map(ports)

print(dataset)