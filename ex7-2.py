# 使用者輸入
# • 借書日期：格式為「年-月-日」
# • 可借幾日：例如 7 日
# ✤ 顯示
# • 還書日期
# • 顯示今天是否逾期
# ✦ 未逾期，顯示還有幾天才需還書
# ✦ 若逾期，顯示逾期天數
from datetime import date, timezone
from datetime import datetime
from datetime import timedelta

# get user input year, month, day, and transfer to date strim
user_input= input("借書日期: 格式為「年-月-日」")

# formate transformation
fmt = "%Y-%m-%d"
date_strim = datetime.strptime(user_input, fmt).date()

# copy date
user_date = date_strim
# print test
# print("------------------------------")
# print(user_date)
# print(date_strim)
# print("------------------------------")
# year = user_date[0]
# month = user_date[1]
# day = user_date[2]

# get user wants to borrow how many day(s)
borrow_date = int(input("可借幾日：例如 7 日 "))

# return date = user date + borrow date
return_date = user_date + timedelta(days = borrow_date)
print(f"{return_date}前歸還")

# now transfer to date format
today = datetime.now().date()

print("今天是", today)
# get expire date = today - return date
expire_date = today - return_date

# if expire date is greater than 0 then print how many days has expired
# else reverse the calculation then print how many days left to return
if expire_date.days > 0:
    print(f"逾期天數:{expire_date.days}")
else:
    expire_date = return_date - today
    print(f"您必須在{expire_date.days}天前歸還")