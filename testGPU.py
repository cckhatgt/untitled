import tensorflow as tf;
import numpy as np;
print(tf.config.list_physical_devices('GPU'))

listsize = 30;

myList1 = np.full([5, 2], -1.1);
myList2 = np.full((5, 2), -1.1);

print(myList1.shape)
print(myList2.shape)

print(myList1 == myList2)

myBoolean = (myList1 == myList2).astype(int);
print(myBoolean)

