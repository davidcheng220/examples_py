# 小華十分熱衷大樂透，但他不選不吉利數字，如果他輸入 4（可以輸入1~9數字，輸入錯誤要求重新
# 輸入），代表 1~49 個可選擇的大樂透數字中，無論個位數或十位數有 4 的數字（例如：4、14、
# 45），他都不選，程式要能顯示剩下他可以選擇的數字有哪些？並且將這些數字的總個數也一併顯
# 示出來
# 不吉利數字 (1 ~ 9) : 12
# 輸入錯誤，請再輸入一次
# 不吉利數字 (1 ~ 9) : 4
# 01 02 03 05 06 07 08 09 10 11
# 12 13 15 16 17 18 19 20 21 22
# 23 25 26 27 28 29 30 31 32 33
# 35 36 37 38 39
# 總個數: 35

# unlucky = int(input("不吉利數字(1~9): "))
count = 0

# if unlucky < 1 or unlucky > 9:
#     print("輸入錯誤，請再輸入一次")
#     unlucky = int(input("不吉利數字(1~9): "))

while True:
    unlucky = int(input("不吉利數字(1~9): "))
    if unlucky < 1 or unlucky > 9:
        print("輸入錯誤，請再輸入一次")
    else:
        break

for i in range(1, 50):
    if i // 10 == unlucky or i % 10 == unlucky:
        continue
    count += 1
    # correct
    # if i < 10:
    #     print("0", end="")
    print(i, end = " ")

    if count % 10 == 0:
        print()
    # wrong
    if i < 10:
        print("0", end="")

print("\n總個數: ", count)