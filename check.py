import os

partition_book = []
local_to_global_0 = []
local_to_global_1 = []
local_to_global_2 = []
local_to_global_3 = []


total_count = 0
double_count = 0
train_count = 0
test_count = 0
valid_count = 0

print("read partition_book..")

with open('./part_0/partition_book.txt') as f:
    for line in f:
        part = int(line.strip())
        partition_book.append(part)


print("read local_to_global_0..")

with open('local_to_global_0.txt') as f:
    for line in f:
        global_id = int(line.strip())
        local_to_global_0.append(global_id)


print("read local_to_global_1..")

with open('local_to_global_1.txt') as f:
    for line in f:
        global_id = int(line.strip())
        local_to_global_1.append(global_id)

print("read local_to_global_2..")

with open('local_to_global_2.txt') as f:
    for line in f:
        global_id = int(line.strip())
        local_to_global_2.append(global_id)

print("read local_to_global_3..")

with open('local_to_global_3.txt') as f:
    for line in f:
        global_id = int(line.strip())
        local_to_global_3.append(global_id)


print("read train_0..")

with open('train_0.txt') as f:
    for line in f:
        total_count += 1
        h, r, t = line.strip().split('\t')
        h_global = local_to_global_0[int(h)]
        t_global = local_to_global_0[int(t)]
        h_part = partition_book[h_global]
        t_part = partition_book[t_global]
        if h_part != t_part:
            double_count += 1

print("read train_1..")

with open('train_1.txt') as f:
    for line in f:
        total_count += 1
        h, r, t = line.strip().split('\t')
        h_global = local_to_global_1[int(h)]
        t_global = local_to_global_1[int(t)]
        h_part = partition_book[h_global]
        t_part = partition_book[t_global]
        if h_part != t_part:
            double_count += 1

print("read train_2..")

with open('train_2.txt') as f:
    for line in f:
        total_count += 1
        h, r, t = line.strip().split('\t')
        h_global = local_to_global_2[int(h)]
        t_global = local_to_global_2[int(t)]
        h_part = partition_book[h_global]
        t_part = partition_book[t_global]
        if h_part != t_part:
            double_count += 1

print("read train_3..")

with open('train_3.txt') as f:
    for line in f:
        total_count += 1
        h, r, t = line.strip().split('\t')
        h_global = local_to_global_3[int(h)]
        t_global = local_to_global_3[int(t)]
        h_part = partition_book[h_global]
        t_part = partition_book[t_global]
        if h_part != t_part:
            double_count += 1


print("read train..")

with open('train.txt') as f:
    for line in f:
        train_count += 1

print("read valid..")

with open('valid.txt') as f:
    for line in f:
        valid_count += 1

print("read test..")

with open('test.txt') as f:
    for line in f:
        test_count += 1

 print('4 part edges: %d' % (total_count-double_count))
 print('train_count: %d' % (train_count))
 print('train + valid + test: %d' % (train_count+valid_count+test_count))
