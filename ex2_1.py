# # 讓使用者輸入被除數與除數，整數除法後取其商與餘數，如下所示：
# # 請輸入被除數: 10
# # 請輸入除數: 3
# # 10 // 3 = 3 ... 1


# 被除數
dividend_number = int(input("請輸入被除數: "))
# 除數
divisor_number = int(input("請輸入除數: "))
# 商數
quotient = dividend_number // divisor_number
# 餘數
remainder = dividend_number % divisor_number
# 列印結果
print(f"{dividend_number} // {divisor_number} = {quotient}...{remainder}")

