list = [1, 2, 'aaa', 'bbb', [3, 'ccc'], (4, 5)]
idx_type = []
for idx, itm in enumerate(list):
    idx_type.append(type(itm))
print(idx_type)