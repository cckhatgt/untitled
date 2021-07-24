import numpy as np;
from sklearn import datasets;

from sklearn.model_selection import train_test_split;

iris = datasets.load_iris();
X = iris.data[:, [2, 3]];
print(X.shape)
y = iris.target;

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=0);
print(X_train.shape);
print(X_test.shape)

from sklearn.preprocessing import StandardScaler;

sc = StandardScaler();
sc.fit(X_train);
X_train_std = sc.transform(X_train);
X_test_std = sc.transform(X_test)

from sklearn.linear_model import Perceptron;
ppn = Perceptron(n_iter_no_change=40, eta0=0.1, random_state=0);
ppn.fit(X_train_std, y_train)

y_pred = ppn.predict(X_test_std)
print((y_pred != y_test).sum())
print(y_pred.shape)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, y_pred))

from matplotlib.colors import ListedColormap;
import matplotlib.pyplot as plt

