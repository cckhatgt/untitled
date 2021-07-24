from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

dataset = loadtxt('data/pima-indians-diabetes.data.txt', delimiter=',')
X = dataset[:, 0:8]
y = dataset[:, 8]

model = Sequential();
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'));
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=500, batch_size=10)

predictions = model.predict_classes(X)
for i in range(5):
	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

//test gui for testing branch
