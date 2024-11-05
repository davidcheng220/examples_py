# 使用者輸入好友名與身上現金， 輸入完後以 dictionary 方式儲存好友資訊
# 之後讓使用者輸入欲借金額，便會顯示可借錢給他的好友姓名以及總數
# 請問有幾個好友? 5
# 請輸入第1個好友名與身上現金: Mary 2000
# 請輸入第2個好友名與身上現金: John 1000
# 請輸入第3個好友名與身上現金: Sue 800
# 請輸入第4個好友名與身上現金: Linda 1200
# 請輸入第5個好友名與身上現金: Ken 500
# --------------------------------------------------
# 請輸入欲借現金: 1200
# 可借錢的好友: Mary, Linda, 共2人

friend_number = int(input("請問有幾個好友? "))
friend = {}
count = 0
text = ""

for friends in range(friend_number):
    friend_name_pocket = input(f"請輸入第{friends + 1}個好友名與身上現金: ").split()
    # friend["name"] = friend_name_cash[0]
    name = friend_name_pocket[0]
    # friend["cash"] = int(friend_name_cash[1])
    pocket = int(friend_name_pocket[1])
    # key to value
    friend["name"] = pocket

    # print(friend.items())

print("--------------------------------------------------")

cash = int(input("請輸入欲借現金: "))

for name, pocket in friend.items():
    if pocket >= cash:
        count += 1
        text += name + ", "
print(f"可借錢的好友:{text}共{count}人")