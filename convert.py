import os

entity2id_global = {}

with open('entities.dict') as f:
    for line in f:
        eid, entity = line.strip().split('\t')
        entity2id_global[entity] = int(eid)

count = 0
entity2id_local = {}
local_to_global = []

with open('train.txt') as f:
    for line in f:
        h, r, t = line.strip().split('\t')
        if h not in entity2id_local.keys():
            entity2id_local[h] = count
            local_to_global.append(entity2id_global[h])
            count += 1
        if t not in entity2id_local.keys():
            entity2id_local[t] = count
            local_to_global.append(entity2id_global[t])
            count += 1

# write
f = open('entities.dict.local', 'w')
for key, value in entity2id_local.items():
    f.write(str(value)+'\t'+key)
f.close()

f = open('local_to_global.txt', 'w')
for data in local_to_global:
    f.write(str(data)+'\n')
f.close()