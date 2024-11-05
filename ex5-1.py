# 定義1個 calculate(numbers)，共有 2 個回傳值
# • 計算numbers所有元素的總和與平均值並回傳 (回傳總和與平均)
# ✤ 讓使用者輸入一個數列，輸入完畢後呼叫上述 calculate 函式運算，
# 並將回傳的總和與平均顯示在畫面上
# 10
# 請輸入整數數列(空白分隔): 1 2 3 4 5
# 數列為: 1 2 3 4 5
# 總和 = 15
# 平均 = 3.0
list_num = input("請輸入整數數列(空白分隔):").split()

def calculate(number):
    sum = 0
    num_list =[]
    text = ""
    
    for index in range(len(list_num)):
        # num_list.append(int(list_num[index]))
        text += list_num[index] + " "
    print(f"數列為: {text}")

    for i in range(len(number)):
        sum += int(number[i])

    average = sum / len(number)
    return sum, average

sum, average,= calculate(list_num)

print("總和 =", sum)
print("平均 =", average)