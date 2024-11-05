# 建立 1 個長方體 (Cuboid) 類別，內容包含
# • 屬性：長 (length)、寬 (width)、高 (height)
# • 方法
# ✦ volume() 方法：計算完體積並回傳
# ✦ getInfo() 方法：回傳長、寬、高與體積
# • 建構式：設定屬性初始值
# ✤ 主流程
# • 將使用者輸入的長、寬、高建立 Cuboid 物件，並顯示該物件長、寬、高與體積
# 請輸入長方體的長、寬、高(空白間隔): 1 2 3
# 輸入的長方體資訊如下:
# 長: 1.0, 寬: 2.0, 高: 3.0, 體積: 6.0

class cuboid:
    """
    體積: 物件導向
    """
    def __init__(self, length, width, height):
        """
        長: float
        寬: float
        高: float
        """
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        """
        運算體積 = 長*寬*高
        """
        volume = self.length * self.width * self.height
        # print(f"體積: {volume}")
        return volume

    def getInfo(self):
        """
        數據提取
        """
        print(f"長: {self.length}, 寬: {self.width}, 高: {self.height}")

def main():
    user = input("請輸入長方體的長、寬、高(空白間隔)").split()
    # 類別對應物件
    cube = cuboid(float(user[0]), float(user[1]), float(user[2]))
    cube.getInfo()
    print("體積: ",cube.volume())

main()