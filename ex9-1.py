# 輸入資料 (或直接按 Enter 結束):  
# 1. 水果 
# 2. 鮮奶 
# 3. 麵包 
# 存檔完畢!
# ✤使用者可以輸入多列資料 
# ✤沒有輸入資料直接按 Enter 鍵會結束輸入 
# ✤結束後會自動將輸入內容存檔
import pathlib

user = input("輸入資料(或直接按enter結束): \n").split()

with open("file.txt", 'w', encoding = "UTF-8") as f:
    for i in user:
        f.writelines(i)
    f.close()
    print("存檔完畢!")