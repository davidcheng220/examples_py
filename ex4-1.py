# 將該數列的總和與平均計算完畢後顯示在畫面上
# 請輸入整數數列(空白分隔): 1 2 3 4 5
# 數列為: 1 2 3 4 5
# 總和 = 15
# 平均 = 3.0

user_list = []
total = 0
user = input("請輸入整數數列(空白分隔): ").split()
divide = float

# ok
# for i in user:
#     user_list.append(int(i))
#     # total += int(user[i])
#     total += int(i)

for i in range(len(user)):
    # list inside is string need to convert to int
    user_list.append(int(user[i]))
    total += user_list[i]
    # total += int(user[i])

# for i in user_list:
#     total += i
    
divide = total / len(user_list)

print("數列為:", user_list)
print("總和 =" , total)
print("平均 =", divide)
