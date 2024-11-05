# ✤ 使用者輸入春、夏、秋、冬任一季節，會顯示該季節對應描述
# • 春：春暖花開
# • 夏：夏日炎炎
# • 秋：秋高氣爽
# • 冬：冬風凜冽
# 請輸入你喜愛的季節: 夏
# 夏日炎炎


quarter = input("請輸入你喜愛的季節: ")

match quarter:
    case "春":
        print("春暖花開")
    case "夏":
        print("夏日炎炎")
    case "秋":
        print("秋高氣爽")
    case "冬":
        print("冬風凜冽")
    # case TypeError:
    #     print("錯誤")