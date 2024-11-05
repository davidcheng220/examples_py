# 假設一趟泰國之旅需要 20000 元與 5 天的假期。讓使用者輸入身
# 上的錢與放假天數，並顯示對應結果
# 身上的錢: 20000
# 放假天數: 5
# 可以去泰國玩
# 錢 >= 20000 假期 >= 5 列印結果
# True True 可以去泰國玩
# True False 有錢沒閒
# False True 有閒沒錢
# False False 沒錢沒閒，真可憐


# input cash
cash = int(input("身上的錢: "))
# input day off
day_off = int(input("放假天數: "))

# if cash is even and greater than 20000 and if day off has 5 days print conditions
if cash >= 20000:
    if day_off >= 5:
        # print statement
        print("可以出去玩")
    else:
        print("有錢沒閒")
# if cash is less than 20000 and if day off less than 5 days print conditions
if cash < 20000:
    if day_off >= 5:
        print("有閒沒錢")
    else:
        print("沒錢沒閒，真可憐")
