# 承襲 6-1，不過改成可以輸入多個長方體資訊，所以 Cuboid 類別新增一個static方法
# • getCuboidsInfo(cuboid)：回傳所有長方體資訊
# ✤ 主流程
# • 詢問使用者欲輸入的長方體總個數
# • 讓使用者輸入指定個數的長方體資訊，並顯示所有輸入長方體的長、寬、高與體積
# 請問有幾個長方體? 3
# 請輸入第1個長方體的長、寬、高(空白間隔): 1 1 1
# 請輸入第2個長方體的長、寬、高(空白間隔): 2 2 2
# 請輸入第3個長方體的長、寬、高(空白間隔): 3 3 3
# 輸入的3個長方體資訊如下:
# 長: 1.0, 寬: 1.0, 高: 1.0, 體積: 1.0
# 長: 2.0, 寬: 2.0, 高: 2.0, 體積: 8.0
# 長: 3.0, 寬: 3.0, 高: 3.0, 體積: 27.0

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
    
    # @staticmethod
    # def getCuboidInfo(cls):
    #     getInfo()

def main():
    user = input("請輸入長方體的長、寬、高(空白間隔)").split()
    # 類別對應物件
    cube = cuboid(float(user[0]), float(user[1]), float(user[2]))
    cube.getInfo()
    print("體積: ",cube.volume())

main()