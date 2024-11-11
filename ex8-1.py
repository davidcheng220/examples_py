# 被除數與除數皆正確，顯示運算結果 
# ✤被除數或除數格式錯誤，例如輸入 
# a，顯示「被除數或除數格式錯誤」 
# ✤除數輸入 0，顯示「除數不可為0，
# 請再重新輸入」
# 8
# 輸入被除數(整數): a 
# 被除數或除數格式錯誤，請重新輸入 
# 輸入被除數(整數): 10 
# 輸入除數(整數): 0 
# 除數不可為0，請重新輸入 
# 輸入被除數(整數): 10 
# 輸入除數(整數): 3 
# 10 ÷ 3 = 3 ... 1

def div(dividend, divisor):
    quotien = dividend // divisor
    r = dividend % divisor
    return quotien, r


def main():
    while True:
        try:
            dividend = int(input("輸入被除數(整數): "))
            divisor = int(input("輸入除數(整數): "))
            q, r = div(dividend, divisor)
            print(f"{dividend} ÷ {divisor} = {q} ... {r}")
            break
        except TypeError as e:
            print("格式錯誤，請重新輸入", e)
        except ValueError as e:
            print("格式錯誤，請重新輸入", e)
        except ZeroDivisionError as e:
            print("除數不可為0，請重新輸入")
        finally:
            print("Done")

main()

