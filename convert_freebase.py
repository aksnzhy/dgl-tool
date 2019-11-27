import os


count = 0

local_train_data = []
local_to_global = []
entity_book = {}

with open('fb.txt') as f:
    for line in f:
        h_count = 0;
        t_count = 0
        h, t, r = line.strip().split('\t')
        if h not in entity_book.keys():
            entity_book[h] = count
            local_to_global.append(h)
            h_count = count
            count += 1
        else:
            h_count = entity_book[h]
        if t not in entity_book.keys():
            entity_book[t] = count
            local_to_global.append(t)
            t_count = count
            count += 1
        else:
            t_count = entity_book[t]

        local_train_data.append(str(h_count)+'\t'+str(t_count)+'\t'+r)

# write
f = open('train.txt', 'w')
for data in local_train_data:
    f.write(data+'\n')
f.close()

f = open('local_to_global.txt', 'w')
for data in local_to_global:
    f.write(data+'\n')
f.close()