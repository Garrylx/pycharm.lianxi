"""author = "GARRY GY"
Date:2021-07-08
Tip:
When asked what's the biggest mistake we make in life
.The biggest mistake is you think you have time ,time is free
but it's priceless .You can't own it, but you can use it .you 
can't keep it ,but you can spend it .And once it lost ,you can't
get it back.  
"""
# 存储数据位置 student.data
# 加载数据文件
# 修改数据后保存到文件
# 列表存储
# 添加学员 删除学员 修改学院 查询学员信息 显示所有学员信息 保存学员信息

# 定义程序入口函数，调用函数后启用以下功能
# 加载数据
# 显示功能菜单
# 用户输入功能介绍
# 根据用户输入的序号执行不同的功能
from student import *

class ManagerSystem(object):
    def __init__(self):

        self.student_list = [] # 直接传入不需要用户输入

    def run(self):
        self.show_menu()

        while 1:
            choose_x = int(input("请输入选项"))

            if choose_x == 1:
                self.add_student()

            elif choose_x == 2:
                self.del_student()

            elif choose_x == 3:
                self.modify_student()

            elif choose_x == 4:
                print(self.show_student())

            elif choose_x == 5:
                self.save_student()

            elif choose_x == 6:
                self.load_student()

            elif choose_x == 7:
                self.search_student()

            elif choose_x == 8:

                break

            elif choose_x == 9:
                self.show_menu()

    @staticmethod
    def show_menu():
            print("""
            请选择功能
            1:添加学员
            2：删除学员信息
            3：修改学员信息
            4：展示学员信息
            5：保存学员信息
            6：加载所有学员信息
            7：查询学员信息
            8：退出
            9: 展示选项信息
            """)

    def add_student(self):
        name = input("请输入名字")
        age = input("请输入年龄")
        gender = input("请输入性别")
        tel = input("请输入电话号码")
        student = Student(name,gender,age,tel)
        self.student_list.append(student)
        print("添加完成")

        print("")

    def del_student(self):
        print("若想清空请输入！")
        print("批量删除请输入all,并用空格分割")
        print("或请输入想删除的学员")
        button = input()
        if button == "!":
            self.student_list = []
        elif button == "all":
            names = button.split()
            for i in names:
                self.student_list.remove(i)
        elif button in self.student_list:
            self.student_list.remove(button)
        else:
            print("非法输入")


    def modify_student(self):
        name = input("请输入需要修改的学员名字")
        check = 0
        for i in self.student_list:
            if i.name == name:
                print(i)
                i.name = input("name")
                i.gender = input("gender")
                i.age = input("age")
                i.tel = input("tel")
                check = 1
        if check == 0:
            print("学员不存在")
        else:
            print("修改完成")



    def search_student(self):
        name1 = input("请输入一个需要查询的学员")
        for i in self.student_list:
            if i.name == name1:
                print(i)

    def show_student(self):
        for i in self.student_list:
            print(i)
        return "打印完成"

    def save_student(self):
        # 保存到文件中
        f = open("students.data","w")
        dict = [i.__dict__ for i in self.student_list]
        f.write(str(dict))
        f.close()
    def load_student(self):
        # 先加载数据
        try:
            f = open("student.data", "r")
        except:
            f = open("student.data", "w")
        else:
            data = f.read()# 已有这个文件的时候的操作

            new_list = eval(data)
            print(new_list)
            self.student_list = [Student(i["name"],i["gender"],i["age"],i["tel"] )for i in new_list]
        finally:
            f.close()

