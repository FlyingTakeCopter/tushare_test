import tushare as ts

# 海龟策略模型 版本:0.1
class Turtle01:
    code = 0
    name = ""
    nHigh = 20
    nLow = 10

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def countTR(self, ):
        return max(1, 3, 4, 5)

    # def countATR(self):




