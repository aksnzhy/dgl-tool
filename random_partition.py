import os
from random import randrange

train_0 = []
train_1 = []
train_2 = []
train_3 = []

with open('train.txt') as f:
    for line in f:
        h, t, r = line.strip().split('\t')
        p_id = randrange(4)
        if p_id == 0:
            train_0.append(h+'\t'+t+'\t'+r)
        elif p_id == 1:
            train_1.append(h+'\t'+t+'\t'+r)
        elif p_id == 2:
            train_2.append(h+'\t'+t+'\t'+r)
        elif p_id == 3:
            train_3.append(h+'\t'+t+'\t'+r)
        else:
            print("error")
            break


# write
f = open('train_0.txt', 'w')
for data in train_0:
    f.write(data+'\n')
f.close()

f = open('train_1.txt', 'w')
for data in train_1:
    f.write(data+'\n')
f.close()

f = open('train_2.txt', 'w')
for data in train_2:
    f.write(data+'\n')
f.close()

f = open('train_3.txt', 'w')
for data in train_3:
    f.write(data+'\n')
f.close()
