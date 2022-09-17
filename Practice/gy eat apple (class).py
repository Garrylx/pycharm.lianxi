"""class Data:
    def __init__(self):
        self.lists = [1,2,3,4,5]
    def change_lists(self,index,n):
        self.lists[index] = n   只能从客户端访问数据的一部分，通过对象访问
Data1 = Data()
Data1.lists[0] = 100
print(Data1.lists)

Data2 = Data()
Data2.change_lists(0,100)
print(Data2.lists)"""#只能从客户端访问数据的一部分，通过对象访问

class apple:
    def __init__(self,d,t):
        self.date = d
        self.mold = 0
        self.tempture = t
        print('苹果筛选装置启动')
    def rot(self):
        self.mold = self.date * self.tempture
        #不能用dt表示
        if self.mold >40:
            print('好像不能吃了哦')
            print('请换一个苹果')
            da2 = int(input("请输入天数"))
            tem2 = int(input('请输入温度'))
            apple2 = apple(da2,tem2)
            print(apple2.rot())
        else:
            print('选择成功')
            print('美味的苹果，请吃')
        return self.mold
da1 = int(input("输入苹果存放天数"))
tem1 = int(input("输入存放温度"))
apple1 = apple(da1,tem1)

print(apple1.rot())
