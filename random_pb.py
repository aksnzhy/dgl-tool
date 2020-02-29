import os
from random import randrange

pb = []

for i in range(86054151):
    p_id = randrange(4)
    pb.append(p_id)

f = open('partition_book.txt', 'w')
for data in pb:
    f.write(str(data)+'\n')
f.close()