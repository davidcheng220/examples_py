# 使用者輸入起與止的數字，可以顯示差為 1 的等差數列與其總和
# 起始值: 1
# 終止值：40
# 01 02 03 04 05 06 07 08 09 10
# 11 12 13 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27 28 29 30
# 31 32 33 34 35 36 37 38 39 40
# 總和: 820


start = int(input("起始值: "))
end = int(input("終止值: "))
total = 0

for i in range(start, end + 1):
    total += i
    if i < 10:
        print("0", end="")
    print(i, end=" ")
    # print(f"{i:02d}", end=" ")

    if i % 10 == 0:
        # print("\n")
        print()

print("\n總和: ", total)