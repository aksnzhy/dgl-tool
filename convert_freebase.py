import os


count = 0

local_train_data = []
local_to_global = []
entity_book = {}

with open('train.txt.full') as f:
    for line in f:
        h_count = 0;
        t_count = 0
        h, t, r = line.strip().split('\t')
        if h not in entity_book.keys():
            entity_book[int(h)] = count
            local_to_global.append(int(h))
            h_count = count
            count += 1
        else:
            h_count = entity_book[int(h)]
        if t not in entity_book.keys():
            entity_book[int(t)] = count
            local_to_global.append(int(h))
            t_count = count
            count += 1
        else:
            t_count = entity_book[int(t)]
        local_train_data.append(str(h_count)+'\t'+str(t_count)+r)

# write
f = open('train.txt', 'w')
for data in local_train_data:
    f.write(data+'\n')
    print(data+'\n')
f.close()

f = open('local_to_global.txt', 'w')
for data in local_to_global:
    f.write(str(data)+'\n')
f.close()