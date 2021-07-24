import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RANSACRegressor

df = pd.read_csv("data/housing.data", header=None, sep='\s+');

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'];




# sns.set(style='whitegrid', context='notebook');

# cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV'];
#
# cm = np.corrcoef(df[cols].values.T)
# sns.set(font_scale=1.5);
# hm = sns.heatmap(cm,
#                  cbar=True,
#                  annot=True,
#                  square=True,
#                  yticklabels=cols,
#                  xticklabels=cols)
#
# sns.pairplot(df[cols], height = 3)
# #sns.pairplot(df, height=4)
#
# plt.show()

X = df[['RM']].values
x = df['RM'].values
y = df['MEDV'].values

slr = LinearRegression();
slr.fit(X, y);

ransac = RANSACRegressor(LinearRegression(),
                         max_trials=100,
                         min_samples=50,
                         residual_threshold=5.0,
                         random_state=0);

ransac.fit(X, y)