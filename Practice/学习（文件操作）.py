"""author = "GARRY GY"
Date:2020-11-22

"""
"""
import os
os.path.join("D:",
             "filetexting"
             "st.txt")

os.makedirs("xx1/xx2")#在当前路径下创建
os.makedirs("C://user//Desktop//texte.txt")#绝对路径创建

print(os.getcwd())#得到当前工作目录

os.chdir()    #G更改工作目录#("c:\\windows")
#看的时候把“”“删除
"""



#读取文件
"""
with open("x") as file:
    content = file.read()#全部读取

    l = file.readlines()#按列表读取

    for i in file:
        print(i.rstrip())#按行读取

    print(content)
    print(l)

with open ("x","w") as f1:
    f1.write("beibao")
    """

#add模式
"""
with open("text","w") as f:
    f.write("kkk")
    f.close()

f1 = open("text","a")
f1.write("llll")
f1.close()

#会创建项目
f2 = open("text1","a")
f1,write("abc")
f1.close()
"""
#无模式默认r
#open("text")

# readline 每一次一行逐行读取
# 访问模式




