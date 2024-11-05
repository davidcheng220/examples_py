# 定義 1 個函式: calculate(numbers, myFunction)
# • numbers: 一個數列
# • myFunction: 一個函式會計算 numbers 所有元素的平均值後顯示在畫面上
# ✤ 讓使用者輸入一個數列，會將平均顯示在畫面上
# 請輸入整數數列(空白分隔): 1 2 3 4 5
# 數列為: 1 2 3 4 5
# 平均 = 3.0

def calculate(numbers, myFumction):
    average(numbers)

def average(numbers):
    sum = 0

    for index in range(len(numbers)):
        sum += int(numbers[index])
    
    average = sum / len(numbers)
    print(f"平均: {average}")


def main():
    number_list = input("請輸入整數數列(空白分隔): ")
    split_number = number_list.split()
    print(f"數列為: {number_list}")
    calculate(split_number, average)

main()