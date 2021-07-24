import pyprind
import pandas as pd
import os
pbar = pyprind.ProgBar(50000);

labels = {'pos': 1, 'neg' : 0};

df = pd.DataFrame();

for s in ('test', 'train'):
    for l in ('pos', 'neg'):
        path = 'C:\\Users\\CH_T460s\\Downloads\\aclImdb_v1.tar\\aclImdb_v1\\aclImdb\\' + s + "\\" + l;

        for file in os.listdir(path):
            fullpath = path + "\\" + file;
            infile = open(fullpath, 'r', encoding="utf8");
            tmpstr = infile.read();
            df = df.append([[tmpstr, labels[l]]], ignore_index=True);
            pbar.update();

df.columns=['review', 'sentiment'];

import numpy as np
np.random.seed(0);

df = df.reindex(np.random.permutation(df.index));
df.to_csv("move_data.csv", index=False);


