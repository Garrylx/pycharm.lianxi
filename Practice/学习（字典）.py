"""author = "GARRY GY"
Date:2021-01-24

"""
list(range(0,10))#把0-10 生成一个列表

a = {"a":1,"b":2,"c":3}

print(a.keys())#输出字典中每一个键

print(a.values())#输出字典的值集合

print(a.items())#获得键值对的输出 方式一

for k,v in a.items():  #获得键值对输出 方式二
    print(k,v)

"a" in a.keys()  #判断键是否在字典中
"a" in a.values() #判断值是否在

#取得键之前先设置默认值，保证不出Error:若键值对存在不添加，若存在则无作用，不添加
a.setdefault("a")
