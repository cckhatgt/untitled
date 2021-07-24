import pandas as pd;
import numpy as np;

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris;

import matplotlib.pyplot as plt

# np.random.seed(0)
#
# iris = load_iris()
# df = pd.DataFrame(iris.data, columns=iris.feature_names)
#
# df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
# df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.75
# train, test = df[df['is_train'] == True], df[df['is_train'] == False];
#
# features = df.columns[0:4]
# y = pd.factorize(train["species"])[0];
#
# clf = RandomForestClassifier(n_jobs=2, random_state=0);
# clf.fit(train[features], y)
# preds = iris.target_names[clf.predict(test[features])];
#
# validation = pd.crosstab(test['species'], preds, rownames=['Actual Species'], colnames=['Predicted Species'])
# print(validation)

import quandl
import pandas as pd

auth_tok = "D2HiDbW_BnmC6GwwMpsv"
print(auth_tok)

#data = quandl.get("WIKI/AAPL", authtoken=auth_tok)
tesla = quandl.get('WIKI/TSLA', authtoken=auth_tok)
gm = quandl.get('WIKI/GM', authtoken=auth_tok)

print(gm.keys())
print(gm.columns)
print(gm.columns)

# plt.plot(gm.index, gm['Adj. Close'])
# plt.title('GM Stock Price')
# plt.ylabel('Price ($)');
# plt.show()
#
# plt.plot(tesla.index, tesla['Adj. Close'], 'r')
# plt.title('Tesla Stock Price')
# plt.ylabel('Price ($)');
# plt.show();


# Yearly average number of shares outstanding for Tesla and GM
tesla_shares = {2018: 168e6, 2017: 162e6, 2016: 144e6, 2015: 128e6, 2014: 125e6, 2013: 119e6, 2012: 107e6, 2011: 100e6,
                2010: 51e6}
gm_shares = {2018: 1.42e9, 2017: 1.50e9, 2016: 1.54e9, 2015: 1.59e9, 2014: 1.61e9, 2013: 1.39e9, 2012: 1.57e9,
             2011: 1.54e9, 2010: 1.50e9}
# Create a year column
tesla['Year'] = tesla.index.year
# Take Dates from index and move to Date column
tesla.reset_index(level=0, inplace=True)
tesla['cap'] = 0
# Calculate market cap for all years
for i, year in enumerate(tesla['Year']):
    # Retrieve the shares for the year
    shares = tesla_shares.get(year)

    # Update the cap column to shares times the price
    tesla.loc[i, 'cap'] = shares * tesla.loc[i, 'Adj. Close']

print(tesla.head())