import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer();
docs = np.array([
    "The sun is shining",
    "The weather is sweet",
    "The sun is shining and the weather is sweet" ])

bag = count.fit_transform(docs)
print(count.vocabulary)
print("##")
print(count.vocabulary_)

print(bag.toarray());

def tokenizer(text):
        return text.split();

tokenizer("runners like running and thus they run")

import nltk
nltk.download("stopwords");

from nltk.corpus import stopwords
stop = stopwords.words("English");
[w for w in tokenizer("runners like running and thus they run") if w not in stop]

p = tokenizer("runners like running and thus they run")
for w in p:
    if (w not in stop):
        print(w)
