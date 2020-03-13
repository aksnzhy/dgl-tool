import os

entities2id = {}
relation2id = {}

with open('entities.dict') as f:
    for line in f:
        ent_id, ent_str = line.strip().split('\t')
        entities2id[ent_str] = ent_id

with open('relations.dict') as f:
    for line in f:
        rel_id, rel_str = line.strip().split('\t')
        relation2id[rel_str] = rel_id

full_train = {}

with open('train.txt') as f:
    for line in f:
        h, r, t = line.strip().split('\t')
        full_train[entities2id[h]+' '+relation2id[r]+' '+entities2id[t]] = 0


local2global_0 = []
local2global_1 = []
local2global_2 = []
local2global_3 = []


with open('./partition_0/local_to_global.txt') as f:
    for line in f:
        g_id = line.strip()
        local2global_0.append(int(g_id))

with open('./partition_1/local_to_global.txt') as f:
    for line in f:
        g_id = line.strip()
        local2global_1.append(int(g_id))

with open('./partition_2/local_to_global.txt') as f:
    for line in f:
        g_id = line.strip()
        local2global_2.append(int(g_id))

with open('./partition_3/local_to_global.txt') as f:
    for line in f:
        g_id = line.strip()
        local2global_3.append(int(g_id))


train_0 = []
train_1 = []
train_2 = []
train_3 = []


with open('./partition_0/train.txt') as f:
    for line in f:
        h, r, t = line.strip().split('\t')
        h_global = local2global_0[int(h)]
        t_global = local2global_0[int(t)]
        str_data = str(h_global)+' '+r+' '+str(t_global)
        if str_data in full_train.keys():
            if full_train[str_data] == 0:
                full_train[str_data] += 1
            else:
                print("duplicate key: %s" % str_data)
        else:
            print('do not have key: %s' % str_data)


with open('./partition_1/train.txt') as f:
    for line in f:
        h, r, t = line.strip().split('\t')
        h_global = local2global_1[int(h)]
        t_global = local2global_1[int(h)]
        str_data = str(h_global)+' '+r+' '+str(t_global)
        if str_data in full_train.keys():
            if full_train[str_data] == 0:
                full_train[str_data] += 1
            else:
                print("duplicate key: %s" % str_data)
        else:
            print('do not have key: %s' % str_data)

with open('./partition_2/train.txt') as f:
    for line in f:
        h, r, t = line.strip().split('\t')
        h_global = local2global_2[int(h)]
        t_global = local2global_2[int(h)]
        str_data = str(h_global)+' '+r+' '+str(t_global)
        if str_data in full_train.keys():
            if full_train[str_data] == 0:
                full_train[str_data] += 1
            else:
                print("duplicate key: %s" % str_data)
        else:
            print('do not have key: %s' % str_data)


with open('./partition_3/train.txt') as f:
    for line in f:
        h, r, t = line.strip().split('\t')
        h_global = local2global_3[int(h)]
        t_global = local2global_3[int(h)]
        str_data = str(h_global)+' '+r+' '+str(t_global)
        if str_data in full_train.keys():
            if full_train[str_data] == 0:
                full_train[str_data] += 1
            else:
                print("duplicate key: %s" % str_data)
        else:
            print('do not have key: %s' % str_data)


print("Yes!")