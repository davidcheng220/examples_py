# 大樂透號碼總共有 6 個號碼加 1 個特別號，而且都不重複
# ✤ 利用亂數產生一組大樂透號碼，除了特別號以外，其他 6 個號碼由小到大排序
# • 大樂透號碼都是1~49，可使用 random.randint(1, 49) 產生
# 開獎，大樂透號碼為:
# 38 11 43 13 15 23 特別號: 29
# 由小到大排列:
# 11 13 15 23 38 43 特別號: 29

import random

random_number = []
spec_number = random.randint(1,49)

for i in range(6):
    # print(i)
    # random_number.append(random.randint(1,49))
    num = random.randint(1,49)
    if num not in random_number or not spec_number:
        random_number.append(num)
    else:
        random_number.append(num)

    # for index in range(len(random_number)):
    #     if random_number[index] in random_number[i]:
    #         random_number.pop(index)
    #         random_number.append(rd.randint(1,49))
    #     else:
    #         random_number.append(rd.randint(1,49))
    

print(random_number)
print(spec_number)