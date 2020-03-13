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
        str_data = entities2id[h]+' '+relation2id[r]+' '+entities2id[t]
        full_train[str_data] = 0


local2global_0 = []
local2global_1 = []
local2global_2 = []
local2global_3 = []


def read_local2global(path, local2global):
    with open(path) as f:
    	for line in f:
            global_id = line.strip()
            local2global.append(int(global_id))


read_local2global('./partition_0/local_to_global.txt', local2global_0)
read_local2global('./partition_1/local_to_global.txt', local2global_1)
read_local2global('./partition_2/local_to_global.txt', local2global_2)
read_local2global('./partition_3/local_to_global.txt', local2global_3)


def check_part_train(path, local2global):
    with open(path) as f:
        for line in f:
            h, r, t = line.strip().split('\t')
            h_global = local2global[int(h)]
            t_global = local2global[int(t)]
            str_data = str(h_global)+' '+r+' '+str(t_global)
            if str_data in full_train.keys():
                if full_train[str_data] == 0:
                    full_train[str_data] += 1
                else:
                    print("duplicate key: %s" % str_data)
            else:
                print('do not have key: %s' % str_data)


check_part_train('./partition_0/train.txt', local2global_0)
check_part_train('./partition_1/train.txt', local2global_1)
check_part_train('./partition_2/train.txt', local2global_2)
check_part_train('./partition_3/train.txt', local2global_3)

print("Finish Test")